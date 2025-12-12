# Python 기초: 타입 변환

> JavaScript 비교 섹션은 선택 사항입니다. Python만 학습 중이라면 Python 예제와 설명 위주로 읽고 넘어가도 괜찮습니다. 실습은 `training/1.variable.py`와 노트북 `notebooks/01-python-basics-types-variables.ipynb`에서 진행하세요.

## 개요

타입 변환은 한 타입의 값을 다른 타입으로 변환하는 작업입니다. Python에서는 명시적인 타입 변환 함수를 사용하여 타입을 변환할 수 있습니다.

## 타입 변환 함수

Python은 명시적인 타입 변환 함수를 제공합니다.

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

# 불리언 변환
print(bool(1))    # True
print(bool(0))    # False
print(bool(""))   # False
print(bool("abc")) # True
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

// 불리언 변환
console.log(Boolean(1));    // true
console.log(Boolean(0));    // false
console.log(Boolean(""));  // false
console.log(Boolean("abc")); // true
```

**비교 설명:**
- Python은 `int()`, `str()`, `float()`, `bool()` 같은 명시적인 변환 함수를 사용합니다.
- JavaScript는 `parseInt()`, `parseFloat()`, `Number()`, `String()`, `Boolean()` 등을 사용합니다.
- JavaScript는 암묵적 타입 변환이 자주 일어납니다 (예: `+""`로 숫자를 문자열로 변환).
- Python은 명시적 변환을 선호하며, 암묵적 변환이 적습니다.
- JavaScript의 `parseInt()`와 `parseFloat()`는 문자열의 시작 부분만 파싱하지만, Python의 `int()`와 `float()`는 전체 문자열이 숫자여야 합니다.

## 주요 타입 변환

### 문자열 ↔ 숫자

```python
# 문자열 → 정수
num_str = "42"
num = int(num_str)
print(num, type(num))  # 42 <class 'int'>

# 문자열 → 실수
float_str = "3.14"
float_num = float(float_str)
print(float_num, type(float_num))  # 3.14 <class 'float'>

# 숫자 → 문자열
age = 25
age_str = str(age)
print(age_str, type(age_str))  # 25 <class 'str'>
```

### 숫자 타입 간 변환

```python
# 정수 → 실수
integer = 42
floating = float(integer)
print(floating)  # 42.0

# 실수 → 정수 (소수점 이하 버림)
pi = 3.14159
pi_int = int(pi)
print(pi_int)  # 3
```

### 불리언 변환

```python
# 숫자 → 불리언
print(bool(1))    # True
print(bool(0))    # False
print(bool(-1))   # True (0이 아닌 모든 숫자는 True)

# 문자열 → 불리언
print(bool(""))   # False
print(bool("abc")) # True

# 리스트 → 불리언
print(bool([]))   # False
print(bool([1, 2])) # True
```

## 타입 변환 오류 처리

타입 변환 시 오류가 발생할 수 있으므로 주의가 필요합니다.

```python
# 올바른 변환
age = int("25")  # 25

# 오류 발생
# age = int("25.5")  # ValueError: invalid literal for int()

# 안전한 변환
def safe_int(value):
    try:
        return int(value)
    except ValueError:
        return None

result = safe_int("25.5")
print(result)  # None
```

## 실습 예제

```python
# 타입 변환 예제
age_input = "30"
age = int(age_input)
print(f"입력된 나이: {age_input}, 변환된 나이: {age}")

# 여러 타입 변환
price_str = "19.99"
price = float(price_str)
price_int = int(price)
print(f"가격 문자열: {price_str}")
print(f"실수: {price}")
print(f"정수: {price_int}")

# 불리언 변환
is_valid = bool(1)
is_empty = bool("")
print(f"is_valid: {is_valid}, is_empty: {is_empty}")
```

## 요약

### Python
- `int()`: 정수로 변환
- `str()`: 문자열로 변환
- `float()`: 실수로 변환
- `bool()`: 불리언으로 변환
- 명시적 변환을 선호하며, 암묵적 변환이 적음
- 전체 문자열이 숫자여야 변환 가능

### JavaScript
- `parseInt()`: 정수로 변환 (문자열의 시작 부분만 파싱)
- `parseFloat()`: 실수로 변환
- `Number()`: 숫자로 변환
- `String()`: 문자열로 변환
- `Boolean()`: 불리언으로 변환
- 암묵적 타입 변환이 자주 일어남

### 주요 차이점
- Python은 명시적 타입 변환을 선호하지만, JavaScript는 암묵적 변환이 많음
- Python의 `int()`와 `float()`는 전체 문자열이 숫자여야 하지만, JavaScript의 `parseInt()`와 `parseFloat()`는 시작 부분만 파싱
- Python은 타입 변환 오류를 명확히 발생시키지만, JavaScript는 `NaN`을 반환할 수 있음

## 직접 해보기
1. 문자열 `"42"`를 정수로 변환한 뒤 다시 문자열로 변환하는 코드를 작성하세요.
2. 사용자 입력을 받아 정수로 변환하고, 오류가 발생할 경우를 처리하는 코드를 작성하세요.
3. 다양한 타입의 값을 불리언으로 변환하고 결과를 확인해 보세요.

