import importlib.util
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.db import init_db
from src.schemas.response_code import ResponseCode
from src.schemas.response_schema import ApiResponse
from src.utils.response import error_response

# 점(.)이 포함된 파일명 import
router_path = Path(__file__).parent / 'routers' / 'user.router.py'
spec = importlib.util.spec_from_file_location('user_router', router_path)
if spec is None or spec.loader is None:
  raise ImportError(f'라우터 모듈을 로드할 수 없습니다: {router_path}')
user_router = importlib.util.module_from_spec(spec)
spec.loader.exec_module(user_router)


@asynccontextmanager
async def lifespan(app: FastAPI):
  init_db()
  yield


app = FastAPI(
  lifespan=lifespan,
  openapi_tags=[
    {
      'name': '사용자 관리',
      'description': '사용자 생성, 조회, 수정, 삭제 관련 API',
    },
    {
      'name': '기본',
      'description': '기본 API 엔드포인트',
    },
  ],
)

origins = [
  'http://localhost:3000',  # 프론트엔드 개발 서버 주소
  'https://your-domain.com',
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,  # 허용할 출처 목록
  allow_credentials=True,  # 쿠키 포함 여부 (True여야 쿠키 주고받기 가능)
  allow_methods=['*'],  # 허용할 HTTP 메서드 (GET, POST 등 전체 허용)
  allow_headers=['*'],  # 허용할 헤더 (전체 허용)
)


# 422 Validation Error를 200 응답으로 변환하는 커스텀 핸들러
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
  request: Request, exc: RequestValidationError
) -> JSONResponse:
  """422 Validation Error를 200 응답으로 변환"""
  errors = exc.errors()
  error_messages = []
  for error in errors:
    field = ' -> '.join(str(loc) for loc in error['loc'])
    error_messages.append(f'{field}: {error["msg"]}')

  error_detail = '; '.join(error_messages)
  response_data: ApiResponse[None] = error_response(
    message=f'입력값 검증 실패: {error_detail}',
    code=ResponseCode.VALIDATION_ERROR,
  )

  return JSONResponse(
    status_code=status.HTTP_200_OK,
    content=response_data.model_dump(),
  )


# 라우터 등록
app.include_router(user_router.router)


@app.get(
  '/',
  summary='헬로우 월드',
  operation_id='get_hello',
  tags=['기본'],
)
def getHello():
  """기본 헬로우 월드 엔드포인트"""
  return 'Hello, World!'
