# FastAPI Template

FastAPI 기반의 RESTful API 템플릿 프로젝트입니다.

## 주요 특징

- 모든 응답이 200 OK로 통일된 API 구조
- Swagger UI에서 다양한 응답 상황을 드롭다운으로 확인 가능
- 3계층 아키텍처 (Router → Service → DAO)
- SQLModel을 사용한 타입 안전한 데이터베이스 모델
- 표준화된 응답 형식 (`ApiResponse`)
- JWT 기반 인증 시스템 (Access Token + Refresh Token)
- VO(Value Object) 패턴을 통한 일관된 데이터 전달
- 메시지 관리 클래스를 통한 응답 메시지 표준화
- CORS 설정 지원
- 환경별 설정 분리 (development/production)

## 프로젝트 구조

```
src/
├── main.py                    # FastAPI 앱 진입점
├── db.py                      # 데이터베이스 연결 설정
├── settings.py                # 환경 변수 설정
├── routers/                   # API 라우터
│   ├── auth_router.py         # 인증 관련 엔드포인트 (로그인, 로그아웃, 비밀번호 재설정/변경)
│   └── user_router.py         # 사용자 관련 엔드포인트 (CRUD)
├── services/                  # 비즈니스 로직
│   ├── auth_service.py        # 인증 비즈니스 로직
│   └── user_service.py        # 사용자 비즈니스 로직
├── dao/                       # 데이터 접근 객체
│   └── user_dao.py            # 사용자 데이터 접근 로직
├── models/                    # 데이터베이스 모델 (SQLModel)
│   └── user.py                # 사용자 모델
├── schemas/                   # Pydantic 스키마
│   ├── auth_schema.py         # 인증 관련 스키마
│   ├── user_schema.py         # 사용자 관련 스키마
│   ├── response_schema.py     # 표준 응답 스키마
│   └── response_code.py       # 응답 코드 Enum
├── messages/                  # 응답 메시지 관리
│   ├── auth_message.py        # 인증 관련 메시지
│   └── user_message.py        # 사용자 관련 메시지
├── vos/                       # Value Object (데이터 전달 객체)
│   ├── search_vo.py           # 검색/페이지네이션 공통 VO
│   └── user_vo.py             # 사용자 VO (모든 작업에서 사용)
└── utils/                     # 유틸리티 함수 (모두 _helper.py 네이밍 규칙 적용)
    ├── auth_helper.py         # 인증 유틸리티 (토큰 검증, 사용자 추출)
    ├── jwt_helper.py          # JWT 토큰 생성/검증
    ├── password_helper.py     # 비밀번호 해싱/검증
    ├── response_helper.py     # 응답 생성 헬퍼
    └── swagger_helper.py      # Swagger 예시 응답 헬퍼
```

## 아키텍처 설명

### 3계층 아키텍처

1. **Router Layer** (`routers/`)
   - HTTP 요청/응답 처리
   - 요청 검증 및 응답 형식 변환
   - Swagger 문서화 설정

2. **Service Layer** (`services/`)
   - 비즈니스 로직 처리
   - 트랜잭션 관리
   - DAO 호출 및 결과 가공

3. **DAO Layer** (`dao/`)
   - 데이터베이스 접근 로직
   - SQL 쿼리 실행
   - 모델 ↔ VO 변환

### VO(Value Object) 패턴

각 리소스별로 하나의 VO를 사용하여 모든 작업(get, post, update, delete)을 처리합니다.

- `SearchVo`: 검색/페이지네이션 공통 필드 (모든 VO의 부모 클래스)
- `UserVo`: 사용자 관련 모든 필드 포함 (검색, 생성, 수정, 삭제 모두에서 사용)

### 메시지 관리

응답 메시지는 `messages/` 폴더의 클래스에서 관리합니다.

- `AuthMessage`: 인증 관련 메시지
- `UserMessage`: 사용자 관련 메시지

이를 통해 메시지 중복을 줄이고 일관성을 유지합니다.

### 인증 시스템

JWT 기반 인증을 사용합니다.

- **Access Token**: 짧은 만료 시간 (기본 15분)
- **Refresh Token**: 긴 만료 시간 (기본 7일)
- 토큰은 HTTP 헤더의 `Authorization: Bearer <token>` 형식으로 전달
- `utils/auth_helper.py`의 `get_current_user_id` 의존성으로 현재 사용자 추출

## Swagger 예시 응답 헬퍼 함수

각 테이블별로 Swagger UI에 표시될 예시 응답 데이터를 생성하는 헬퍼 함수를 `src/utils/swagger_examples.py`에서 관리합니다.

### 사용 방법

1. **헬퍼 함수 생성**: `src/utils/swagger_helper.py`에 각 테이블별 예시 데이터 생성 함수를 추가합니다.

