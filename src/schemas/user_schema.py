from typing import Optional

from pydantic import BaseModel, EmailStr, model_validator

from src.models import UserRole, YnStatus


# 요청 스키마
class UserCreate(BaseModel):
  emlAddr: EmailStr
  userNm: str
  encptPswd: str
  userRole: UserRole = UserRole.USER


class UserUpdate(BaseModel):
  emlAddr: Optional[EmailStr] = None
  userNm: Optional[str] = None
  userRole: Optional[UserRole] = None
  proflImg: Optional[str] = None
  userBiogp: Optional[str] = None
  encptPswd: Optional[str] = None
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

  @model_validator(mode='before')
  @classmethod
  def mask_sensitive_fields(cls, data):
    """비밀번호와 리프레시 토큰을 항상 null로 설정"""
    if isinstance(data, dict):
      data['encptPswd'] = None
      data['reshToken'] = None
    return data
