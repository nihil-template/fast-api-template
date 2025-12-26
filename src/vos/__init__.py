"""VO (Value Object) 모듈

자원별로 하나의 VO만 사용하여 모든 작업(get, post, update, delete)을 처리합니다.
"""

from src.vos.search_vo import SearchVo
from src.vos.user_vo import UserVo

__all__ = [
  'SearchVo',
  'UserVo',
]
