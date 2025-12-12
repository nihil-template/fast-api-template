# Python 기초: 기본 타입

> JavaScript 비교 섹션은 선택 사항입니다. Python만 학습 중이라면 Python 예제와 설명 위주로 읽고 넘어가도 괜찮습니다. 실습은 `training/1.variable.py`와 노트북 `notebooks/01-python-basics-types-variables.ipynb`에서 진행하세요.

## 개요

Python은 동적 타입 언어입니다. 변수를 선언할 때 타입을 명시하지 않아도 되며, 변수에 할당되는 값에 따라 타입이 자동으로 결정됩니다. 이 문서에서는 Python의 기본 타입에 대해 학습합니다.

## 기본 타입

Python에는 여러 기본 타입이 있습니다. 각 타입은 특정 종류의 데이터를 나타냅니다.

### 1. 정수 (int)

정수형 데이터를 나타냅니다. 양수, 음수, 0 모두 포함합니다.

**Python 예제:**
```python
# 정수 예제
age = 25
temperature = -10
count = 0

print(type(age))  # <class 'int'>
print(age)        # 25
```

**JavaScript 예제:**
```javascript
// JavaScript는 정수와 실수를 구분하지 않음 (모두 Number 타입)
let age = 25;
let temperature = -10;
let count = 0;

console.log(typeof age);  // "number"
console.log(age);         // 25
```

**비교 설명:**
- Python은 `int`와 `float`를 명확히 구분합니다.
- JavaScript는 정수와 실수를 구분하지 않고 모두 `Number` 타입입니다.
- Python의 정수는 무한 정밀도를 지원하지만, JavaScript의 Number는 IEEE 754 표준을 따릅니다.

### 2. 실수 (float)

소수점이 있는 숫자를 나타냅니다.

**Python 예제:**
```python
# 실수 예제
pi = 3.14159
price = 19.99
temperature = -5.5

print(type(pi))  # <class 'float'>
print(pi)        # 3.14159
```

**JavaScript 예제:**
```javascript
// JavaScript는 정수와 실수를 구분하지 않음
let pi = 3.14159;
let price = 19.99;
let temperature = -5.5;

console.log(typeof pi);  // "number"
console.log(pi);         // 3.14159
```

**비교 설명:**
- Python은 `float` 타입이 별도로 존재합니다.
- JavaScript는 정수와 실수 모두 `Number` 타입으로 처리됩니다.
- 두 언어 모두 부동소수점 연산의 정밀도 문제를 가지고 있습니다.

### 3. 문자열 (str)

텍스트 데이터를 나타냅니다. 작은따옴표(`'`) 또는 큰따옴표(`"`)로 감싸서 표현합니다.

**Python 예제:**
```python
# 문자열 예제
name = "홍길동"
greeting = '안녕하세요'
message = "Python은 '간단한' 언어입니다"

print(type(name))  # <class 'str'>
print(name)        # 홍길동

# 여러 줄 문자열
multiline = """
첫 번째 줄
두 번째 줄
세 번째 줄
"""
```

**JavaScript 예제:**
```javascript
// 문자열 예제
let name = "홍길동";
let greeting = '안녕하세요';
let message = "JavaScript는 '간단한' 언어입니다";

console.log(typeof name);  // "string"
console.log(name);         // 홍길동

// 여러 줄 문자열 (템플릿 리터럴)
let multiline = `
첫 번째 줄
두 번째 줄
세 번째 줄
`;

// 또는 백슬래시 사용
let multiline2 = "첫 번째 줄\n두 번째 줄\n세 번째 줄";
```

