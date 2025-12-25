from typing import List

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from src.db import get_session
from src.schemas.response_code import ResponseCode
from src.schemas.response_schema import ApiResponse
from src.schemas.user_schema import UserCreate, UserResponse, UserUpdate
from src.services.user_service import UserService
from src.utils.response import error_response, success_response

router = APIRouter(prefix='/api/users')


def get_user_service(session: Session = Depends(get_session)) -> UserService:
  """UserService 의존성 주입"""
  return UserService(session)


@router.post(
  '/',
  response_model=ApiResponse[UserResponse],
  status_code=status.HTTP_200_OK,
  summary='사용자 생성',
  operation_id='create_user',
  tags=['사용자 관리'],
)
def create_user(
  user_data: UserCreate,
  service: UserService = Depends(get_user_service),
):
  """새로운 사용자를 생성합니다."""
  try:
    user = service.create_user(user_data)
    return success_response(
      data=user,
      message='사용자가 성공적으로 생성되었습니다.',
      code=ResponseCode.CREATED,
    )
  except ValueError as e:
    return error_response(message=str(e), code=ResponseCode.VALIDATION_ERROR)


@router.get(
  '/{user_no}',
  response_model=ApiResponse[UserResponse],
  status_code=status.HTTP_200_OK,
  summary='사용자 조회',
  operation_id='get_user_by_no',
  tags=['사용자 관리'],
)
def get_user(
  user_no: int,
  service: UserService = Depends(get_user_service),
):
  """사용자 번호로 사용자 정보를 조회합니다."""
  user = service.get_user_by_id(user_no)
  if not user:
    return error_response(
      message='사용자를 찾을 수 없습니다.', code=ResponseCode.NOT_FOUND
    )
  return success_response(data=user, message='사용자 조회에 성공했습니다.')


@router.get(
  '/',
  response_model=ApiResponse[List[UserResponse]],
  status_code=status.HTTP_200_OK,
  summary='사용자 목록 조회',
  operation_id='get_all_users',
  tags=['사용자 관리'],
)
def get_all_users(
  skip: int = 0,
  limit: int = 100,
  service: UserService = Depends(get_user_service),
):
  """모든 사용자 목록을 페이지네이션으로 조회합니다."""
  users = service.get_all_users(skip=skip, limit=limit)
  return success_response(data=users, message='사용자 목록 조회에 성공했습니다.')


@router.put(
  '/{user_no}',
  response_model=ApiResponse[UserResponse],
  status_code=status.HTTP_200_OK,
  summary='사용자 정보 수정',
  operation_id='update_user',
  tags=['사용자 관리'],
)
def update_user(
  user_no: int,
  update_data: UserUpdate,
  service: UserService = Depends(get_user_service),
):
  """사용자 정보를 수정합니다. (PATCH 방식 - 전달된 필드만 업데이트)"""
  try:
    user = service.update_user(user_no, update_data)
    if not user:
      return error_response(
        message='사용자를 찾을 수 없습니다.', code=ResponseCode.NOT_FOUND
      )
    return success_response(
      data=user, message='사용자 정보가 성공적으로 업데이트되었습니다.'
    )
  except ValueError as e:
    return error_response(message=str(e), code=ResponseCode.VALIDATION_ERROR)


@router.delete(
  '/{user_no}',
  response_model=ApiResponse[None],
  status_code=status.HTTP_200_OK,
  summary='사용자 삭제',
  operation_id='delete_user',
  tags=['사용자 관리'],
)
def delete_user(
  user_no: int,
  service: UserService = Depends(get_user_service),
):
  """사용자를 삭제합니다. (소프트 삭제)"""
  success = service.delete_user(user_no)
  if not success:
    return error_response(
      message='사용자를 찾을 수 없습니다.', code=ResponseCode.NOT_FOUND
    )
  return success_response(message='사용자가 성공적으로 삭제되었습니다.')
