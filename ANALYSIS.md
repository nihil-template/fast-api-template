# FastAPI 프로젝트 구조 분석 및 스프링부트 비교

## 현재 프로젝트 구조

### 계층 구조
```
Router (Controller) 
  ↓ VO (Pydantic Schema)
Service (Business Logic)
  ↓ Entity (SQLModel) / dict
DAO (Data Access)
  ↓ Entity (SQLModel)
Database
```

### 현재 구조의 특징

#### 1. Router (Controller) - `routers/user_router.py`
- ✅ FastAPI의 `APIRouter` 사용
- ✅ Pydantic 스키마로 요청/응답 검증
- ✅ Service에 의존성 주입
- ⚠️ Service가 Entity를 반환하지만 FastAPI가 자동으로 VO로 변환

#### 2. Service (Business Logic) - `services/user_service.py`
- ✅ 비즈니스 로직 처리
- ✅ DAO 호출
- ⚠️ **Entity를 직접 반환** (`ApiResponse[UserInfo]`)
- ⚠️ **dict 변환 로직 존재** (`user_data.model_dump()`)
- ⚠️ Entity와 VO가 혼재

#### 3. DAO (Data Access) - `dao/user_dao.py`
- ✅ 데이터베이스 접근만 담당
- ⚠️ **dict를 받아서 처리** (`create_user(session, user_data: dict)`)
- ✅ Entity 반환

#### 4. Schemas (VO) - `schemas/user_schema.py`
- ✅ 요청 VO: `CreateUser`, `UpdateUser`, `DeleteUserRequest`
- ✅ 응답 VO: `UserResponse`
- ✅ Pydantic으로 검증 및 변환

#### 5. Models (Entity) - `models/user.py`
- ✅ SQLModel 엔티티
- ✅ 데이터베이스 테이블과 매핑

---

## 스프링부트와 비교

### 스프링부트 구조
```
Controller
  ↓ VO (DTO)
Service
  ↓ VO (DTO)
Repository
  ↓ Entity (JPA)
Database
```

### 주요 차이점

| 항목 | 스프링부트 | 현재 FastAPI | 개선 필요 |
|------|-----------|-------------|----------|
| **Service 반환 타입** | VO (DTO) | Entity | ✅ VO로 변경 |
| **DAO 파라미터** | Entity 또는 VO | dict | ✅ VO로 변경 |
| **계층 간 데이터 전달** | VO 중심 | Entity/dict 혼재 | ✅ VO 중심으로 통일 |
| **변환 로직 위치** | Service에서 명시적 변환 | FastAPI 자동 변환 | ✅ Service에서 명시적 변환 |

---

## 현재 구조의 문제점

### 1. Service에서 Entity 직접 반환
```python
# 현재
def createUser(self, user_data: CreateUser) -> ApiResponse[UserInfo]:
    user = self.dao.create_user(self.session, user_dict)
    return success_response(data=user, ...)  # Entity 반환
```

**문제:**
- Service 계층이 Entity에 의존
- 비즈니스 로직과 데이터베이스 구조가 결합
- 테스트 시 Entity 모킹 필요

### 2. DAO에서 dict 사용
```python
# 현재
def create_user(session: Session, user_data: dict) -> UserInfo:
    user = UserInfo(**user_data)
```

**문제:**
- 타입 안정성 부족
- IDE 자동완성 불가
- 런타임 에러 가능성

### 3. Service에서 dict 변환
```python
# 현재
user_dict = user_data.model_dump()
if 'password' in user_dict:
    user_dict['encptPswd'] = hash_password(user_dict.pop('password'))
```

**문제:**
- VO의 장점을 활용하지 못함
- 필드명 변환 로직이 Service에 존재

---

## 개선 방안

### 목표: 완전한 VO 중심 아키텍처 (서버 내부는 완전한 VO, 외부는 상황별 스키마)

**핵심 원칙:**
- **서버 내부**: 완전한 VO 사용 (테이블 구조 + 확장 필드 포함)
- **외부 통신**: 상황에 맞는 스키마로 필터링 (FastAPI의 response_model 활용)

### 1. Service에서 완전한 VO 받기 및 반환

**핵심 원칙: 모든 Service 메서드는 완전한 VO를 받아서 처리**

