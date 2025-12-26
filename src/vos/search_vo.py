"""검색/페이지네이션용 공통 VO (Value Object) 정의

모든 리소스에서 공통으로 사용하는 검색 및 페이지네이션 필드를 정의합니다.
"""

from typing import Optional

from pydantic import BaseModel


class SearchVo(BaseModel):
  """검색/페이지네이션용 VO

  모든 리소스에서 공통으로 사용하는 검색 및 페이지네이션 필드를 정의합니다.
  """

  page: Optional[int] = None  # 페이지 번호
  pageSz: Optional[int] = 10  # 페이지 사이즈 (기본값 10)
  strtRow: Optional[int] = None  # 시작 행
  endRow: Optional[int] = None  # 종료 행
  srchType: Optional[str] = None  # 검색 타입
  srchKywd: Optional[str] = None  # 검색 키워드

  class Config:
    from_attributes = True
