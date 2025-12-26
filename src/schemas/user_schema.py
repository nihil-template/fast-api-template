from typing import Optional

from pydantic import BaseModel, EmailStr, model_validator

from src.models import UserRole, YnStatus


# 요청 스키마
class CreateUser(BaseModel):
  emlAddr: EmailStr
  userNm: str
  password: str
  userRole: UserRole = UserRole.USER


class DeleteUserRequest(BaseModel):
  """사용자 삭제 요청 VO (단건 또는 다건 삭제)"""

  userNo: Optional[int] = None
  userNoList: Optional[list[int]] = None


class UpdateUser(BaseModel):
  emlAddr: Optional[EmailStr] = None
  userNm: Optional[str] = None
  userRole: Optional[UserRole] = None
  proflImg: Optional[str] = None
  userBiogp: Optional[str] = None
  password: Optional[str] = None
  useYn: Optional[YnStatus] = None
  delYn: Optional[YnStatus] = None
  lastLgnDt: Optional[str] = None
  lastPswdChgDt: Optional[str] = None
  updtDt: Optional[str] = None
  delDt: Optional[str] = None
  updtNo: Optional[int] = None
  delNo: Optional[int] = None


# 응답 스키마
class UserResponse(BaseModel):
  userNo: Optional[int]
  emlAddr: str
  userNm: str
  userRole: UserRole
  proflImg: Optional[str]
  userBiogp: Optional[str]
  encptPswd: Optional[str] = None  # 보안상 항상 null로 반환
  reshToken: Optional[str] = None  # 보안상 항상 null로 반환
  useYn: YnStatus
  delYn: YnStatus
  lastLgnDt: Optional[str]
  lastPswdChgDt: Optional[str]
  crtNo: Optional[int]
  crtDt: str
  updtNo: Optional[int]
  updtDt: str
  delNo: Optional[int]
  delDt: Optional[str]

  class Config:
    from_attributes = True

  @model_validator(mode='after')
  def mask_sensitive_fields(self):
    """비밀번호와 리프레시 토큰을 항상 null로 설정"""
    self.encptPswd = None
    self.reshToken = None
    return self
