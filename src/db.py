from typing import Generator

from sqlmodel import Session, SQLModel, create_engine

# 모든 모델을 import하여 SQLModel.metadata에 등록
from src.models import (  # noqa: F401
  UserInfo,
)
from src.settings import settings

engine = create_engine(settings.DATABASE_URL, echo=True)


def init_db():
  SQLModel.metadata.create_all(engine)


def get_session() -> Generator[Session, None, None]:
  with Session(engine) as session:
    yield session
