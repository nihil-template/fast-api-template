"""JWT 토큰 생성 및 검증 유틸리티"""

from datetime import datetime, timedelta, timezone
from typing import Optional

from jose import JWTError, jwt  # type: ignore[import-untyped]

from src.settings import settings


def parse_expiration(exp_str: str) -> timedelta:
  """만료 시간 문자열을 timedelta로 변환합니다.

  Args:
    exp_str: 만료 시간 문자열 (예: '15m', '1h', '7d', '30d')

  Returns:
    timedelta 객체

  Raises:
    ValueError: 잘못된 형식의 문자열인 경우
  """
  if not exp_str:
    raise ValueError('만료 시간이 비어있습니다.')

  exp_str = exp_str.lower().strip()

  if exp_str.endswith('m'):
    minutes = int(exp_str[:-1])
    return timedelta(minutes=minutes)
  elif exp_str.endswith('h'):
    hours = int(exp_str[:-1])
    return timedelta(hours=hours)
  elif exp_str.endswith('d'):
    days = int(exp_str[:-1])
    return timedelta(days=days)
  else:
    raise ValueError(f'지원하지 않는 만료 시간 형식: {exp_str}')


def create_access_token(data: dict) -> str:
  """Access Token을 생성합니다.

  Args:
    data: 토큰에 포함할 데이터 (예: {'sub': user_id})

  Returns:
    생성된 JWT 토큰 문자열
  """
  to_encode = data.copy()
  expire = datetime.now(timezone.utc) + parse_expiration(settings.ACCESS_EXP)
  to_encode.update({'exp': expire, 'type': 'access'})
  encoded_jwt = jwt.encode(to_encode, settings.ACCESS_TOKEN_SECRET, algorithm='HS256')
  return encoded_jwt


def create_refresh_token(data: dict) -> str:
  """Refresh Token을 생성합니다.

  Args:
    data: 토큰에 포함할 데이터 (예: {'sub': user_id})

  Returns:
    생성된 JWT 토큰 문자열
  """
  to_encode = data.copy()
  expire = datetime.now(timezone.utc) + parse_expiration(settings.REFRESH_EXP)
  to_encode.update({'exp': expire, 'type': 'refresh'})
  encoded_jwt = jwt.encode(to_encode, settings.REFRESH_TOKEN_SECRET, algorithm='HS256')
  return encoded_jwt


def verify_access_token(token: str) -> Optional[dict]:
  """Access Token을 검증하고 디코딩합니다.

  Args:
    token: 검증할 JWT 토큰

  Returns:
    디코딩된 토큰 데이터 또는 None (검증 실패 시)
  """
  try:
    payload = jwt.decode(token, settings.ACCESS_TOKEN_SECRET, algorithms=['HS256'])
    if payload.get('type') != 'access':
      return None
    return payload
  except JWTError:
    return None


def verify_refresh_token(token: str) -> Optional[dict]:
  """Refresh Token을 검증하고 디코딩합니다.

  Args:
    token: 검증할 JWT 토큰

  Returns:
    디코딩된 토큰 데이터 또는 None (검증 실패 시)
  """
  try:
    payload = jwt.decode(token, settings.REFRESH_TOKEN_SECRET, algorithms=['HS256'])
    if payload.get('type') != 'refresh':
      return None
    return payload
  except JWTError:
    return None