```python
# src/utils/swagger_helper.py

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

from src.utils.swagger_helper import get_user_response_example, get_user_list_example

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

1. `src/utils/swagger_helper.py`에 해당 테이블의 예시 데이터 생성 함수 추가
   - 단일 항목: `get_{table_name}_response_example() -> dict`
   - 리스트: `get_{table_name}_list_example() -> list[dict]`

2. Router 파일에서 헬퍼 함수 import 및 사용

3. 예시 데이터는 실제 응답 스키마와 정확히 일치해야 합니다 (모든 필드 포함)

이렇게 하면 코드 중복을 줄이고, 예시 데이터를 한 곳에서 관리할 수 있습니다.

## 시작하기

### 사전 요구사항

- [uv](https://github.com/astral-sh/uv) 설치 (Python 패키지 관리자)
  ```bash
  # Windows (PowerShell)
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  
  # macOS / Linux
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

### 환경 설정

1. 의존성 설치 및 가상환경 동기화
```bash
uv sync
```
uv는 자동으로 가상환경을 생성하고 `pyproject.toml`의 의존성을 설치합니다. 가상환경은 `.venv` 폴더에 생성됩니다.

2. 환경 변수 설정
`.env` 파일을 생성하고 다음 변수들을 설정하세요:

```env
# 데이터베이스
DATABASE_URL=postgresql://user:password@localhost:5432/dbname

# 환경 설정
ENVIRONMENT=development  # 또는 production

# JWT 설정
ACCESS_TOKEN_SECRET=your-access-token-secret-key
REFRESH_TOKEN_SECRET=your-refresh-token-secret-key
ACCESS_EXP=15m  # Access Token 만료 시간 (기본값: 15분)
REFRESH_EXP=7d   # Refresh Token 만료 시간 (기본값: 7일)
```

3. 데이터베이스 초기화
```bash
uv run python -m src.main
```

### 서버 실행

```bash
uv run uvicorn src.main:app --reload
```

또는 uv를 통해 직접 실행:
```bash
uv run --with uvicorn[standard] uvicorn src.main:app --reload
```

### 유용한 uv 명령어

- `uv sync`: 의존성 설치 및 가상환경 동기화
- `uv add <package>`: 패키지 추가 (예: `uv add fastapi`)
- `uv remove <package>`: 패키지 제거
- `uv run <command>`: 가상환경에서 명령 실행
- `uv lock`: `uv.lock` 파일 업데이트

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

### 응답 코드 종류

`ResponseCode` Enum에 정의된 코드들:

- **성공 (2xx)**: `OK`, `CREATED`, `ACCEPTED`, `NO_CONTENT`
- **클라이언트 에러 (4xx)**: `BAD_REQUEST`, `UNAUTHORIZED`, `FORBIDDEN`, `NOT_FOUND`, `METHOD_NOT_ALLOWED`, `CONFLICT`, `VALIDATION_ERROR`, `UNPROCESSABLE_ENTITY`
- **서버 에러 (5xx)**: `INTERNAL_SERVER_ERROR`, `BAD_GATEWAY`, `SERVICE_UNAVAILABLE`

### 리스트 응답 형식

리스트 조회 시에는 다음 형식을 사용합니다:

```json
{
  "data": {
    "list": [...],  // 데이터 리스트
    "totalCnt": 10  // 전체 개수
  },
  "error": false,
  "code": "OK",
  "message": "조회에 성공했습니다."
}
```

## API 엔드포인트

### 인증 API (`/auth`)

- `POST /auth/login` - 로그인
- `POST /auth/logout` - 로그아웃
- `POST /auth/reset-password/request` - 비밀번호 재설정 요청
- `POST /auth/reset-password` - 비밀번호 재설정
- `POST /auth/change-password` - 비밀번호 변경 (로그인 필요)

### 사용자 관리 API (`/users`)

- `POST /users` - 사용자 생성
- `GET /users` - 사용자 목록 조회 (페이지네이션)
- `GET /users/{user_no}` - 사용자 조회 (번호)
- `GET /users/email/{eml_addr}` - 사용자 조회 (이메일)
- `PATCH /users/{user_no}` - 사용자 정보 수정
- `PATCH /users/{user_no}/password` - 사용자 비밀번호 수정
- `DELETE /users/{user_no}` - 사용자 단건 삭제
- `DELETE /users` - 사용자 다건 삭제

## 기술 스택

- **FastAPI**: 웹 프레임워크
- **SQLModel**: ORM 및 타입 안전성
- **PostgreSQL**: 데이터베이스 (psycopg)
- **Pydantic**: 데이터 검증 및 설정 관리
- **python-jose**: JWT 토큰 처리
- **passlib**: 비밀번호 해싱 (bcrypt)