```python
# 개선 후 - 완전한 VO를 받아서 처리
def createUser(self, user_vo: UserVo) -> ApiResponse[UserVo]:
    """완전한 VO를 받아서 그 안에서 필요한 필드를 꺼내서 처리"""
    # VO에서 필요한 필드 추출
    if user_vo.emlAddr:
        # 이메일 중복 체크
        existing_user = self.dao.get_user_by_email(self.session, user_vo.emlAddr)
        if existing_user:
            return error_response(...)
    
    # 비밀번호 해시화 (VO에서 password 필드가 있으면)
    if user_vo.password:
        user_vo.encptPswd = hash_password(user_vo.password)
    
    # DAO에 VO 전달
    user_entity = self.dao.create_user(self.session, user_vo)
    
    # Entity를 완전한 VO로 변환하여 반환
    user_response = UserVo.model_validate(user_entity)
    return success_response(data=user_response, ...)

def getUserByNo(self, user_vo: UserVo) -> ApiResponse[UserVo]:
    """완전한 VO를 받아서 그 안에서 userNo를 꺼내서 처리"""
    # VO에서 userNo 추출
    user_no = user_vo.userNo
    user_entity = self.dao.get_user_by_no(self.session, user_no)
    if not user_entity:
        return error_response(...)
    
    user_response = UserVo.model_validate(user_entity)
    return success_response(data=user_response, ...)

def getUserList(self, user_vo: UserVo) -> ApiResponse[ListResponse[UserVo]]:
    """완전한 VO를 받아서 그 안에서 검색 조건 등을 꺼내서 처리"""
    # VO에서 검색 조건 추출 (예: user_vo.userNm, user_vo.emlAddr, user_vo.srchKywd 등)
    # SearchVo의 페이지네이션 필드도 활용 가능 (page, pageSz 등)
    users = self.dao.get_users(self.session, user_vo)  # VO 전달
    user_responses = [UserVo.model_validate(u) for u in users]
    return success_response(data=ListResponse(list=user_responses, totalCnt=len(user_responses)), ...)
```

**장점:**
- 모든 메서드가 일관되게 VO를 받음
- Service가 Entity에 의존하지 않음
- 완전한 VO를 반환하여 서버 내부에서 모든 정보 활용 가능
- 확장 필드 추가 용이
- 검색 조건도 VO에 포함 가능

### 2. DAO에서 완전한 VO 받기

```python
# 개선 후 - 완전한 VO를 받아서 처리
@staticmethod
def create_user(session: Session, user_vo: UserVo) -> UserInfo:
    """완전한 VO를 받아서 Entity로 변환"""
    # VO에서 필요한 필드만 추출하여 Entity 생성
    # Service에서 이미 비밀번호 해시화 등 변환 완료
    user = UserInfo(
        emlAddr=user_vo.emlAddr,
        userNm=user_vo.userNm,
        encptPswd=user_vo.encptPswd,  # Service에서 해시화된 값
        userRole=user_vo.userRole,
        # ... 기타 필드
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@staticmethod
def get_users(session: Session, user_vo: UserVo) -> list[UserInfo]:
    """완전한 VO를 받아서 검색 조건으로 사용"""
    statement = select(UserInfo)
    
    # VO에서 검색 조건 추출
    if user_vo.userNm:
        statement = statement.where(UserInfo.userNm == user_vo.userNm)
    if user_vo.emlAddr:
        statement = statement.where(UserInfo.emlAddr == user_vo.emlAddr)
    # ... 기타 검색 조건
    
    return list(session.exec(statement).all())
```

### 3. 완전한 VO 정의 (확장 필드 포함 가능)

**구현 완료: `src/vos/` 폴더에 VO 구조 생성**

```python
# src/vos/search_vo.py - 공통 검색/페이지네이션 VO
class SearchVo(BaseModel):
    """검색/페이지네이션용 VO (모든 리소스에서 공통 사용)"""
    page: Optional[int] = None
    pageSz: Optional[int] = 10  # 기본값 10
    strtRow: Optional[int] = None
    endRow: Optional[int] = None
    srchType: Optional[str] = None
    srchKywd: Optional[str] = None

# src/vos/user_vo.py - 사용자 VO
class UserVo(SearchVo):
    """사용자 VO (모든 작업에서 사용 - 하나의 VO로 get, post, update, delete 처리)"""
    # 테이블 필드 (모두 Optional로 정의하여 검색/생성/수정/삭제 모두에서 사용)
    userNo: Optional[int] = None
    emlAddr: Optional[EmailStr] = None
    userNm: Optional[str] = None
    userRole: Optional[UserRole] = None
    password: Optional[str] = None  # 입력용 (Service에서 encptPswd로 변환)
    encptPswd: Optional[str] = None  # 저장용 (Service에서 해시화된 값)
    proflImg: Optional[str] = None
    userBiogp: Optional[str] = None
    reshToken: Optional[str] = None
    useYn: Optional[YnStatus] = None
    delYn: Optional[YnStatus] = None
    lastLgnDt: Optional[str] = None
    lastPswdChgDt: Optional[str] = None
    crtNo: Optional[int] = None
    crtDt: Optional[str] = None
    updtNo: Optional[int] = None
    updtDt: Optional[str] = None
    delNo: Optional[int] = None
    delDt: Optional[str] = None
    
    # 확장 필드 (검색 조건, 계산된 필드 등)
    userNoList: Optional[list[int]] = None  # 검색/삭제용
    
    class Config:
        from_attributes = True
```

