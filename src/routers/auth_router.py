"""인증 관련 라우터"""

from typing import Annotated, Optional

from fastapi import APIRouter, BackgroundTasks, Depends, Request, Response, status
from sqlmodel import Session

from src.db import get_session
from src.schemas.auth_schema import (
  ChangePasswordRequest,
  LoginRequest,
  LoginResponse,
  ResetPasswordRequest,
  ResetPasswordRequestRequest,
)
from src.schemas.response_schema import ApiResponse
from src.services.auth_service import AuthService
from src.settings import settings
from src.utils.auth_helper import get_current_user_id, get_refresh_token_from_cookie
from src.utils.jwt_helper import parse_expiration

router = APIRouter(prefix='/auth', tags=['인증'])


def get_auth_service(session: Session = Depends(get_session)) -> AuthService:
  """AuthService 의존성 주입"""
  return AuthService(session)


@router.post(
  '/signin',
  response_model=ApiResponse[LoginResponse],
  status_code=status.HTTP_200_OK,
  summary='로그인',
  operation_id='signIn',
)
def signin(
  login_request: LoginRequest,
  response: Response,
  service: AuthService = Depends(get_auth_service),
):
  """이메일과 비밀번호로 로그인합니다."""
  result = service.signin(login_request)

  if result.error is False and result.data:
    access_token = result.data.accessToken
    refresh_token = result.data.refreshToken

    # HTTPOnly 쿠키에 토큰 설정 (토큰이 None이 아닌 경우에만)
    if access_token and refresh_token:
      access_token_max_age = int(parse_expiration(settings.ACCESS_EXP).total_seconds())
      refresh_token_max_age = int(
        parse_expiration(settings.REFRESH_EXP).total_seconds()
      )

      response.set_cookie(
        key='access_token',
        value=access_token,
        max_age=access_token_max_age,
        httponly=True,
        samesite='strict',  # CSRF 보호
        secure=True,  # HTTPS 전용
      )
      response.set_cookie(
        key='refresh_token',
        value=refresh_token,
        max_age=refresh_token_max_age,
        httponly=True,
        samesite='strict',
        secure=True,
      )

    # 응답 본문에서 토큰 제거
    result.data.accessToken = None
    result.data.refreshToken = None

  return result


@router.post(
  '/signout',
  response_model=ApiResponse[None],
  status_code=status.HTTP_200_OK,
  summary='로그아웃',
  operation_id='signOut',
)
def signout(
  response: Response,
  refresh_token: Annotated[Optional[str], Depends(get_refresh_token_from_cookie)],
  service: AuthService = Depends(get_auth_service),
):
  """로그아웃합니다."""
  result = service.signout(refresh_token)

  # 쿠키 삭제
  response.delete_cookie(key='access_token', samesite='strict', secure=True)
  response.delete_cookie(key='refresh_token', samesite='strict', secure=True)

  return result


@router.post(
  '/refresh',
  response_model=ApiResponse[LoginResponse],
  status_code=status.HTTP_200_OK,
  summary='Access Token 재발급 (Refresh Token 사용)',
  operation_id='refreshToken',
)
def refresh_token(
  response: Response,
  refresh_token: Annotated[str, Depends(get_refresh_token_from_cookie)],
  service: AuthService = Depends(get_auth_service),
):
  """Refresh Token을 사용하여 새로운 Access Token과 Refresh Token을 발급합니다."""
  result = service.refresh(refresh_token)

  if result.error is False and result.data:
    access_token = result.data.accessToken
    new_refresh_token = result.data.refreshToken

    # HTTPOnly 쿠키에 새로운 토큰 설정 (토큰이 None이 아닌 경우에만)
    if access_token and new_refresh_token:
      access_token_max_age = int(parse_expiration(settings.ACCESS_EXP).total_seconds())
      refresh_token_max_age = int(
        parse_expiration(settings.REFRESH_EXP).total_seconds()
      )

      response.set_cookie(
        key='access_token',
        value=access_token,
        max_age=access_token_max_age,
        httponly=True,
        samesite='strict',
        secure=True,
      )
      response.set_cookie(
        key='refresh_token',
        value=new_refresh_token,
        max_age=refresh_token_max_age,
        httponly=True,
        samesite='strict',
        secure=True,
      )

    # 응답 본문에서 토큰 제거
    result.data.accessToken = None
    result.data.refreshToken = None

  return result


@router.post(
  '/reset-password/request',
  response_model=ApiResponse[None],
  status_code=status.HTTP_200_OK,
  summary='비밀번호 재설정 요청',
  operation_id='requestResetPassword',
)
def request_reset_password(
  background_tasks: BackgroundTasks,
  request: ResetPasswordRequestRequest,
  service: AuthService = Depends(get_auth_service),
):
  """비밀번호 재설정을 위한 이메일을 발송합니다."""
  result = service.request_reset_password(request)

  # 성공 응답인 경우에만 이메일 발송 (백그라운드 작업)
  if result.error is False:
    from src.services.auth_service import reset_tokens
    from src.utils.email_helper import send_reset_password_email

    token_info = reset_tokens.get(request.emlAddr)
    if token_info:
      background_tasks.add_task(
        send_reset_password_email, request.emlAddr, token_info['token']
      )

  return result


@router.post(
  '/reset-password',
  response_model=ApiResponse[None],
  status_code=status.HTTP_200_OK,
  summary='비밀번호 재설정',
  operation_id='resetPassword',
)
def reset_password(
  request: ResetPasswordRequest,
  service: AuthService = Depends(get_auth_service),
):
  """비밀번호를 재설정합니다."""
  return service.reset_password(request)


@router.post(
  '/change-password',
  response_model=ApiResponse[None],
  status_code=status.HTTP_200_OK,
  summary='비밀번호 변경',
  operation_id='changePassword',
)
def change_password(
  request: Request,
  change_request: ChangePasswordRequest,
  user_no: int = Depends(get_current_user_id),
  service: AuthService = Depends(get_auth_service),
):
  """로그인 후 비밀번호를 변경합니다."""
  return service.change_password(user_no, change_request)
