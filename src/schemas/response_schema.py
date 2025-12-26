from typing import Generic, Optional, TypeVar

from pydantic import BaseModel

from src.schemas.response_code import ResponseCode

TData = TypeVar('TData')


class ListResponse(BaseModel, Generic[TData]):
  """리스트 응답 데이터 형식"""

  list: list[TData]
  totalCnt: int

  class Config:
    from_attributes = True


class ApiResponse(BaseModel, Generic[TData]):
  """API 응답 표준 형식"""

  data: Optional[TData] = None
  error: bool = False
  code: ResponseCode = ResponseCode.OK
  message: str = '성공'

  class Config:
    from_attributes = True