**핵심 원칙:**
- **하나의 VO로 모든 작업 처리**: `UserVo` 하나로 get, post, update, delete 모두 처리
- **SearchVo 상속**: 검색/페이지네이션 기능을 공통 VO로 분리하여 재사용
- **모든 필드 Optional**: 검색/생성/수정/삭제 모든 상황에서 사용 가능

### 4. Router에서 완전한 VO 받기

```python
# Router에서도 완전한 VO를 받아서 Service에 전달
@router.post('/users/')
def createUser(
    user_vo: UserVo,  # 완전한 VO를 받음
    service: UserService = Depends(get_user_service),
):
    """완전한 VO를 받아서 Service에 그대로 전달"""
    return service.createUser(user_vo)

@router.get('/users/{user_no}')
def getUserByNo(
    user_no: int,  # Path 파라미터
    service: UserService = Depends(get_user_service),
):
    """Path 파라미터를 VO로 변환하여 Service에 전달"""
    user_vo = UserVo(userNo=user_no)
    return service.getUserByNo(user_vo)

@router.get('/users/')
def getUserList(
    user_vo: UserVo = Depends(),  # Query 파라미터를 VO로 자동 변환
    service: UserService = Depends(get_user_service),
):
    """Query 파라미터를 VO로 받아서 Service에 전달"""
    return service.getUserList(user_vo)
```

**FastAPI의 자동 변환:**
- FastAPI는 Query 파라미터를 자동으로 Pydantic 모델로 변환
- `?userNm=홍길동&emlAddr=test@example.com` → `UserVo(userNm="홍길동", emlAddr="test@example.com")`

### 5. 외부 통신 시 상황별 스키마 필터링

FastAPI의 `response_model_exclude`, `response_model_include` 활용:

```python
# Router에서 상황별 스키마 정의
class UserPublicResponse(BaseModel):
    """공개용 사용자 정보 (민감 정보 제외)"""
    userNo: Optional[int]
    userNm: str
    proflImg: Optional[str]
    userBiogp: Optional[str]
    # 비밀번호, 이메일 등 제외

class UserDetailResponse(UserResponse):
    """상세 정보 (모든 필드 포함)"""
    pass

# Router에서 사용
@router.get('/users/{user_no}', response_model=ApiResponse[UserPublicResponse])
def getUserByNo(
    user_no: int,
    service: UserService = Depends(get_user_service),
):
    """Service는 완전한 VO 반환, FastAPI가 자동으로 필터링"""
    user_vo = UserVo(userNo=user_no)
    return service.getUserByNo(user_vo)
    # FastAPI가 자동으로 UserPublicResponse로 필터링
```

**또는 동적 필터링:**

```python
@router.get('/users/{user_no}')
def getUserByNo(
    user_no: int,
    fields: Optional[str] = None,  # ?fields=userNo,userNm,emlAddr
    service: UserService = Depends(get_user_service),
):
    """Service는 완전한 VO 반환, 필요시 필드 필터링"""
    user_vo = UserVo(userNo=user_no)
    response = service.getUserByNo(user_vo)
    
    # 필드 필터링 (필요시)
    if fields and response.data:
        field_list = fields.split(',')
        filtered_data = {
            k: v for k, v in response.data.model_dump().items() 
            if k in field_list
        }
        response.data = UserResponse(**filtered_data)
    
    return response
```

### 6. DAO에서 VO 사용

**구현 원칙: DAO는 UserVo를 받아서 처리**

