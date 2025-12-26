"""사용자 관련 VO (Value Object) 정의

자원별로 하나의 VO만 사용하여 모든 작업(get, post, update, delete)을 처리합니다.
테이블의 모든 컬럼을 담고, 필요한 확장 필드를 추가로 포함합니다.
"""

from typing import Optional

from pydantic import EmailStr

from src.models import UserRole, YnStatus
from src.vos.search_vo import SearchVo


class UserVo(SearchVo):
  """사용자 VO (모든 작업에서 사용)

  테이블의 모든 컬럼을 포함하고, 필요한 확장 필드를 추가로 포함합니다.
  이 하나의 VO로 get, post, update, delete 모든 작업을 처리합니다.
  """

  # 테이블 필드 (모두 Optional로 정의하여 검색/생성/수정/삭제 모두에서 사용)
  userNo: Optional[int] = None
  emlAddr: Optional[EmailStr] = None
  userNm: Optional[str] = None
  userRole: Optional[UserRole] = None
  password: Optional[str] = None  # 입력용 (Service에서 encptPswd로 변환)
  encptPswd: Optional[str] = None  # 저장용 (Service에서 해시화된 값)
  proflImg: Optional[str] = None
  userBiogp: Optional[str] = None
  reshToken: Optional[str] = None
  useYn: Optional[YnStatus] = None
  delYn: Optional[YnStatus] = None
  lastLgnDt: Optional[str] = None
  lastPswdChgDt: Optional[str] = None
  crtNo: Optional[int] = None
  crtDt: Optional[str] = None
  updtNo: Optional[int] = None
  updtDt: Optional[str] = None
  delNo: Optional[int] = None
  delDt: Optional[str] = None

  # 확장 필드 (검색 조건, 계산된 필드 등)
  userNoList: Optional[list[int]] = None  # 검색/삭제용

  class Config:
    from_attributes = True
