"""인증 관련 라우터"""

from fastapi import APIRouter, Depends, Request, status
from sqlmodel import Session

from src.db import get_session
from src.schemas.auth_schema import (
  ChangePasswordRequest,
  LoginRequest,
  LoginResponse,
  LogoutRequest,
  ResetPasswordRequest,
  ResetPasswordRequestRequest,
)
from src.schemas.response_schema import ApiResponse
from src.services.auth_service import AuthService
from src.utils.auth import get_current_user_id

router = APIRouter(prefix='/auth', tags=['인증'])


def get_auth_service(session: Session = Depends(get_session)) -> AuthService:
  """AuthService 의존성 주입"""
  return AuthService(session)


@router.post(
  '/login',
  response_model=ApiResponse[LoginResponse],
  status_code=status.HTTP_200_OK,
  summary='로그인',
  operation_id='login',
)
def login(
  login_request: LoginRequest,
  service: AuthService = Depends(get_auth_service),
):
  """이메일과 비밀번호로 로그인합니다."""
  return service.login(login_request)


@router.post(
  '/logout',
  response_model=ApiResponse[None],
  status_code=status.HTTP_200_OK,
  summary='로그아웃',
  operation_id='logout',
)
def logout(
  logout_request: LogoutRequest,
  service: AuthService = Depends(get_auth_service),
):
  """로그아웃합니다."""
  return service.logout(logout_request.refreshToken)


@router.post(
  '/reset-password/request',
  response_model=ApiResponse[None],
  status_code=status.HTTP_200_OK,
  summary='비밀번호 재설정 요청',
  operation_id='requestResetPassword',
)
def request_reset_password(
  request: ResetPasswordRequestRequest,
  service: AuthService = Depends(get_auth_service),
):
  """비밀번호 재설정을 위한 이메일을 발송합니다."""
  return service.request_reset_password(request)


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
