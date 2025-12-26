# FastAPI Template

FastAPI 기반의 RESTful API 템플릿 프로젝트입니다.

## 주요 특징

- 모든 응답이 200 OK로 통일된 API 구조
- Swagger UI에서 다양한 응답 상황을 드롭다운으로 확인 가능
- 3계층 아키텍처 (Router → Service → DAO)
- SQLModel을 사용한 타입 안전한 데이터베이스 모델
- 표준화된 응답 형식 (`ApiResponse`)

## 프로젝트 구조

```
src/
├── main.py              # FastAPI 앱 진입점
├── db.py                # 데이터베이스 연결 설정
├── settings.py          # 환경 변수 설정
├── routers/             # API 라우터
│   └── user_router.py   # 사용자 관련 엔드포인트
├── services/            # 비즈니스 로직
│   └── user_service.py
├── dao/                 # 데이터 접근 객체
│   └── user_dao.py
├── models/              # 데이터베이스 모델
│   └── user.py
├── schemas/             # Pydantic 스키마
│   ├── user_schema.py
│   ├── response_schema.py
│   └── response_code.py
└── utils/               # 유틸리티 함수
    ├── response.py
    └── swagger_examples.py  # Swagger 예시 응답 헬퍼
```

## Swagger 예시 응답 헬퍼 함수

각 테이블별로 Swagger UI에 표시될 예시 응답 데이터를 생성하는 헬퍼 함수를 만들어야 합니다.

### 사용 방법

1. **헬퍼 함수 생성**: `src/utils/swagger_examples.py`에 각 테이블별 예시 데이터 생성 함수를 추가합니다.

```python
# src/utils/swagger_examples.py

def get_user_response_example() -> dict:
  """UserResponse 예시 데이터를 반환합니다."""
  return {
    'userNo': 1,
    'emlAddr': 'user@example.com',
    'userNm': '홍길동',
    # ... 모든 필드 포함
  }

def get_user_list_example() -> list[dict]:
  """UserResponse 리스트 예시 데이터를 반환합니다."""
  return [
    get_user_response_example(),  # 첫 번째 항목
    {  # 두 번째 항목 (필요시 수정)
      'userNo': 2,
      'emlAddr': 'user2@example.com',
      # ...
    },
  ]
```

2. **Router에서 사용**: 각 엔드포인트의 `responses` 파라미터에서 헬퍼 함수를 사용합니다.

```python
# src/routers/user_router.py

from src.utils.swagger_examples import get_user_response_example, get_user_list_example

@router.get(
  '/{user_no}',
  responses={
    200: {
      'content': {
        'application/json': {
          'examples': {
            'success': {
              'summary': '사용자 조회 성공',
              'value': {
                'data': get_user_response_example(),  # 헬퍼 함수 사용
                'error': False,
                'code': 'OK',
                'message': '사용자 조회에 성공했습니다.',
              },
            },
          },
        },
      },
    },
  },
)
```

### 새 테이블 추가 시

새로운 테이블을 추가할 때는 다음 단계를 따르세요:

1. `src/utils/swagger_examples.py`에 해당 테이블의 예시 데이터 생성 함수 추가
   - 단일 항목: `get_{table_name}_response_example() -> dict`
   - 리스트: `get_{table_name}_list_example() -> list[dict]`

2. Router 파일에서 헬퍼 함수 import 및 사용

3. 예시 데이터는 실제 응답 스키마와 정확히 일치해야 합니다 (모든 필드 포함)

이렇게 하면 코드 중복을 줄이고, 예시 데이터를 한 곳에서 관리할 수 있습니다.

## 시작하기

### 환경 설정

1. 가상환경 생성 및 활성화
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

2. 의존성 설치
```bash
pip install -e .
```

3. 환경 변수 설정
`.env` 파일을 생성하고 데이터베이스 연결 정보를 설정하세요.

4. 데이터베이스 초기화
```bash
python -m src.main
```

### 서버 실행

```bash
uvicorn src.main:app --reload
```

서버가 실행되면 다음 URL에서 API 문서를 확인할 수 있습니다:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 응답 형식

모든 API 응답은 다음 형식을 따릅니다:

```json
{
  "data": {},  // 실제 데이터 (성공 시) 또는 null (에러 시)
  "error": false,  // true: 에러, false: 성공
  "code": "OK",  // 응답 코드 (OK, CREATED, NOT_FOUND, CONFLICT 등)
  "message": "성공"  // 응답 메시지
}
```

모든 응답은 HTTP 상태 코드 200으로 반환되며, 실제 성공/실패 여부는 `error` 필드와 `code` 필드로 구분합니다.
