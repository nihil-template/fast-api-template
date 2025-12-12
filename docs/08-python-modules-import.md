# Python 기초: 모듈과 Import

## 개요

모듈은 Python 코드를 파일 단위로 구성하는 방법입니다. 코드를 재사용하고 구조화하기 위해 모듈을 사용합니다. Python과 JavaScript 모두 모듈 시스템을 제공하지만, 문법과 동작 방식에 차이가 있습니다.

## 모듈이란?

모듈은 Python 코드가 담긴 파일(`.py`)입니다. 함수, 클래스, 변수 등을 정의하고 다른 파일에서 재사용할 수 있습니다.

```python
# math_utils.py (모듈 파일)
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

PI = 3.14159
```

## Import 방법

### 기본 import

모듈 전체를 가져옵니다.

**Python 예제:**
```python
# math_utils.py 파일이 같은 디렉토리에 있다고 가정
import math_utils

result = math_utils.add(3, 5)
print(result)  # 8

print(math_utils.PI)  # 3.14159
```

**JavaScript 예제:**
```javascript
// CommonJS (Node.js)
const mathUtils = require('./math_utils');
let result = mathUtils.add(3, 5);
console.log(result);  // 8

// ES6 모듈
import mathUtils from './math_utils.js';
let result2 = mathUtils.add(3, 5);
console.log(result2);  // 8
```

**비교 설명:**
- Python은 `import` 키워드로 모듈을 가져옵니다.
- JavaScript는 CommonJS(`require`)와 ES6 모듈(`import`) 두 가지 방식을 지원합니다.
- Python은 파일 확장자 없이 모듈을 import하지만, JavaScript ES6 모듈은 확장자가 필요할 수 있습니다.

### from ... import

모듈에서 특정 항목만 가져옵니다.

**Python 예제:**
```python
# 특정 함수만 가져오기
from math_utils import add

result = add(3, 5)
print(result)  # 8

# 여러 항목 가져오기
from math_utils import add, multiply, PI

result1 = add(3, 5)
result2 = multiply(3, 5)
print(result1, result2, PI)  # 8 15 3.14159
```

**JavaScript 예제:**
```javascript
// ES6 모듈 - named import
import { add, multiply, PI } from './math_utils.js';

let result1 = add(3, 5);
let result2 = multiply(3, 5);
console.log(result1, result2, PI);  // 8 15 3.14159

// CommonJS는 구조 분해 할당 사용
const { add, multiply, PI } = require('./math_utils');
```

**비교 설명:**
- Python은 `from module import item` 형식을 사용합니다.
- JavaScript ES6 모듈은 `import { item } from module` 형식을 사용합니다.
- 두 언어 모두 여러 항목을 한 번에 import할 수 있습니다.

### from ... import * (권장하지 않음)

모듈의 모든 항목을 가져옵니다. 이름 충돌 가능성이 있어 권장하지 않습니다.

```python
# 모든 항목 가져오기 (권장하지 않음)
from math_utils import *

result = add(3, 5)
print(result)  # 8
```

### as 별칭

모듈이나 항목에 별칭을 지정할 수 있습니다.

```python
# 모듈에 별칭 지정
import math_utils as math

result = math.add(3, 5)
print(result)  # 8

# 항목에 별칭 지정
from math_utils import add as plus

result = plus(3, 5)
print(result)  # 8
```

## 내장 모듈

Python은 많은 내장 모듈을 제공합니다.

### math 모듈

수학 함수를 제공합니다.

```python
import math

print(math.pi)        # 3.141592653589793
print(math.sqrt(16))  # 4.0
print(math.pow(2, 3)) # 8.0
```

### datetime 모듈

날짜와 시간을 다룹니다.

```python
from datetime import datetime, date

# 현재 날짜와 시간
now = datetime.now()
print(now)  # 2024-01-15 10:30:45.123456

# 날짜만
today = date.today()
print(today)  # 2024-01-15

# 날짜 포맷팅
formatted = now.strftime("%Y년 %m월 %d일 %H시 %M분")
print(formatted)  # 2024년 01월 15일 10시 30분
```

### random 모듈

난수를 생성합니다.

```python
import random

# 0과 1 사이의 난수
print(random.random())

# 정수 범위의 난수
print(random.randint(1, 10))

# 리스트에서 랜덤 선택
fruits = ["사과", "바나나", "오렌지"]
print(random.choice(fruits))

# 리스트 섞기
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)
```

### os 모듈

운영체제 관련 기능을 제공합니다.

```python
import os

# 현재 작업 디렉토리
print(os.getcwd())

# 환경 변수
print(os.getenv("PATH"))

# 파일 존재 확인
print(os.path.exists("file.txt"))

# 파일 경로 조작
path = os.path.join("folder", "file.txt")
print(path)  # folder/file.txt (또는 folder\file.txt)
```

## 모듈 생성 예제

### 예제 1: 계산기 모듈

```python
# calculator.py
def add(a, b):
    """두 수를 더합니다."""
    return a + b

def subtract(a, b):
    """두 수를 뺍니다."""
    return a - b

def multiply(a, b):
    """두 수를 곱합니다."""
    return a * b

def divide(a, b):
    """두 수를 나눕니다."""
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b
```

