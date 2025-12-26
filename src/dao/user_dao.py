from typing import Optional

from sqlmodel import Session, select

from src.models import UserInfo, UserRole, YnStatus
from src.vos.user_vo import UserVo


class UserDAO:
  """사용자 데이터 접근 객체"""

  @staticmethod
  def create_user(session: Session, user_vo: UserVo) -> UserInfo:
    """사용자 생성 (UserVo를 받아서 Entity로 변환)"""
    print('[DAO] user_vo:', user_vo.model_dump())
    # Service에서 이미 비밀번호 해시화 등 변환 완료
    user = UserInfo(
      emlAddr=user_vo.emlAddr,
      userNm=user_vo.userNm,
      encptPswd=user_vo.encptPswd,
      userRole=user_vo.userRole or UserRole.USER,
      useYn=YnStatus.Y if user_vo.useYn is None else user_vo.useYn,  # 기본값 필수
      delYn=YnStatus.N if user_vo.delYn is None else user_vo.delYn,  # 기본값 필수
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    print('[DAO] user_entity:', user)
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
  def get_users(session: Session, user_vo: Optional[UserVo] = None) -> list[UserInfo]:
    """사용자 목록 조회 (UserVo의 검색 조건 활용)"""
    statement = select(UserInfo)

    if user_vo:
      # VO에서 검색 조건 추출
      if user_vo.userNm:
        statement = statement.where(UserInfo.userNm == user_vo.userNm)
      if user_vo.emlAddr:
        statement = statement.where(UserInfo.emlAddr == user_vo.emlAddr)
      if user_vo.userRole:
        statement = statement.where(UserInfo.userRole == user_vo.userRole)
      if user_vo.useYn:
        statement = statement.where(UserInfo.useYn == user_vo.useYn)
      if user_vo.delYn:
        statement = statement.where(UserInfo.delYn == user_vo.delYn)
      # 검색 키워드 활용 (srchType과 srchKywd 조합)
      if user_vo.srchKywd:
        from sqlmodel import col

        search_pattern = f'%{user_vo.srchKywd}%'
        if user_vo.srchType == 'userNm':
          statement = statement.where(col(UserInfo.userNm).like(search_pattern))
        elif user_vo.srchType == 'emlAddr':
          statement = statement.where(col(UserInfo.emlAddr).like(search_pattern))
        else:
          # 기본: 사용자명 또는 이메일에서 검색
          statement = statement.where(
            (col(UserInfo.userNm).like(search_pattern))
            | (col(UserInfo.emlAddr).like(search_pattern))
          )

    return list(session.exec(statement).all())

  @staticmethod
  def update_user(session: Session, user: UserInfo, user_vo: UserVo) -> UserInfo:
    """사용자 정보 업데이트 (UserVo를 받아서 Entity 업데이트)"""
    # Service에서 이미 비밀번호 해시화 등 변환 완료
    # VO에서 None이 아니고 설정된 값만 추출 (password, 검색 필드 제외)
    update_data = user_vo.model_dump(
      exclude_unset=True,
      exclude_none=True,
      exclude={
        'password',  # password는 encptPswd로 변환되어 있음
        'userNo',  # userNo는 업데이트 대상이 아님
        'userNoList',  # 확장 필드
        'page',  # SearchVo 필드
        'pageSz',
        'strtRow',
        'endRow',
        'srchType',
        'srchKywd',
      },
    )

    # Entity에 존재하는 필드만 업데이트
    for key, value in update_data.items():
      if hasattr(user, key):
        setattr(user, key, value)

    session.add(user)
    session.commit()
    session.refresh(user)
    return user

  @staticmethod
  def delete_user(session: Session, user: UserInfo) -> None:
    """사용자 삭제 (소프트 삭제)"""
    user.useYn = YnStatus.N
    user.delYn = YnStatus.Y
    session.add(user)
    session.commit()

  @staticmethod
  def delete_users(session: Session, users: list[UserInfo]) -> None:
    """다건 사용자 삭제 (소프트 삭제)"""
    for user in users:
      user.useYn = YnStatus.N
      user.delYn = YnStatus.Y
      session.add(user)
    session.commit()
