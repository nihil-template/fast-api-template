from typing import Optional, TypeVar

from src.schemas.response_code import ResponseCode
from src.schemas.response_schema import ApiResponse

TData = TypeVar('TData')


def success_response(
  data: Optional[TData] = None,
  message: str = '성공',
  code: ResponseCode = ResponseCode.OK,
) -> ApiResponse[TData]:
  """성공 응답 생성"""
  return ApiResponse(data=data, error=False, code=code, message=message)


def error_response(
  message: str = '실패',
  code: ResponseCode = ResponseCode.INTERNAL_SERVER_ERROR,
  data: Optional[TData] = None,
) -> ApiResponse[TData]:
  """에러 응답 생성"""
  return ApiResponse(data=data, error=True, code=code, message=message)
