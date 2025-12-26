"""인증 관련 비즈니스 로직 서비스"""

from datetime import datetime, timezone
from typing import Optional

from sqlmodel import Session

from src.dao.user_dao import UserDAO
from src.messages.auth_message import AuthMessage
from src.models import YnStatus
from src.schemas.auth_schema import (
  ChangePasswordRequest,
  LoginRequest,
  LoginResponse,
  ResetPasswordRequest,
  ResetPasswordRequestRequest,
)
from src.schemas.response_code import ResponseCode
from src.schemas.response_schema import ApiResponse
from src.utils.jwt import (
  create_access_token,
  create_refresh_token,
  verify_access_token,
  verify_refresh_token,
)
from src.utils.password import hash_password, verify_password
from src.utils.response import error_response, success_response

# 비밀번호 재설정 토큰 저장소 (실제 프로덕션에서는 Redis나 DB 사용 권장)
reset_tokens: dict[str, dict] = {}


class AuthService:
  """인증 비즈니스 로직 서비스"""

  def __init__(self, session: Session):
    self.session = session
    self.dao = UserDAO()

  def login(self, login_request: LoginRequest) -> ApiResponse[LoginResponse]:
    """로그인"""
    # 이메일로 사용자 조회
    user_entity = self.dao.get_user_by_email(self.session, login_request.emlAddr)
    if not user_entity:
      return error_response(
        message=AuthMessage.LOGIN_FAILED,
        code=ResponseCode.UNAUTHORIZED,
      )

    # 사용자 상태 확인
    if user_entity.useYn != YnStatus.Y or user_entity.delYn != YnStatus.N:
      return error_response(
        message=AuthMessage.USER_DISABLED,
        code=ResponseCode.FORBIDDEN,
      )

    # 비밀번호 검증
    if not verify_password(login_request.password, user_entity.encptPswd):
      return error_response(
        message=AuthMessage.LOGIN_FAILED,
        code=ResponseCode.UNAUTHORIZED,
      )

    # 마지막 로그인 시간 업데이트
    user_entity.lastLgnDt = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    user_entity.updtNo = user_entity.userNo
    user_entity.updtDt = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    self.session.add(user_entity)
    self.session.commit()

    # JWT 토큰 생성 (사용자 번호, 이름, 이메일, userRole 포함)
    token_data = {
      'sub': str(user_entity.userNo),
      'userNm': user_entity.userNm,
      'email': user_entity.emlAddr,
      'userRole': user_entity.userRole.value,
    }
    access_token = create_access_token(token_data)
    refresh_token = create_refresh_token(token_data)

    # Refresh Token을 DB에 저장
    user_entity.reshToken = refresh_token
    user_entity.updtNo = user_entity.userNo
    user_entity.updtDt = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    self.session.add(user_entity)
    self.session.commit()

    login_response = LoginResponse(accessToken=access_token, refreshToken=refresh_token)

    return success_response(
      data=login_response,
      message=AuthMessage.LOGIN_SUCCESS,
      code=ResponseCode.OK,
    )

  def logout(self, refresh_token: Optional[str]) -> ApiResponse[None]:
    """로그아웃"""
    if refresh_token:
      # Refresh Token 검증
      payload = verify_refresh_token(refresh_token)
      if payload:
        user_no = int(payload.get('sub', 0))
        user_entity = self.dao.get_user_by_no(self.session, user_no)
        if user_entity and user_entity.reshToken == refresh_token:
          # Refresh Token 제거
          user_entity.reshToken = None
          user_entity.updtNo = user_no
          user_entity.updtDt = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
          self.session.add(user_entity)
          self.session.commit()

    return success_response(
      message=AuthMessage.LOGOUT_SUCCESS,
      code=ResponseCode.OK,
    )

  def request_reset_password(
    self, request: ResetPasswordRequestRequest
  ) -> ApiResponse[None]:
    """비밀번호 재설정 요청 (이메일 검증)"""
    user_entity = self.dao.get_user_by_email(self.session, request.emlAddr)
    if not user_entity:
      # 보안을 위해 사용자가 존재하지 않아도 성공 메시지 반환
      return success_response(
        message=AuthMessage.RESET_PASSWORD_REQUEST_SUCCESS,
        code=ResponseCode.OK,
      )

    # 비밀번호 재설정 토큰 생성 (간단하게 JWT 사용)
    token_data = {
      'sub': str(user_entity.userNo),
      'email': user_entity.emlAddr,
      'type': 'reset',
    }
    reset_token = create_access_token(token_data)  # ACCESS_TOKEN_SECRET 사용

    # 토큰 저장 (실제 프로덕션에서는 Redis나 DB 사용)
    reset_tokens[request.emlAddr] = {
      'token': reset_token,
      'user_no': user_entity.userNo,
      'created_at': datetime.now(timezone.utc).isoformat(),
    }

    # 실제로는 여기서 이메일을 발송해야 함
    # send_reset_password_email(request.emlAddr, reset_token)

    return success_response(
      message=AuthMessage.RESET_PASSWORD_REQUEST_SUCCESS,
      code=ResponseCode.OK,
    )

  def reset_password(self, request: ResetPasswordRequest) -> ApiResponse[None]:
    """비밀번호 재설정 (실제 재설정)"""
    # 저장된 토큰 확인
    token_info = reset_tokens.get(request.emlAddr)
    if not token_info or token_info['token'] != request.resetToken:
      return error_response(
        message=AuthMessage.RESET_TOKEN_NOT_FOUND,
        code=ResponseCode.BAD_REQUEST,
      )

    # 토큰 검증
    payload = verify_access_token(request.resetToken)
    if not payload or payload.get('type') != 'reset':
      # 토큰 삭제
      reset_tokens.pop(request.emlAddr, None)
      return error_response(
        message=AuthMessage.RESET_TOKEN_INVALID,
        code=ResponseCode.BAD_REQUEST,
      )

    # 사용자 조회
    user_no = token_info['user_no']
    user_entity = self.dao.get_user_by_no(self.session, user_no)
    if not user_entity:
      reset_tokens.pop(request.emlAddr, None)
      return error_response(
        message=AuthMessage.USER_NOT_FOUND,
        code=ResponseCode.NOT_FOUND,
      )

    # 비밀번호 업데이트
    user_entity.encptPswd = hash_password(request.newPassword)
    user_entity.lastPswdChgDt = datetime.now(timezone.utc).strftime(
      '%Y-%m-%dT%H:%M:%SZ'
    )
    user_entity.updtNo = user_entity.userNo
    user_entity.updtDt = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    self.session.add(user_entity)
    self.session.commit()

    # 토큰 삭제
    reset_tokens.pop(request.emlAddr, None)

    return success_response(
      message=AuthMessage.RESET_PASSWORD_SUCCESS,
      code=ResponseCode.OK,
    )

  def change_password(
    self, user_no: int, request: ChangePasswordRequest
  ) -> ApiResponse[None]:
    """비밀번호 변경 (로그인 후)"""
    # 사용자 조회
    user_entity = self.dao.get_user_by_no(self.session, user_no)
    if not user_entity:
      return error_response(
        message=AuthMessage.USER_NOT_FOUND,
        code=ResponseCode.NOT_FOUND,
      )

    # 현재 비밀번호 검증
    if not verify_password(request.currentPassword, user_entity.encptPswd):
      return error_response(
        message=AuthMessage.CURRENT_PASSWORD_INCORRECT,
        code=ResponseCode.UNAUTHORIZED,
      )

    # 새 비밀번호가 현재 비밀번호와 같은지 확인
    if verify_password(request.newPassword, user_entity.encptPswd):
      return error_response(
        message=AuthMessage.NEW_PASSWORD_SAME,
        code=ResponseCode.BAD_REQUEST,
      )

    # 비밀번호 업데이트
    user_entity.encptPswd = hash_password(request.newPassword)
    user_entity.lastPswdChgDt = datetime.now(timezone.utc).strftime(
      '%Y-%m-%dT%H:%M:%SZ'
    )
    user_entity.updtNo = user_no
    user_entity.updtDt = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    self.session.add(user_entity)
    self.session.commit()

    return success_response(
      message=AuthMessage.CHANGE_PASSWORD_SUCCESS,
      code=ResponseCode.OK,
    )

  def get_current_user(self, token: str):
    """현재 사용자 정보 조회 (토큰에서)"""
    payload = verify_access_token(token)
    if not payload:
      return None

    user_no = int(payload.get('sub', 0))
    return self.dao.get_user_by_no(self.session, user_no)
