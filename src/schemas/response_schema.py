from typing import Generic, Optional, TypeVar

from pydantic import BaseModel

from src.schemas.response_code import ResponseCode

TData = TypeVar('TData')


class ApiResponse(BaseModel, Generic[TData]):
  """API 응답 표준 형식"""

  data: Optional[TData] = None
  error: bool = False
  code: ResponseCode = ResponseCode.OK
  message: str = '성공'

  class Config:
    from_attributes = True
