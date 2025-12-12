# Python 기초: 타입과 변수

## 개요

Python은 동적 타입 언어입니다. 변수를 선언할 때 타입을 명시하지 않아도 되며, 변수에 할당되는 값에 따라 타입이 자동으로 결정됩니다. JavaScript도 동적 타입 언어이지만, 몇 가지 중요한 차이점이 있습니다.

## 기본 타입

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

## 타입 확인

### type() 함수

변수의 타입을 확인할 수 있습니다.

**Python 예제:**
```python
age = 25
name = "홍길동"
price = 19.99

print(type(age))   # <class 'int'>
print(type(name))  # <class 'str'>
print(type(price)) # <class 'float'>
```

**JavaScript 예제:**
```javascript
let age = 25;
let name = "홍길동";
let price = 19.99;

console.log(typeof age);   // "number"
console.log(typeof name);  // "string"
console.log(typeof price); // "number"
```

**비교 설명:**
- Python의 `type()`은 타입 객체를 반환합니다.
- JavaScript의 `typeof`는 타입 이름 문자열을 반환합니다.
- JavaScript는 `typeof`로는 객체의 구체적인 타입을 구분하기 어렵습니다 (예: 배열, 객체, null 모두 "object").

### isinstance() 함수

변수가 특정 타입인지 확인할 수 있습니다. `type()`보다 더 안전한 방법입니다.

**Python 예제:**
```python
age = 25
name = "홍길동"

print(isinstance(age, int))   # True
print(isinstance(age, str))   # False
print(isinstance(name, str))  # True
```

**JavaScript 예제:**
```javascript
let age = 25;
let name = "홍길동";

console.log(age instanceof Number);   // false (원시 타입은 false)
console.log(typeof age === "number"); // true
console.log(typeof name === "string"); // true

// 배열이나 객체의 경우
let arr = [1, 2, 3];
console.log(Array.isArray(arr));      // true
console.log(arr instanceof Array);   // true
```

**비교 설명:**
- Python의 `isinstance()`는 상속 관계도 고려하여 타입을 확인합니다.
- JavaScript의 `instanceof`는 프로토타입 체인을 확인하지만, 원시 타입에는 작동하지 않습니다.
- JavaScript는 `Array.isArray()` 같은 특수한 타입 확인 함수를 제공합니다.

## 타입 변환

다른 타입으로 변환할 수 있습니다.

**Python 예제:**
```python
# 문자열을 정수로 변환
age_str = "25"
age_int = int(age_str)
print(age_int, type(age_int))  # 25 <class 'int'>

# 정수를 문자열로 변환
age = 25
age_str = str(age)
print(age_str, type(age_str))  # 25 <class 'str'>

# 문자열을 실수로 변환
price_str = "19.99"
price_float = float(price_str)
print(price_float, type(price_float))  # 19.99 <class 'float'>

# 실수를 정수로 변환 (소수점 이하 버림)
pi = 3.14159
pi_int = int(pi)
print(pi_int)  # 3
```

**JavaScript 예제:**
```javascript
// 문자열을 숫자로 변환
let ageStr = "25";
let ageInt = parseInt(ageStr);        // 25
let ageInt2 = Number(ageStr);          // 25
let ageInt3 = +ageStr;                 // 25 (단항 연산자)

// 숫자를 문자열로 변환
let age = 25;
let ageStr2 = String(age);            // "25"
let ageStr3 = age.toString();          // "25"
let ageStr4 = age + "";                // "25" (문자열 연결)

// 문자열을 실수로 변환
let priceStr = "19.99";
let priceFloat = parseFloat(priceStr); // 19.99
let priceFloat2 = Number(priceStr);     // 19.99

// 실수를 정수로 변환
let pi = 3.14159;
let piInt = Math.floor(pi);            // 3 (내림)
let piInt2 = Math.ceil(pi);            // 4 (올림)
let piInt3 = Math.round(pi);           // 3 (반올림)
let piInt4 = parseInt(pi);             // 3
```

**비교 설명:**
- Python은 `int()`, `str()`, `float()` 같은 명시적인 변환 함수를 사용합니다.
- JavaScript는 `parseInt()`, `parseFloat()`, `Number()`, `String()` 등을 사용합니다.
- JavaScript는 암묵적 타입 변환이 자주 일어납니다 (예: `+""`로 숫자를 문자열로 변환).
- Python은 명시적 변환을 선호하며, 암묵적 변환이 적습니다.
- JavaScript의 `parseInt()`와 `parseFloat()`는 문자열의 시작 부분만 파싱하지만, Python의 `int()`와 `float()`는 전체 문자열이 숫자여야 합니다.

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
# 사용자 정보 저장
user_name = "홍길동"
user_age = 25
user_height = 175.5
is_student = True
email = None

# 타입 확인
print(f"이름: {user_name} (타입: {type(user_name).__name__})")
print(f"나이: {user_age} (타입: {type(user_age).__name__})")
print(f"키: {user_height} (타입: {type(user_height).__name__})")
print(f"학생 여부: {is_student} (타입: {type(is_student).__name__})")
print(f"이메일: {email} (타입: {type(email).__name__})")

# 타입 변환 예제
age_input = "30"
age = int(age_input)
print(f"입력된 나이: {age_input}, 변환된 나이: {age}")
```

## 요약

### Python
- Python의 기본 타입: `int`, `float`, `str`, `bool`, `None`
- 변수는 타입 선언 없이 값 할당으로 생성됨
- `type()`과 `isinstance()`로 타입 확인 가능
- `int()`, `str()`, `float()` 등으로 타입 변환 가능
- Python은 동적 타입 언어로, 변수에 다른 타입의 값을 할당할 수 있음

### JavaScript
- JavaScript의 기본 타입: `Number`, `String`, `Boolean`, `null`, `undefined`, `Symbol`, `BigInt`
- `let`, `const`, `var` 키워드로 변수 선언
- `typeof`와 `instanceof`로 타입 확인 가능
- `parseInt()`, `parseFloat()`, `Number()`, `String()` 등으로 타입 변환 가능
- JavaScript도 동적 타입 언어이며, 암묵적 타입 변환이 자주 일어남

### 주요 차이점
- Python은 정수와 실수를 구분하지만, JavaScript는 모두 Number 타입
- Python은 `None` 하나만 사용하지만, JavaScript는 `null`과 `undefined` 두 가지 사용
- Python은 명시적 타입 변환을 선호하지만, JavaScript는 암묵적 변환이 많음
- JavaScript는 템플릿 리터럴로 문자열 보간을 지원하지만, Python은 f-string 사용