**비교 설명:**
- 두 언어 모두 작은따옴표와 큰따옴표를 사용할 수 있습니다.
- Python은 삼중 따옴표(`"""` 또는 `'''`)로 여러 줄 문자열을 만듭니다.
- JavaScript는 템플릿 리터럴(백틱 `` ` ``)을 사용하거나 이스케이프 문자(`\n`)를 사용합니다.
- JavaScript의 템플릿 리터럴은 문자열 보간(`${변수}`)을 지원합니다.

### 4. 불리언 (bool)

참(True) 또는 거짓(False) 값을 나타냅니다.

**Python 예제:**
```python
# 불리언 예제
is_active = True
is_completed = False

print(type(is_active))  # <class 'bool'>
print(is_active)        # True
```

**JavaScript 예제:**
```javascript
// 불리언 예제
let isActive = true;
let isCompleted = false;

console.log(typeof isActive);  // "boolean"
console.log(isActive);         // true
```

**비교 설명:**
- Python은 `True`와 `False`(대문자 시작)를 사용합니다.
- JavaScript는 `true`와 `false`(소문자)를 사용합니다.
- 두 언어 모두 불리언 타입을 별도로 가지고 있습니다.
- JavaScript는 `truthy`와 `falsy` 값 개념이 있어 더 유연한 타입 변환이 일어납니다.

### 5. None / null / undefined

값이 없음을 나타내는 특별한 타입입니다.

**Python 예제:**
```python
# None 예제
result = None
data = None

print(type(result))  # <class 'NoneType'>
print(result)        # None
```

**JavaScript 예제:**
```javascript
// null과 undefined 예제
let result = null;
let data = undefined;
let notDefined;  // undefined

console.log(typeof result);     // "object" (JavaScript의 설계상 오류)
console.log(typeof data);       // "undefined"
console.log(result);            // null
console.log(data);              // undefined
console.log(notDefined);        // undefined
```

**비교 설명:**
- Python은 `None` 하나만 사용합니다.
- JavaScript는 `null`(의도적으로 비어있음)과 `undefined`(정의되지 않음) 두 가지를 사용합니다.
- Python의 `None`은 JavaScript의 `null`과 유사하지만, JavaScript의 `undefined`는 Python에 직접 대응되는 개념이 없습니다.
- JavaScript에서 `typeof null`은 `"object"`를 반환하는데, 이는 언어 설계상의 오류입니다.

## 실습 예제

```python
# 다양한 타입의 변수 선언
age = 25              # 정수
height = 175.5        # 실수
name = "홍길동"       # 문자열
is_student = True     # 불리언
email = None          # None

# 타입 확인
print(f"나이: {age} (타입: {type(age).__name__})")
print(f"키: {height} (타입: {type(height).__name__})")
print(f"이름: {name} (타입: {type(name).__name__})")
print(f"학생 여부: {is_student} (타입: {type(is_student).__name__})")
print(f"이메일: {email} (타입: {type(email).__name__})")
```

## 요약

### Python
- Python의 기본 타입: `int`, `float`, `str`, `bool`, `None`
- 각 타입은 특정 종류의 데이터를 나타냅니다
- 타입은 변수에 할당되는 값에 따라 자동으로 결정됩니다

### JavaScript
- JavaScript의 기본 타입: `Number`, `String`, `Boolean`, `null`, `undefined`, `Symbol`, `BigInt`
- JavaScript는 정수와 실수를 구분하지 않고 모두 `Number` 타입입니다

### 주요 차이점
- Python은 정수와 실수를 구분하지만, JavaScript는 모두 Number 타입
- Python은 `None` 하나만 사용하지만, JavaScript는 `null`과 `undefined` 두 가지 사용
- Python의 불리언은 `True`/`False`(대문자), JavaScript는 `true`/`false`(소문자)

## 직접 해보기
1. 정수, 실수, 문자열, 불리언, None 타입의 변수를 각각 하나씩 선언하고 `type()` 함수로 타입을 확인해 보세요.
2. 삼중 따옴표를 사용해 여러 줄 문자열을 만들고 출력해 보세요.
3. `training/1.variable.py`를 참고해 다양한 타입의 변수를 추가하고, `python training/1.variable.py`로 실행한 결과를 관찰하세요.

