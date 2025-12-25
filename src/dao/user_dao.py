from typing import Optional

from sqlmodel import Session, select

from src.models import UserInfo, YnStatus


class UserDAO:
  """사용자 데이터 접근 객체"""

  @staticmethod
  def create_user(session: Session, user_data: dict) -> UserInfo:
    """사용자 생성"""
    user = UserInfo(**user_data)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

  @staticmethod
  def get_user_by_no(session: Session, user_no: int) -> Optional[UserInfo]:
    """번호로 사용자 조회"""
    statement = select(UserInfo).where(UserInfo.userNo == user_no)
    return session.exec(statement).first()

  @staticmethod
  def get_user_by_email(session: Session, eml_addr: str) -> Optional[UserInfo]:
    """이메일로 사용자 조회"""
    statement = select(UserInfo).where(UserInfo.emlAddr == eml_addr)
    return session.exec(statement).first()

  @staticmethod
  def get_user_by_username(session: Session, user_nm: str) -> Optional[UserInfo]:
    """사용자명으로 사용자 조회"""
    statement = select(UserInfo).where(UserInfo.userNm == user_nm)
    return session.exec(statement).first()

  @staticmethod
  def get_users(session: Session, skip: int = 0, limit: int = 100) -> list[UserInfo]:
    """모든 사용자 조회 (페이지네이션)"""
    statement = select(UserInfo).offset(skip).limit(limit)
    return list(session.exec(statement).all())

  @staticmethod
  def update_user(session: Session, user: UserInfo, update_data: dict) -> UserInfo:
    """사용자 정보 업데이트"""
    for key, value in update_data.items():
      if value is not None:
        setattr(user, key, value)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

  @staticmethod
  def delete_user(session: Session, user: UserInfo) -> None:
    """사용자 삭제 (소프트 삭제)"""
    user.delYn = YnStatus.Y
    session.add(user)
    session.commit()
