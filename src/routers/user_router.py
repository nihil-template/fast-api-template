from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from src.db import get_session
from src.messages.user_message import UserMessage
from src.schemas.response_code import ResponseCode
from src.schemas.response_schema import ApiResponse, ListResponse
from src.services.user_service import UserService
from src.utils.swagger_examples import get_user_list_example, get_user_response_example
from src.vos.user_vo import UserVo

router = APIRouter(prefix='/users')


def get_user_service(session: Session = Depends(get_session)) -> UserService:
  """UserService 의존성 주입"""
  return UserService(session)


@router.post(
  '/',
  response_model=ApiResponse[UserVo],
  status_code=status.HTTP_200_OK,
  summary='사용자 생성',
  operation_id='createUser',
  tags=['사용자 관리'],
  responses={
    200: {
      'description': '성공 응답',
      'content': {
        'application/json': {
          'examples': {
            'success': {
              'summary': '사용자 생성 성공',
              'value': {
                'data': get_user_response_example(),
                'error': False,
                'code': ResponseCode.CREATED,
                'message': UserMessage.CREATE_SUCCESS,
              },
            },
            'conflict_email': {
              'summary': '이메일 중복',
              'value': {
                'data': None,
                'error': True,
                'code': ResponseCode.CONFLICT,
                'message': UserMessage.EMAIL_CONFLICT,
              },
            },
            'conflict_username': {
              'summary': '사용자명 중복',
              'value': {
                'data': None,
                'error': True,
                'code': ResponseCode.CONFLICT,
                'message': UserMessage.USERNAME_CONFLICT,
              },
            },
            'validation_error': {
              'summary': '입력값 검증 실패',
              'value': {
                'data': None,
                'error': True,
                'code': ResponseCode.VALIDATION_ERROR,
                'message': '입력값이 유효하지 않습니다.',
              },
            },
          },
        },
      },
    },
  },
)
def createUser(
  user_vo: UserVo,
  service: UserService = Depends(get_user_service),
):
  """새로운 사용자를 생성합니다."""
  print('[ROUTER] user_vo:', user_vo.model_dump())
  return service.createUser(user_vo)


@router.get(
  '/email/{eml_addr}',
  response_model=ApiResponse[UserVo],
  status_code=status.HTTP_200_OK,
  summary='이메일로 사용자 조회',
  operation_id='getUserByEmail',
  tags=['사용자 관리'],
  responses={
    200: {
      'description': '성공 응답',
      'content': {
        'application/json': {
          'examples': {
            'success': {
              'summary': '사용자 조회 성공',
              'value': {
                'data': get_user_response_example(),
                'error': False,
                'code': ResponseCode.OK,
                'message': UserMessage.GET_SUCCESS,
              },
            },
            'not_found': {
              'summary': '사용자를 찾을 수 없음',
              'value': {
                'data': None,
                'error': True,
                'code': ResponseCode.NOT_FOUND,
                'message': UserMessage.NOT_FOUND,
              },
            },
          },
        },
      },
    },
  },
)
def getUserByEmail(
  eml_addr: str,
  service: UserService = Depends(get_user_service),
):
  """이메일로 사용자 정보를 조회합니다."""
  user_vo = UserVo(emlAddr=eml_addr)
  return service.getUserByEmail(user_vo)


@router.get(
  '/{user_no}',
  response_model=ApiResponse[UserVo],
  status_code=status.HTTP_200_OK,
  summary='사용자 조회',
  operation_id='getUserByNo',
  tags=['사용자 관리'],
  responses={
    200: {
      'description': '성공 응답',
      'content': {
        'application/json': {
          'examples': {
            'success': {
              'summary': '사용자 조회 성공',
              'value': {
                'data': get_user_response_example(),
                'error': False,
                'code': ResponseCode.OK,
                'message': UserMessage.GET_SUCCESS,
              },
            },
            'not_found': {
              'summary': '사용자를 찾을 수 없음',
              'value': {
                'data': None,
                'error': True,
                'code': ResponseCode.NOT_FOUND,
                'message': UserMessage.NOT_FOUND,
              },
            },
          },
        },
      },
    },
  },
)
def getUserByNo(
  user_no: int,
  service: UserService = Depends(get_user_service),
):
  """사용자 번호로 사용자 정보를 조회합니다."""
  user_vo = UserVo(userNo=user_no)
  return service.getUserByNo(user_vo)


@router.get(
  '/',
  response_model=ApiResponse[ListResponse[UserVo]],
  status_code=status.HTTP_200_OK,
  summary='사용자 목록 조회',
  operation_id='getUserList',
  tags=['사용자 관리'],
  responses={
    200: {
      'description': '성공 응답',
      'content': {
        'application/json': {
          'examples': {
            'success': {
              'summary': '사용자 목록 조회 성공',
              'value': {
                'data': {
                  'list': get_user_list_example(),
                  'totalCnt': 3,
                },
                'error': False,
                'code': ResponseCode.OK,
                'message': UserMessage.GET_LIST_SUCCESS,
              },
            },
            'empty': {
              'summary': '빈 목록',
              'value': {
                'data': {
                  'list': [],
                  'totalCnt': 0,
                },
                'error': False,
                'code': ResponseCode.OK,
                'message': UserMessage.GET_LIST_SUCCESS,
              },
            },
          },
        },
      },
    },
  },
)
def getUserList(
  user_vo: UserVo = Depends(),
  service: UserService = Depends(get_user_service),
):
  """사용자 목록을 페이지네이션으로 조회합니다. (Query 파라미터를 UserVo로 자동 변환)"""
  return service.getUserList(user_vo)


