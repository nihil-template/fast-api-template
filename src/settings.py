from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
  # .env 파일에 있는 변수명과 똑같이 적어주면 자동으로 매핑됩니다.
  DATABASE_URL: str = ''
  ENVIRONMENT: str = 'development'  # development 또는 production

  # .env 파일을 읽도록 설정
  model_config = SettingsConfigDict(env_file='.env')


# 인스턴스 생성 (이 변수를 다른 파일에서 가져다 씁니다)
settings = Settings()
