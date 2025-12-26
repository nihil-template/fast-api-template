from typing import Optional

from sqlmodel import Session

from src.dao.user_dao import UserDAO
from src.messages.user_message import UserMessage
from src.schemas.response_code import ResponseCode
from src.schemas.response_schema import ApiResponse, ListResponse
from src.utils.password import hash_password
from src.utils.response import error_response, success_response
from src.vos.user_vo import UserVo


class UserService:
  """사용자 비즈니스 로직 서비스"""

  def __init__(self, session: Session):
    self.session = session
    self.dao = UserDAO()

  def createUser(self, user_vo: UserVo) -> ApiResponse[UserVo]:
    """사용자 생성"""
    print('[SERVICE] user_vo:', user_vo.model_dump())
    # 필수값 검증
    if (
      not user_vo.emlAddr
      or not user_vo.userNm
      or not user_vo.password
      or not user_vo.userRole
    ):
      return error_response(
        message=UserMessage.INVALID_REQUEST,
        code=ResponseCode.VALIDATION_ERROR,
      )

    # 이메일 중복 체크
    existing_user = self.dao.get_user_by_email(self.session, user_vo.emlAddr)
    if existing_user:
      return error_response(
        message=UserMessage.EMAIL_CONFLICT,
        code=ResponseCode.CONFLICT,
      )

    # 사용자명 중복 체크
    existing_username = self.dao.get_user_by_username(self.session, user_vo.userNm)
    if existing_username:
      return error_response(
        message=UserMessage.USERNAME_CONFLICT,
        code=ResponseCode.CONFLICT,
      )

    # 비밀번호 해시화 (password -> encptPswd)
    if user_vo.password:
      user_vo.encptPswd = hash_password(user_vo.password)

    # 사용자 생성
    user_entity = self.dao.create_user(self.session, user_vo)

    # Entity를 VO로 변환하여 반환
    user_response = UserVo.model_validate(user_entity)
    return success_response(
      data=user_response,
      message=UserMessage.CREATE_SUCCESS,
      code=ResponseCode.CREATED,
    )

  def getUserByNo(self, user_vo: UserVo) -> ApiResponse[UserVo]:
    """번호로 사용자 조회"""
    if not user_vo.userNo:
      return error_response(
        message=UserMessage.INVALID_REQUEST, code=ResponseCode.VALIDATION_ERROR
      )

    user_entity = self.dao.get_user_by_no(self.session, user_vo.userNo)
    if not user_entity:
      return error_response(message=UserMessage.NOT_FOUND, code=ResponseCode.NOT_FOUND)

    # Entity를 VO로 변환하여 반환
    user_response = UserVo.model_validate(user_entity)
    return success_response(data=user_response, message=UserMessage.GET_SUCCESS)

  def getUserByEmail(self, user_vo: UserVo) -> ApiResponse[UserVo]:
    """이메일로 사용자 조회"""
    if not user_vo.emlAddr:
      return error_response(
        message=UserMessage.INVALID_REQUEST, code=ResponseCode.VALIDATION_ERROR
      )

    user_entity = self.dao.get_user_by_email(self.session, user_vo.emlAddr)
    if not user_entity:
      return error_response(message=UserMessage.NOT_FOUND, code=ResponseCode.NOT_FOUND)

    # Entity를 VO로 변환하여 반환
    user_response = UserVo.model_validate(user_entity)
    return success_response(data=user_response, message=UserMessage.GET_SUCCESS)

  def getUserList(
    self, user_vo: Optional[UserVo] = None
  ) -> ApiResponse[ListResponse[UserVo]]:
    """사용자 목록 조회 (검색 조건 포함)"""
    user_entities = self.dao.get_users(self.session, user_vo)

    # Entity 리스트를 VO 리스트로 변환
    user_responses = [UserVo.model_validate(u) for u in user_entities]
    list_response = ListResponse(list=user_responses, totalCnt=len(user_responses))
    return success_response(data=list_response, message=UserMessage.GET_LIST_SUCCESS)

  def updateUser(self, user_vo: UserVo) -> ApiResponse[UserVo]:
    """사용자 정보 업데이트 (비밀번호 제외)"""
    if not user_vo.userNo:
      return error_response(
        message=UserMessage.INVALID_REQUEST, code=ResponseCode.VALIDATION_ERROR
      )

    user_entity = self.dao.get_user_by_no(self.session, user_vo.userNo)
    if not user_entity:
      return error_response(message=UserMessage.NOT_FOUND, code=ResponseCode.NOT_FOUND)

    # 이메일 변경 시 중복 체크 (자기 자신 제외)
    if user_vo.emlAddr and user_vo.emlAddr != user_entity.emlAddr:
      existing_user = self.dao.get_user_by_email(self.session, user_vo.emlAddr)
      if existing_user and existing_user.userNo != user_entity.userNo:
        return error_response(
          message=UserMessage.UPDATE_EMAIL_CONFLICT,
          code=ResponseCode.CONFLICT,
        )

    # 사용자명 변경 시 중복 체크 (자기 자신 제외)
    if user_vo.userNm and user_vo.userNm != user_entity.userNm:
      existing_user = self.dao.get_user_by_username(self.session, user_vo.userNm)
      if existing_user and existing_user.userNo != user_entity.userNo:
        return error_response(
          message=UserMessage.UPDATE_USERNAME_CONFLICT,
          code=ResponseCode.CONFLICT,
        )

    updated_user_entity = self.dao.update_user(self.session, user_entity, user_vo)

    # Entity를 VO로 변환하여 반환
    user_response = UserVo.model_validate(updated_user_entity)
    return success_response(
      data=user_response,
      message=UserMessage.UPDATE_SUCCESS,
    )

  def updateUserPassword(self, user_vo: UserVo) -> ApiResponse[UserVo]:
    """사용자 비밀번호 업데이트"""
    if not user_vo.userNo or not user_vo.password:
      return error_response(
        message=UserMessage.INVALID_REQUEST, code=ResponseCode.VALIDATION_ERROR
      )

    user_entity = self.dao.get_user_by_no(self.session, user_vo.userNo)
    if not user_entity:
      return error_response(message=UserMessage.NOT_FOUND, code=ResponseCode.NOT_FOUND)

    # 비밀번호 해시화 (password -> encptPswd)
    user_vo.encptPswd = hash_password(user_vo.password)

    # 비밀번호만 업데이트
    user_entity.encptPswd = user_vo.encptPswd
    self.session.add(user_entity)
    self.session.commit()
    self.session.refresh(user_entity)

    # Entity를 VO로 변환하여 반환
    user_response = UserVo.model_validate(user_entity)
    return success_response(
      data=user_response,
      message=UserMessage.UPDATE_SUCCESS,
    )

  def deleteUser(self, user_vo: UserVo) -> ApiResponse[None]:
    """사용자 단건 삭제"""
    if not user_vo.userNo:
      return error_response(
        message=UserMessage.INVALID_REQUEST, code=ResponseCode.VALIDATION_ERROR
      )

    user_entity = self.dao.get_user_by_no(self.session, user_vo.userNo)
    if not user_entity:
      return success_response(
        message=UserMessage.get_delete_not_found_message(
          user_no=user_vo.userNo, is_single=True
        )
      )

    self.dao.delete_user(self.session, user_entity)
    return success_response(message=UserMessage.get_delete_message(is_single=True))

  def deleteUsers(self, user_vo: UserVo) -> ApiResponse[None]:
    """사용자 다건 삭제"""
    if not user_vo.userNoList or len(user_vo.userNoList) == 0:
      return error_response(
        message=UserMessage.INVALID_REQUEST, code=ResponseCode.VALIDATION_ERROR
      )

    user_entities = []
    not_found_nos = []

    for user_no in user_vo.userNoList:
      user_entity = self.dao.get_user_by_no(self.session, user_no)
      if user_entity:
        user_entities.append(user_entity)
      else:
        not_found_nos.append(user_no)

    if not user_entities:
      return success_response(
        message=UserMessage.get_delete_not_found_message(is_single=False)
      )

    self.dao.delete_users(self.session, user_entities)

    message = UserMessage.get_delete_message(
      count=len(user_entities), not_found_nos=not_found_nos if not_found_nos else None
    )

    return success_response(message=message)