```python
# DAO에서 UserVo를 받아서 Entity로 변환
@staticmethod
def create_user(session: Session, user_vo: UserVo) -> UserInfo:
    """UserVo를 받아서 Entity로 변환"""
    # Service에서 이미 비밀번호 해시화 등 변환 완료
    # VO에서 필요한 필드만 추출하여 Entity 생성
    user = UserInfo(
        emlAddr=user_vo.emlAddr,
        userNm=user_vo.userNm,
        encptPswd=user_vo.encptPswd,  # Service에서 해시화된 값
        userRole=user_vo.userRole or UserRole.USER,
        # ... 기타 필드
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
```

**참고:** 내부용 VO(CreateUserVO, UpdateUserVO)는 제거하고, 하나의 `UserVo`로 모든 작업을 처리합니다.

---

## 개선 우선순위

### Phase 1: VO 구조 생성 (✅ 완료)
- ✅ `src/vos/` 폴더 생성
- ✅ `SearchVo` 생성 (공통 검색/페이지네이션 필드)
- ✅ `UserVo` 생성 (SearchVo 상속, 하나의 VO로 모든 작업 처리)

### Phase 2: Service 반환 타입 변경 (진행 필요)
- Service 메서드 반환 타입을 `ApiResponse[UserVo]`로 변경
- Entity → 완전한 VO 변환 로직 추가
- **서버 내부에서는 완전한 VO 사용**

### Phase 3: DAO 파라미터 타입 개선 (진행 필요)
- dict 대신 `UserVo` 사용
- 타입 안정성 향상

### Phase 4: Router에서 VO 사용 (진행 필요)
- Router에서 `UserVo`를 받아서 Service에 전달
- Path 파라미터, Query 파라미터를 VO로 변환
- FastAPI의 자동 변환 기능 활용

### Phase 5: 외부 통신용 스키마 필터링 (권장)
- FastAPI의 `response_model_exclude`, `response_model_include` 활용
- 상황별 응답 스키마 정의 (필요시)
- **프론트엔드나 각 상황에 맞는 스키마 설정**

### Phase 6: 확장 필드 지원 (✅ 완료)
- ✅ 완전한 VO에 확장 필드 추가 (`userNoList` 등)
- 계산된 필드, 조인된 데이터 등 추가 가능

---

## 예상 효과

### 장점
1. **계층 분리 명확화**: 각 계층이 명확한 책임
2. **타입 안정성**: dict 대신 VO 사용
3. **테스트 용이성**: Entity 없이 Service 테스트 가능
4. **유지보수성**: 변경 영향 범위 최소화
5. **완전한 VO 활용**: 서버 내부에서 모든 정보 활용 가능
6. **유연한 외부 통신**: 상황에 맞는 스키마로 필터링
7. **확장성**: 확장 필드 추가 용이
8. **스프링부트와 유사한 구조**: 개발자 친화적

### 단점
1. **변환 오버헤드**: Entity ↔ VO 변환 비용 (미미함)
2. **코드 증가**: 변환 로직 추가 필요
3. **초기 작업량**: 기존 코드 리팩토링 필요
4. **스키마 관리**: 여러 스키마 관리 필요 (하지만 유연성 확보)

---

## 결론

현재 구조는 **기본적인 계층 분리는 되어 있으나**, Service와 DAO 사이에서 Entity와 dict가 혼재되어 있습니다.

**완전한 VO 중심 아키텍처로 개선**하면:
- ✅ 계층 간 의존성 감소
- ✅ 타입 안정성 향상
- ✅ 테스트 용이성 향상
- ✅ 유지보수성 향상
- ✅ **서버 내부는 완전한 VO 사용** (모든 정보 활용 가능)
- ✅ **외부 통신은 상황별 스키마** (필요한 필드만 노출)

**핵심 원칙:**
1. **하나의 VO로 모든 작업**: `UserVo` 하나로 get, post, update, delete 모두 처리
2. **서버 내부**: 완전한 VO (`UserVo`) - 테이블 구조 + 확장 필드 + 검색/페이지네이션 필드
3. **공통 기능 분리**: `SearchVo`로 검색/페이지네이션 기능 공통화
4. **외부 통신**: FastAPI의 `response_model`로 필터링 (필요시)

**개선 진행 상황:**
1. ✅ VO 구조 생성 (`SearchVo`, `UserVo`)
2. ⏳ Service 반환 타입을 완전한 VO로 변경 (진행 필요)
3. ⏳ DAO 파라미터를 VO로 변경 (진행 필요)
4. ⏳ Router에서 VO 사용 (진행 필요)
5. ⏳ 외부 통신용 스키마 필터링 (권장)

