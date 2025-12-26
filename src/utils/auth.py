"""인증 관련 유틸리티"""

from typing import Annotated, Optional

from fastapi import Cookie, Depends, HTTPException, Request, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlmodel import Session

from src.db import get_session
from src.messages.auth_message import AuthMessage
from src.services.auth_service import AuthService
from src.utils.jwt import verify_access_token

# HTTP Bearer 토큰 스키마
security = HTTPBearer(auto_error=False)


def get_auth_service(session: Session = Depends(get_session)) -> AuthService:
  """AuthService 의존성 주입"""
  return AuthService(session)


def _get_current_user_id_internal(
  request: Request,
  credentials: Annotated[
    Optional[HTTPAuthorizationCredentials], Security(security)
  ] = None,
  access_token: Annotated[Optional[str], Cookie()] = None,
  service: AuthService = Depends(get_auth_service),
  required: bool = True,
) -> Optional[int]:
  """현재 로그인한 사용자 ID 추출 (내부 함수)

  Args:
    request: FastAPI Request 객체
    credentials: Authorization 헤더에서 추출한 인증 정보
    access_token: 쿠키에서 추출한 액세스 토큰
    service: AuthService 인스턴스
    required: True면 토큰이 없을 때 에러 발생, False면 None 반환

  Returns:
    사용자 번호 (required=False이고 토큰이 없으면 None)
  """
  token: Optional[str] = None

  # 1. Authorization 헤더에서 토큰 읽기
  if credentials:
    token = credentials.credentials
  # 2. 쿠키에서 토큰 읽기
  elif access_token:
    token = access_token

  if not token:
    if required:
      raise HTTPException(
        status_code=status.HTTP_200_OK,
        detail={
          'data': None,
          'error': True,
          'code': 'UNAUTHORIZED',
          'message': AuthMessage.TOKEN_INVALID,
        },
      )
    return None

  payload = verify_access_token(token)
  if not payload:
    if required:
      raise HTTPException(
        status_code=status.HTTP_200_OK,
        detail={
          'data': None,
          'error': True,
          'code': 'UNAUTHORIZED',
          'message': AuthMessage.TOKEN_INVALID,
        },
      )
    return None

  user_no = int(payload.get('sub', 0))
  user = service.get_current_user(token)
  if not user:
    if required:
      raise HTTPException(
        status_code=status.HTTP_200_OK,
        detail={
          'data': None,
          'error': True,
          'code': 'UNAUTHORIZED',
          'message': AuthMessage.USER_NOT_FOUND,
        },
      )
    return None

  return user_no


def get_current_user_id(
  request: Request,
  credentials: Annotated[
    Optional[HTTPAuthorizationCredentials], Security(security)
  ] = None,
  access_token: Annotated[Optional[str], Cookie()] = None,
  service: AuthService = Depends(get_auth_service),
) -> int:
  """현재 로그인한 사용자 ID 추출 (필수 - 토큰이 없으면 에러 반환)"""
  result = _get_current_user_id_internal(
    request, credentials, access_token, service, required=True
  )
  # required=True이므로 result는 항상 int
  return result  # type: ignore[return-value]


def get_current_user_id_optional(
  request: Request,
  credentials: Annotated[
    Optional[HTTPAuthorizationCredentials], Security(security)
  ] = None,
  access_token: Annotated[Optional[str], Cookie()] = None,
  service: AuthService = Depends(get_auth_service),
) -> Optional[int]:
  """현재 로그인한 사용자 ID 추출 (선택적 - 토큰이 없으면 None 반환)"""
  return _get_current_user_id_internal(
    request, credentials, access_token, service, required=False
  )
