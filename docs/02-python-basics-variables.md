# Python 기초: 변수

> JavaScript 비교 섹션은 선택 사항입니다. Python만 학습 중이라면 Python 예제와 설명 위주로 읽고 넘어가도 괜찮습니다. 실습은 `training/1.variable.py`와 노트북 `notebooks/01-python-basics-types-variables.ipynb`에서 진행하세요.

## 개요

Python에서는 변수를 선언할 때 타입을 명시하지 않습니다. 변수명에 값을 할당하면 자동으로 변수가 생성됩니다. 이 문서에서는 변수의 선언, 할당, 그리고 변수명 규칙에 대해 학습합니다.

## 변수 선언과 할당

Python에서는 변수를 선언할 때 타입을 명시하지 않습니다. 변수명에 값을 할당하면 자동으로 변수가 생성됩니다.

**Python 예제:**
```python
# 변수 선언과 할당
x = 10
y = 20.5
name = "Python"
is_valid = True

# 여러 변수에 동시에 할당
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3

# 같은 값으로 여러 변수 초기화
x = y = z = 0
print(x, y, z)  # 0 0 0
```

**JavaScript 예제:**
```javascript
// 변수 선언 (let, const, var)
let x = 10;
const y = 20.5;
var name = "JavaScript";
const isValid = true;

// 여러 변수에 동시에 할당 (구조 분해 할당)
let [a, b, c] = [1, 2, 3];
console.log(a, b, c);  // 1 2 3

// 같은 값으로 여러 변수 초기화
let x2 = y2 = z2 = 0;
console.log(x2, y2, z2);  // 0 0 0
```

**비교 설명:**
- Python은 변수 선언 키워드가 없고, 할당만으로 변수가 생성됩니다.
- JavaScript는 `let`, `const`, `var` 키워드를 사용합니다.
  - `let`: 블록 스코프, 재할당 가능
  - `const`: 블록 스코프, 재할당 불가
  - `var`: 함수 스코프, 재할당 가능 (구식, 권장하지 않음)
- Python의 튜플 언패킹은 JavaScript의 구조 분해 할당과 유사합니다.
- 두 언어 모두 같은 값으로 여러 변수를 초기화할 수 있습니다.

## 변수명 규칙

Python 변수명은 다음 규칙을 따라야 합니다:

1. 영문자, 숫자, 언더스코어(`_`)만 사용 가능
2. 숫자로 시작할 수 없음
3. 대소문자를 구분함
4. 예약어는 사용할 수 없음

```python
# 올바른 변수명
user_name = "홍길동"
age2 = 25
_total = 100

# 잘못된 변수명 (주석 처리)
# 2age = 25        # 숫자로 시작 불가
# user-name = "홍길동"  # 하이픈 사용 불가
# class = "A"      # 예약어 사용 불가
```

## 동적 타입 시스템

Python은 동적 타입 언어이므로, 같은 변수에 다른 타입의 값을 할당할 수 있습니다.

**Python 예제:**
```python
# 변수에 다른 타입 할당 가능
value = 10
print(value, type(value))  # 10 <class 'int'>

value = "문자열"
print(value, type(value))  # 문자열 <class 'str'>

value = 3.14
print(value, type(value))  # 3.14 <class 'float'>
```

**JavaScript 예제:**
```javascript
// 변수에 다른 타입 할당 가능
let value = 10;
console.log(value, typeof value);  // 10 "number"

value = "문자열";
console.log(value, typeof value);  // 문자열 "string"

value = 3.14;
console.log(value, typeof value);  // 3.14 "number"
```

**비교 설명:**
- 두 언어 모두 동적 타입 언어이므로, 변수에 다른 타입의 값을 할당할 수 있습니다.
- Python은 타입이 런타임에 결정되며, 타입 힌트를 사용해 선택적으로 타입을 명시할 수 있습니다.
- JavaScript도 타입이 런타임에 결정되며, TypeScript를 사용하면 정적 타입 검사를 할 수 있습니다.
- 두 언어 모두 타입 안정성을 보장하지 않으므로, 런타임 타입 오류에 주의해야 합니다.

## 실습 예제

```python
# 변수 선언과 할당
user_name = "홍길동"
user_age = 25
user_height = 175.5
is_student = True

# 여러 변수 동시 할당
first_name, last_name = "홍", "길동"
print(f"이름: {first_name}{last_name}")

# 같은 값으로 여러 변수 초기화
x = y = z = 0
print(f"x={x}, y={y}, z={z}")

# 동적 타입 시스템
value = 10
print(f"value: {value}, 타입: {type(value).__name__}")

value = "문자열"
print(f"value: {value}, 타입: {type(value).__name__}")
```

## 요약

### Python
- 변수는 타입 선언 없이 값 할당으로 생성됨
- 여러 변수에 동시에 할당 가능 (튜플 언패킹)
- 같은 값으로 여러 변수 초기화 가능
- 동적 타입 언어로, 변수에 다른 타입의 값을 할당할 수 있음
- 변수명 규칙: 영문자, 숫자, 언더스코어만 사용, 숫자로 시작 불가, 예약어 사용 불가

### JavaScript
- `let`, `const`, `var` 키워드로 변수 선언
- 구조 분해 할당으로 여러 변수에 동시 할당 가능
- 동적 타입 언어이며, 암묵적 타입 변환이 자주 일어남

### 주요 차이점
- Python은 변수 선언 키워드가 없고, 할당만으로 변수 생성
- JavaScript는 `let`, `const`, `var` 키워드 사용
- Python의 튜플 언패킹은 JavaScript의 구조 분해 할당과 유사

## 직접 해보기
1. `user_name`, `user_age`, `user_city` 변수를 선언하고, f-string으로 한 문장 소개 문구를 만들어 보세요.
2. 여러 변수에 동시에 할당하는 방법을 사용해 `x=1, y=2, z=3`을 한 줄로 할당해 보세요.
3. `training/1.variable.py`를 참고해 새로운 변수를 추가하고, `python training/1.variable.py`로 실행한 결과를 관찰하세요.

