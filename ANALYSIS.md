# API 엔드포인트 로직 분석

이 문서는 프로젝트의 주요 API 엔드포인트의 목적과 내부 로직 흐름을 간략하게 설명합니다.

## 인증 라우터 (`/auth`)

인증 관련 모든 기능을 담당합니다.

### `POST /login`
- **목적**: 사용자 로그인
- **로직**:
  1. `AuthService.login` 호출.
  2. DAO를 통해 이메일로 사용자 정보를 조회하고, 비밀번호를 검증합니다.
  3. 이미 활성화된 세션(Refresh Token)이 있는지 확인하여 중복 로그인을 방지합니다.
  4. 검증 성공 시, Access Token과 Refresh Token을 생성합니다.
  5. DAO를 호출하여 데이터베이스에 새로운 Refresh Token과 마지막 로그인 시간을 기록합니다.
  6. 두 토큰을 클라이언트에게 반환합니다.

### `POST /logout`
- **목적**: 사용자 로그아웃
- **로직**:
  1. `AuthService.logout` 호출.
  2. 전달받은 Refresh Token을 검증하여 사용자 정보를 찾습니다.
  3. DAO를 호출하여 데이터베이스에서 해당 사용자의 Refresh Token을 삭제(초기화)합니다.

### `POST /reset-password/request`
- **목적**: 비밀번호 재설정 이메일 요청
- **로직**:
  1. `AuthService.request_reset_password` 호출.
  2. 이메일로 사용자를 조회하고, 비밀번호 재설정 토큰을 생성하여 임시 저장소(메모리)에 보관합니다.
  3. 백그라운드 작업을 통해 사용자에게 재설정 토큰이 포함된 이메일을 발송합니다.

### `POST /reset-password`
- **목적**: 비밀번호 재설정
- **로직**:
  1. `AuthService.reset_password` 호출.
  2. 전달받은 재설정 토큰이 임시 저장소의 값과 일치하는지 확인합니다.
  3. DAO를 호출하여 데이터베이스에 새로운 비밀번호를 해시하여 업데이트하고, 비밀번호 변경일시를 기록합니다.

### `POST /change-password`
- **목적**: 로그인된 사용자의 비밀번호 변경
- **로직**:
  1. `AuthService.change_password` 호출 (현재 로그인된 사용자 번호와 함께).
  2. 현재 비밀번호가 올바른지 검증합니다.
  3. DAO를 호출하여 데이터베이스에 새로운 비밀번호를 해시하여 업데이트하고, 비밀번호 변경일시를 기록합니다.

---

## 사용자 라우터 (`/users`)

사용자 정보의 CRUD(생성, 조회, 수정, 삭제)를 담당합니다. 대부분의 엔드포인트는 JWT 토큰을 통해 현재 로그인된 사용자(`current_user_no`)를 식별하여 감사 필드(생성자, 수정자 번호)를 자동으로 기록합니다.

### `POST /`
- **목적**: 신규 사용자 생성
- **로직**: `UserService.createUser`를 호출합니다. 로그인된 사용자의 번호가 생성자(`crtNo`)로 자동 설정되어 DAO로 전달됩니다.

### `GET /`
- **목적**: 사용자 목록 조회
- **로직**: `UserService.getUserList`를 호출합니다. 쿼리 파라미터를 통해 다양한 조건(사용자명, 이메일 등)으로 필터링이 가능합니다.

### `GET /{user_no}`
- **목적**: 특정 사용자 정보 조회
- **로직**: `UserService.getUserByNo`를 호출하여 해당 번호의 사용자 정보를 조회합니다.

### `GET /email/{eml_addr}`
- **목적**: 이메일로 특정 사용자 정보 조회
- **로직**: `UserService.getUserByEmail`을 호출하여 해당 이메일의 사용자 정보를 조회합니다.

### `PATCH /{user_no}`
- **목적**: 사용자 정보 수정
- **로직**: `UserService.updateUser`를 호출합니다. 로그인된 사용자의 번호가 수정자(`updtNo`)로 자동 설정되어 DAO로 전달됩니다.

### `PATCH /{user_no}/password`
- **목적**: (관리자에 의한) 특정 사용자 비밀번호 수정
- **로직**: `UserService.updateUserPassword`를 호출합니다. 로그인된 사용자의 번호가 수정자(`updtNo`)로 자동 설정되어 DAO로 전달됩니다.

### `DELETE /{user_no}`
- **목적**: 특정 사용자 단건 삭제 (논리적 삭제)
- **로직**: `UserService.deleteUser`를 호출합니다. 로그인된 사용자의 번호가 수정자(`updtNo`)로 자동 설정되며, `delYn` 플래그가 'Y'로 변경됩니다.

### `DELETE /`
- **목적**: 여러 사용자 다건 삭제 (논리적 삭제)
- **로직**: `UserService.deleteUsers`를 호출합니다. 요청 본문에 포함된 사용자 번호 목록(`userNoList`)을 기반으로 여러 사용자를 동시에 논리적으로 삭제합니다.