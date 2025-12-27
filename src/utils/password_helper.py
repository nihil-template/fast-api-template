"""비밀번호 해시화 및 검증 유틸리티"""

from passlib.context import CryptContext  # type: ignore[import-untyped]

# CryptContext 초기화 (sha256_crypt를 기본 알고리즘으로 사용)
# sha256_crypt는 기본적으로 80000 rounds를 사용하며, 비밀번호 길이 제한이 없습니다.
pwd_context = CryptContext(
  schemes=['sha256_crypt'],
  deprecated='auto',
  sha256_crypt__default_rounds=80000,
)


def hash_password(plain_password: str) -> str:
  """평문 비밀번호를 해시화합니다.

  Args:
    plain_password: 해시화할 평문 비밀번호

  Returns:
    해시화된 비밀번호 문자열
  """
  return pwd_context.hash(plain_password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
  """평문 비밀번호와 해시화된 비밀번호를 비교합니다.

  Args:
    plain_password: 검증할 평문 비밀번호
    hashed_password: 비교할 해시화된 비밀번호

  Returns:
    비밀번호가 일치하면 True, 그렇지 않으면 False
  """
  return pwd_context.verify(plain_password, hashed_password)
