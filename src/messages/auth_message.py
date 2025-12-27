"""인증 관련 메시지 상수"""


class AuthMessage:
  """인증 관련 메시지"""

  # 로그인
  LOGIN_SUCCESS = '로그인에 성공했습니다.'
  LOGIN_FAILED = '이메일 또는 비밀번호가 올바르지 않습니다.'
  ALREADY_LOGGED_IN = '이미 로그인되어 있습니다. 로그아웃 후 다시 시도해주세요.'
  USER_NOT_FOUND = '사용자를 찾을 수 없습니다.'
  USER_DISABLED = '비활성화된 사용자입니다.'

  # 로그아웃
  LOGOUT_SUCCESS = '로그아웃에 성공했습니다.'

  # 비밀번호 재설정
  RESET_PASSWORD_REQUEST_SUCCESS = '비밀번호 재설정 이메일을 발송했습니다.'
  RESET_PASSWORD_SUCCESS = '비밀번호가 성공적으로 재설정되었습니다.'
  RESET_TOKEN_INVALID = '비밀번호 재설정 토큰이 유효하지 않거나 만료되었습니다.'
  RESET_TOKEN_NOT_FOUND = '비밀번호 재설정 토큰을 찾을 수 없습니다.'

  # 비밀번호 변경
  CHANGE_PASSWORD_SUCCESS = '비밀번호가 성공적으로 변경되었습니다.'
  CURRENT_PASSWORD_INCORRECT = '현재 비밀번호가 올바르지 않습니다.'
  NEW_PASSWORD_SAME = '새 비밀번호는 현재 비밀번호와 달라야 합니다.'

  # 토큰
  TOKEN_INVALID = '토큰이 유효하지 않습니다.'
  TOKEN_EXPIRED = '토큰이 만료되었습니다.'
  REFRESH_TOKEN_INVALID = 'Refresh Token이 유효하지 않습니다.'
