# Python 기초: 모듈 기본

> JavaScript 비교는 참고용입니다. Python 모듈 사용에 집중하려면 Python 예제만 실행해도 됩니다. `notebooks/08-python-modules-import.ipynb`와 `training/8.modules.py`를 통해 모듈을 직접 작성하고 import하는 연습을 하세요.

## 개요

모듈은 Python 코드를 파일 단위로 구성하는 방법입니다. 코드를 재사용하고 구조화하기 위해 모듈을 사용합니다.

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

```python
# math_utils.py 파일이 같은 디렉토리에 있다고 가정
import math_utils

result = math_utils.add(3, 5)
print(result)  # 8

print(math_utils.PI)  # 3.14159
```

### from ... import

모듈에서 특정 항목만 가져옵니다.

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

## 모듈 생성 예제

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

## 요약

### Python
- **모듈**: Python 코드가 담긴 `.py` 파일
- **import**: `import module` 형식
- **from ... import**: `from module import item` 형식
- **as 별칭**: 모듈이나 항목에 별칭 지정

## 직접 해보기
1. 간단한 모듈을 만들고 다른 파일에서 import해 사용하세요.
2. `from ... import`를 사용해 특정 함수만 가져와 사용하세요.

