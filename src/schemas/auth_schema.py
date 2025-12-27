"""인증 관련 스키마 정의"""

from typing import Optional

from pydantic import BaseModel, EmailStr


class LoginRequest(BaseModel):
  """로그인 요청 스키마"""

  emlAddr: EmailStr
  password: str


class LoginResponse(BaseModel):
  """로그인 응답 스키마"""

  accessToken: Optional[str] = None
  refreshToken: Optional[str] = None
  tokenType: str = 'bearer'


class LogoutRequest(BaseModel):
  """로그아웃 요청 스키마"""

  refreshToken: str | None = None


class ResetPasswordRequestRequest(BaseModel):
  """비밀번호 재설정 요청 스키마 (이메일 검증)"""

  emlAddr: EmailStr


class ResetPasswordRequest(BaseModel):
  """비밀번호 재설정 스키마 (실제 재설정)"""

  emlAddr: EmailStr
  resetToken: str  # 이메일로 받은 인증 토큰
  newPassword: str


class ChangePasswordRequest(BaseModel):
  """비밀번호 변경 스키마 (로그인 후)"""

  currentPassword: str
  newPassword: str
