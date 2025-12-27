from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse

from src.db import init_db
from src.routers.auth_router import router as auth_router
from src.routers.user_router import router as user_router
from src.schemas.response_schema import ApiResponse
from src.utils.response_helper import success_response


@asynccontextmanager
async def lifespan(app: FastAPI):
  init_db()
  yield


app = FastAPI(
  lifespan=lifespan,
  openapi_tags=[
    {
      'name': '인증',
      'description': '로그인, 로그아웃, 비밀번호 재설정/변경 관련 API',
    },
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
  return JSONResponse(
    status_code=status.HTTP_200_OK,  # [핵심] 상태 코드를 200으로 강제
    content={
      'data': None,
      'error': True,
      'code': 'VALIDATION_ERROR',
      'message': '입력값이 유효하지 않습니다.',
    },
  )


# 401 Unauthorized Error를 200 응답으로 변환하는 커스텀 핸들러
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
  """HTTPException을 200 응답으로 변환 (401 에러 포함)"""
  # detail이 dict 형태인 경우 그대로 사용, 아니면 변환
  if isinstance(exc.detail, dict):
    content = exc.detail
  else:
    content = {
      'data': None,
      'error': True,
      'code': 'UNAUTHORIZED' if exc.status_code == 401 else 'ERROR',
      'message': str(exc.detail),
    }

  return JSONResponse(
    status_code=status.HTTP_200_OK,  # [핵심] 상태 코드를 200으로 강제
    content=content,
  )


# 라우터 등록
app.include_router(auth_router)
app.include_router(user_router)


# OpenAPI 스키마 커스터마이징 - 422 응답 제거
def custom_openapi():
  if app.openapi_schema:
    return app.openapi_schema

  openapi_schema = get_openapi(
    title='FastAPI Template',
    version='0.1.0',
    description='FastAPI 템플릿',
    routes=app.routes,
  )

  # 모든 경로(path)를 순회하며 422 응답 정의를 삭제합니다.
  for path in openapi_schema.get('paths', {}).values():
    for method in path.values():
      if 'responses' in method and '422' in method['responses']:
        del method['responses']['422']

  app.openapi_schema = openapi_schema
  return app.openapi_schema


# 커스텀 스키마 함수를 앱에 등록합니다.
app.openapi = custom_openapi  # type: ignore[assignment]


@app.get(
  '/',
  response_model=ApiResponse[str],
  summary='헬로우 월드',
  operation_id='get_hello',
  tags=['기본'],
)
def getHello():
  """기본 헬로우 월드 엔드포인트"""
  return success_response(data='Hello, World!', message='정상 작동 중입니다.')
