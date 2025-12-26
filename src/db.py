from typing import Generator

from sqlmodel import Session, SQLModel, create_engine

# 모든 모델을 import하여 SQLModel.metadata에 등록
from src.models import (  # noqa: F401
  UserInfo,
)
from src.settings import settings

# 연결 풀 설정:
# - pool_pre_ping=True: 연결 사용 전에 살아있는지 확인 (stale connection 방지)
# - pool_recycle=3600: 1시간마다 연결을 재생성 (서버 타임아웃 방지)
# - pool_size=5: 기본 연결 풀 크기
# - max_overflow=10: 추가 연결 허용 수
engine = create_engine(
  settings.DATABASE_URL,
  echo=True,
  pool_pre_ping=True,  # 연결이 살아있는지 확인 후 사용
  pool_recycle=3600,  # 1시간마다 연결 재생성 (초 단위)
  pool_size=5,  # 기본 연결 풀 크기
  max_overflow=10,  # 추가 연결 허용 수
)


def init_db():
  SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
  with Session(engine) as session:
    yield session
