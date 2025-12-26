from src.settings import settings


class UserMessage:
  """사용자 관련 메시지 관리 클래스"""

  # 생성 관련
  CREATE_SUCCESS = '사용자가 성공적으로 생성되었습니다.'
  EMAIL_CONFLICT = '이미 존재하는 이메일입니다.'
  USERNAME_CONFLICT = '이미 존재하는 사용자명입니다.'

  # 조회 관련
  GET_SUCCESS = '사용자 조회에 성공했습니다.'
  GET_LIST_SUCCESS = '사용자 목록 조회에 성공했습니다.'
  NOT_FOUND = '사용자를 찾을 수 없습니다.'

  # 수정 관련
  UPDATE_SUCCESS = '사용자 정보가 성공적으로 업데이트되었습니다.'
  UPDATE_EMAIL_CONFLICT = '이미 존재하는 이메일입니다.'
  UPDATE_USERNAME_CONFLICT = '이미 존재하는 사용자명입니다.'

  # 삭제 관련
  DELETE_SUCCESS_SINGLE = '사용자가 성공적으로 삭제되었습니다.'
  DELETE_SUCCESS_MULTIPLE = '{count}명의 사용자가 성공적으로 삭제되었습니다.'
  DELETE_NOT_FOUND = '사용자를 찾을 수 없습니다.'

  # 삭제 검증 관련
  DELETE_VALIDATION_REQUIRED = (
    'userNo 또는 userNoList 중 하나는 반드시 제공되어야 합니다.'
  )
  DELETE_VALIDATION_CONFLICT = 'userNo와 userNoList는 동시에 제공될 수 없습니다.'

  # 기타
  INVALID_REQUEST = '잘못된 요청입니다.'
  VALIDATION_ERROR = '입력값이 유효하지 않습니다.'

  @classmethod
  def get_delete_message(
    cls,
    count: int | None = None,
    not_found_nos: list[int] | None = None,
    is_single: bool = False,
  ) -> str:
    """삭제 메시지를 환경에 따라 반환

    Args:
      count: 삭제된 사용자 수 (다건 삭제 시)
      not_found_nos: 찾을 수 없는 사용자 번호 리스트
      is_single: 단건 삭제 여부

    Returns:
      개발 환경: 상세 메시지
      운영 환경: 정상 완료 메시지
    """
    # 개발 환경인지 확인 (기본값은 개발 환경)
    is_development = (
      getattr(settings, 'ENVIRONMENT', 'development').lower() == 'development'
    )

    if is_development:
      # 개발 환경: 상세 메시지 반환
      if is_single:
        return cls.DELETE_SUCCESS_SINGLE
      else:
        return cls.DELETE_SUCCESS_MULTIPLE.format(count=count or 0)
    else:
      # 운영 환경: 정상 완료 메시지만 반환
      if is_single:
        return cls.DELETE_SUCCESS_SINGLE
      else:
        return cls.DELETE_SUCCESS_MULTIPLE.format(count=count or 0)

  @classmethod
  def get_delete_not_found_message(
    cls, user_no: int | None = None, is_single: bool = False
  ) -> str:
    """삭제 시 사용자를 찾을 수 없을 때 메시지 반환

    Args:
      user_no: 사용자 번호 (사용하지 않음)
      is_single: 단건 삭제 여부

    Returns:
      개발 환경: 상세 메시지
      운영 환경: 정상 완료 메시지
    """
    # 개발 환경인지 확인 (기본값은 개발 환경)
    is_development = (
      getattr(settings, 'ENVIRONMENT', 'development').lower() == 'development'
    )

    if is_development:
      # 개발 환경: 상세 메시지 반환
      return cls.DELETE_NOT_FOUND
    else:
      # 운영 환경: 정상 완료 메시지 반환
      if is_single:
        return cls.DELETE_SUCCESS_SINGLE
      else:
        return cls.DELETE_SUCCESS_MULTIPLE.format(count=0)