@router.patch(
  '/{user_no}/password',
  response_model=ApiResponse[UserVo],
  status_code=status.HTTP_200_OK,
  summary='사용자 비밀번호 수정',
  operation_id='updateUserPassword',
  tags=['사용자 관리'],
  responses={
    200: {
      'description': '성공 응답',
      'content': {
        'application/json': {
          'examples': {
            'success': {
              'summary': '비밀번호 수정 성공',
              'value': {
                'data': get_user_response_example(),
                'error': False,
                'code': ResponseCode.OK,
                'message': UserMessage.UPDATE_SUCCESS,
              },
            },
            'not_found': {
              'summary': '사용자를 찾을 수 없음',
              'value': {
                'data': None,
                'error': True,
                'code': ResponseCode.NOT_FOUND,
                'message': UserMessage.NOT_FOUND,
              },
            },
            'validation_error': {
              'summary': '입력값 검증 실패',
              'value': {
                'data': None,
                'error': True,
                'code': ResponseCode.VALIDATION_ERROR,
                'message': '입력값이 유효하지 않습니다.',
              },
            },
          },
        },
      },
    },
  },
)
def updateUserPassword(
  user_no: int,
  user_vo: UserVo,
  service: UserService = Depends(get_user_service),
):
  """사용자 비밀번호를 수정합니다."""
  user_vo.userNo = user_no
  return service.updateUserPassword(user_vo)


@router.patch(
  '/{user_no}',
  response_model=ApiResponse[UserVo],
  status_code=status.HTTP_200_OK,
  summary='사용자 정보 수정',
  operation_id='updateUser',
  tags=['사용자 관리'],
  responses={
    200: {
      'description': '성공 응답',
      'content': {
        'application/json': {
          'examples': {
            'success': {
              'summary': '사용자 정보 수정 성공',
              'value': {
                'data': get_user_response_example(),
                'error': False,
                'code': ResponseCode.OK,
                'message': UserMessage.UPDATE_SUCCESS,
              },
            },
            'not_found': {
              'summary': '사용자를 찾을 수 없음',
              'value': {
                'data': None,
                'error': True,
                'code': ResponseCode.NOT_FOUND,
                'message': UserMessage.NOT_FOUND,
              },
            },
            'conflict': {
              'summary': '사용자명 중복',
              'value': {
                'data': None,
                'error': True,
                'code': ResponseCode.CONFLICT,
                'message': UserMessage.UPDATE_USERNAME_CONFLICT,
              },
            },
            'validation_error': {
              'summary': '입력값 검증 실패',
              'value': {
                'data': None,
                'error': True,
                'code': ResponseCode.VALIDATION_ERROR,
                'message': '입력값이 유효하지 않습니다.',
              },
            },
          },
        },
      },
    },
  },
)
def updateUser(
  user_no: int,
  user_vo: UserVo,
  service: UserService = Depends(get_user_service),
):
  """사용자 정보를 수정합니다. (PATCH 방식 - 전달된 필드만 업데이트, 비밀번호 제외)"""
  user_vo.userNo = user_no
  return service.updateUser(user_vo)


@router.delete(
  '/{user_no}',
  response_model=ApiResponse[None],
  status_code=status.HTTP_200_OK,
  summary='사용자 단건 삭제',
  operation_id='deleteUser',
  tags=['사용자 관리'],
  responses={
    200: {
      'description': '성공 응답',
      'content': {
        'application/json': {
          'examples': {
            'success': {
              'summary': '단건 삭제 성공',
              'value': {
                'data': None,
                'error': False,
                'code': ResponseCode.OK,
                'message': UserMessage.DELETE_SUCCESS_SINGLE,
              },
            },
            'not_found': {
              'summary': '사용자를 찾을 수 없음',
              'value': {
                'data': None,
                'error': True,
                'code': ResponseCode.NOT_FOUND,
                'message': UserMessage.DELETE_NOT_FOUND,
              },
            },
            'validation_error': {
              'summary': '입력값 검증 실패',
              'value': {
                'data': None,
                'error': True,
                'code': ResponseCode.VALIDATION_ERROR,
                'message': UserMessage.INVALID_REQUEST,
              },
            },
          },
        },
      },
    },
  },
)
def deleteUser(
  user_no: int,
  service: UserService = Depends(get_user_service),
):
  """사용자를 단건 삭제합니다. (소프트 삭제)"""
  user_vo = UserVo(userNo=user_no)
  return service.deleteUser(user_vo)


@router.delete(
  '/',
  response_model=ApiResponse[None],
  status_code=status.HTTP_200_OK,
  summary='사용자 다건 삭제',
  operation_id='deleteUsers',
  tags=['사용자 관리'],
  responses={
    200: {
      'description': '성공 응답',
      'content': {
        'application/json': {
          'examples': {
            'success': {
              'summary': '다건 삭제 성공',
              'value': {
                'data': None,
                'error': False,
                'code': ResponseCode.OK,
                'message': UserMessage.DELETE_SUCCESS_MULTIPLE.format(count=3),
              },
            },
            'not_found': {
              'summary': '사용자를 찾을 수 없음',
              'value': {
                'data': None,
                'error': True,
                'code': ResponseCode.NOT_FOUND,
                'message': UserMessage.DELETE_NOT_FOUND,
              },
            },
            'validation_error': {
              'summary': '입력값 검증 실패',
              'value': {
                'data': None,
                'error': True,
                'code': ResponseCode.VALIDATION_ERROR,
                'message': UserMessage.INVALID_REQUEST,
              },
            },
          },
        },
      },
    },
  },
)
def deleteUsers(
  user_vo: UserVo,
  service: UserService = Depends(get_user_service),
):
  """사용자를 다건 삭제합니다. (소프트 삭제)

  - 요청 예시: `{"userNoList": [1, 2, 3]}` 형태로 요청
  """
  return service.deleteUsers(user_vo)
