"""Swagger UI 예시 응답 헬퍼 함수들

각 테이블별로 예시 응답 데이터를 생성하는 헬퍼 함수를 정의합니다.
이 함수들은 Swagger UI의 responses 예시를 생성하는 데 사용됩니다.
"""


def get_user_response_example() -> dict:
  """UserResponse 예시 데이터를 반환합니다."""
  return {
    'userNo': 1,
    'emlAddr': 'user@example.com',
    'userNm': '홍길동',
    'userRole': 'USER',
    'proflImg': None,
    'userBiogp': None,
    'encptPswd': None,
    'reshToken': None,
    'useYn': 'Y',
    'delYn': 'N',
    'lastLgnDt': None,
    'lastPswdChgDt': None,
    'crtNo': None,
    'crtDt': '2024-01-01T00:00:00Z',
    'updtNo': None,
    'updtDt': '2024-01-01T00:00:00Z',
    'delNo': None,
    'delDt': None,
  }


def get_user_list_example() -> list[dict]:
  """UserResponse 리스트 예시 데이터를 반환합니다."""
  return [
    {
      'userNo': 1,
      'emlAddr': 'user1@example.com',
      'userNm': '홍길동',
      'userRole': 'USER',
      'proflImg': None,
      'userBiogp': None,
      'encptPswd': None,
      'reshToken': None,
      'useYn': 'Y',
      'delYn': 'N',
      'lastLgnDt': None,
      'lastPswdChgDt': None,
      'crtNo': None,
      'crtDt': '2024-01-01T00:00:00Z',
      'updtNo': None,
      'updtDt': '2024-01-01T00:00:00Z',
      'delNo': None,
      'delDt': None,
    },
    {
      'userNo': 2,
      'emlAddr': 'user2@example.com',
      'userNm': '김철수',
      'userRole': 'USER',
      'proflImg': None,
      'userBiogp': None,
      'encptPswd': None,
      'reshToken': None,
      'useYn': 'Y',
      'delYn': 'N',
      'lastLgnDt': None,
      'lastPswdChgDt': None,
      'crtNo': None,
      'crtDt': '2024-01-01T00:00:00Z',
      'updtNo': None,
      'updtDt': '2024-01-01T00:00:00Z',
      'delNo': None,
      'delDt': None,
    },
  ]
