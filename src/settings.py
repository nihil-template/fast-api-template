from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
  # .env 파일에 있는 변수명과 똑같이 적어주면 자동으로 매핑됩니다.
  DATABASE_URL: str = ''
  ENVIRONMENT: str = 'development'  # development 또는 production

  # JWT 관련 환경변수
  ACCESS_TOKEN_SECRET: str = ''
  REFRESH_TOKEN_SECRET: str = ''
  ACCESS_EXP: str = '15m'  # 기본값 15분
  REFRESH_EXP: str = '7d'  # 기본값 7일

  # SMTP 이메일 발송 설정
  SMTP_HOST: str = ''  # SMTP 서버 주소 (예: smtp.gmail.com)
  SMTP_PORT: int = 587  # SMTP 포트 (기본값: 587)
  SMTP_USER: str = ''  # SMTP 사용자명 (이메일 주소)
  SMTP_PASSWORD: str = ''  # SMTP 비밀번호
  SMTP_FROM_EMAIL: str = ''  # 발신자 이메일 주소 (기본값: SMTP_USER 사용)
  SMTP_USE_TLS: bool = True  # TLS 사용 여부 (기본값: True)

  # 프론트엔드 URL (환경별 설정)
  FRONTEND_URL_DEV: str = 'http://localhost:3000'  # 개발 환경 프론트엔드 URL
  FRONTEND_URL_PROD: str = ''  # 운영 환경 프론트엔드 URL

  @computed_field
  def FRONTEND_URL(self) -> str:
    """환경에 따라 적절한 프론트엔드 URL 반환"""
    if self.ENVIRONMENT == 'production':
      return self.FRONTEND_URL_PROD or 'http://localhost:3000'
    return self.FRONTEND_URL_DEV

  # .env 파일을 읽도록 설정
  model_config = SettingsConfigDict(env_file='.env')


# 인스턴스 생성 (이 변수를 다른 파일에서 가져다 씁니다)
settings = Settings()
