from typing import Optional

from sqlmodel import Session

from src.dao.user_dao import UserDAO
from src.models import UserInfo
from src.schemas.user_schema import UserCreate, UserUpdate


class UserService:
  """사용자 비즈니스 로직 서비스"""

  def __init__(self, session: Session):
    self.session = session
    self.dao = UserDAO()

  def create_user(self, user_data: UserCreate) -> UserInfo:
    """사용자 생성"""
    # 이메일 중복 체크
    existing_user = self.dao.get_user_by_email(self.session, user_data.emlAddr)
    if existing_user:
      raise ValueError(f'이미 존재하는 이메일입니다: {user_data.emlAddr}')

    # 사용자명 중복 체크
    existing_username = self.dao.get_user_by_username(self.session, user_data.userNm)
    if existing_username:
      raise ValueError(f'이미 존재하는 사용자명입니다: {user_data.userNm}')

    # 사용자 생성
    user_dict = user_data.model_dump()
    return self.dao.create_user(self.session, user_dict)

  def get_user_by_id(self, user_no: int) -> Optional[UserInfo]:
    """번호로 사용자 조회"""
    return self.dao.get_user_by_no(self.session, user_no)

  def get_user_by_email(self, eml_addr: str) -> Optional[UserInfo]:
    """이메일로 사용자 조회"""
    return self.dao.get_user_by_email(self.session, eml_addr)

  def get_all_users(self, skip: int = 0, limit: int = 100) -> list[UserInfo]:
    """모든 사용자 조회"""
    return self.dao.get_users(self.session, skip=skip, limit=limit)

  def update_user(self, user_no: int, update_data: UserUpdate) -> Optional[UserInfo]:
    """사용자 정보 업데이트"""
    user = self.dao.get_user_by_no(self.session, user_no)
    if not user:
      return None

    # 사용자명 변경 시 중복 체크
    if update_data.userNm and update_data.userNm != user.userNm:
      existing_user = self.dao.get_user_by_username(self.session, update_data.userNm)
      if existing_user:
        raise ValueError(f'이미 존재하는 사용자명입니다: {update_data.userNm}')

    update_dict = update_data.model_dump(exclude_unset=True)
    return self.dao.update_user(self.session, user, update_dict)

  def delete_user(self, user_no: int) -> bool:
    """사용자 삭제"""
    user = self.dao.get_user_by_no(self.session, user_no)
    if not user:
      return False

    self.dao.delete_user(self.session, user)
    return True