```python
# main.py
import calculator

result1 = calculator.add(10, 5)
result2 = calculator.subtract(10, 5)
result3 = calculator.multiply(10, 5)
result4 = calculator.divide(10, 5)

print(result1, result2, result3, result4)  # 15 5 50 2.0
```

### 예제 2: 유틸리티 모듈

```python
# utils.py
def format_currency(amount):
    """금액을 포맷팅합니다."""
    return f"{amount:,}원"

def validate_email(email):
    """이메일 형식을 검증합니다."""
    return "@" in email and "." in email

def get_timestamp():
    """현재 타임스탬프를 반환합니다."""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
```

```python
# main.py
from utils import format_currency, validate_email, get_timestamp

print(format_currency(1000000))  # 1,000,000원
print(validate_email("test@example.com"))  # True
print(get_timestamp())  # 2024-01-15 10:30:45
```

## __name__ == "__main__" 패턴

모듈이 직접 실행될 때와 import될 때를 구분하는 패턴입니다.

```python
# math_utils.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# 이 파일이 직접 실행될 때만 실행됨
if __name__ == "__main__":
    print("math_utils 모듈이 직접 실행되었습니다.")
    print(add(3, 5))
    print(multiply(3, 5))
```

```python
# main.py
import math_utils

# math_utils의 __main__ 블록은 실행되지 않음
result = math_utils.add(10, 20)
print(result)  # 30
```

### 사용 예시

```python
# calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# 테스트 코드
if __name__ == "__main__":
    # 모듈을 직접 실행할 때만 테스트 실행
    assert add(2, 3) == 5
    assert subtract(5, 2) == 3
    print("모든 테스트 통과!")
```

## 모듈 검색 경로

Python은 다음 순서로 모듈을 검색합니다:

1. 현재 디렉토리
2. PYTHONPATH 환경 변수에 지정된 디렉토리
3. Python 설치 디렉토리의 표준 라이브러리
4. site-packages 디렉토리 (설치된 패키지)

```python
import sys

# 모듈 검색 경로 확인
print(sys.path)

# 경로 추가
sys.path.append("/custom/path")
```

## 모듈 재로드

모듈을 수정한 후 다시 로드하려면 `importlib`를 사용합니다.

```python
import importlib
import math_utils

# 모듈 수정 후
importlib.reload(math_utils)
```

## dir() 함수

모듈이나 객체의 속성 목록을 확인할 수 있습니다.

```python
import math_utils

# 모듈의 모든 속성 확인
print(dir(math_utils))

# 특정 속성만 필터링
attributes = [attr for attr in dir(math_utils) if not attr.startswith("_")]
print(attributes)  # ['add', 'multiply', 'PI']
```

## 실습 예제

### 예제 1: 사용자 관리 모듈

```python
# user_manager.py
users = []

def add_user(name, email):
    """사용자를 추가합니다."""
    user = {"name": name, "email": email}
    users.append(user)
    return user

def get_user(name):
    """이름으로 사용자를 찾습니다."""
    for user in users:
        if user["name"] == name:
            return user
    return None

def list_users():
    """모든 사용자를 반환합니다."""
    return users.copy()

if __name__ == "__main__":
    # 테스트
    add_user("홍길동", "hong@example.com")
    add_user("김철수", "kim@example.com")
    print(list_users())
```

```python
# main.py
from user_manager import add_user, get_user, list_users

add_user("이영희", "lee@example.com")
user = get_user("이영희")
print(user)  # {'name': '이영희', 'email': 'lee@example.com'}
```

### 예제 2: 설정 모듈

```python
# config.py
DATABASE_URL = "postgresql://localhost/mydb"
DEBUG = True
SECRET_KEY = "my-secret-key"

# 환경에 따라 설정 변경
import os
if os.getenv("ENVIRONMENT") == "production":
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY")
```

```python
# main.py
import config

print(config.DATABASE_URL)
print(config.DEBUG)
```

## 요약

### Python
- **모듈**: Python 코드가 담긴 `.py` 파일
- **import**: `import module` 형식
- **from ... import**: `from module import item` 형식
- **as 별칭**: 모듈이나 항목에 별칭 지정
- **__name__ == "__main__"**: 모듈이 직접 실행될 때만 코드 실행
- **내장 모듈**: `math`, `datetime`, `random`, `os` 등
- **dir()**: 모듈의 속성 목록 확인

### JavaScript
- **모듈**: JavaScript 코드가 담긴 `.js` 파일
- **CommonJS**: `require()` 사용 (Node.js)
- **ES6 모듈**: `import`/`export` 사용 (브라우저/Node.js)
- **named import**: `import { item } from module`
- **default import**: `import item from module`
- **as 별칭**: `import { item as alias } from module`
- **내장 모듈**: `fs`, `path`, `http` 등 (Node.js)

### 주요 차이점
- Python은 단일 모듈 시스템을 사용하지만, JavaScript는 CommonJS와 ES6 모듈 두 가지를 지원
- Python은 파일 확장자 없이 import하지만, JavaScript ES6 모듈은 확장자가 필요할 수 있음
- Python의 `__name__ == "__main__"`은 JavaScript에 직접 대응되는 개념이 없음
- JavaScript는 `export` 키워드로 명시적으로 내보내야 하지만, Python은 파일의 모든 항목이 자동으로 export됨

