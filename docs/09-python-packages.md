# Python 기초: 패키지

## 개요

패키지는 여러 모듈을 하나의 디렉토리로 묶어 관리하는 방법입니다. 패키지를 사용하면 대규모 프로젝트를 체계적으로 구성할 수 있습니다. Python의 패키지는 JavaScript의 npm 패키지와 유사하지만, 구조와 관리 방식에 차이가 있습니다.

## 패키지 구조

패키지는 `__init__.py` 파일이 있는 디렉토리입니다. (Python 3.3+에서는 선택사항이지만 명시하는 것이 좋습니다)

```
my_package/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
```

## __init__.py의 역할

`__init__.py` 파일은 디렉토리를 패키지로 인식하게 하며, 패키지 초기화 코드를 작성할 수 있습니다.

### 빈 __init__.py

```python
# my_package/__init__.py
# 빈 파일이어도 패키지로 인식됨
```

### __init__.py에서 import

패키지를 import할 때 자동으로 실행되는 코드를 작성할 수 있습니다.

```python
# my_package/__init__.py
from .module1 import function1
from .module2 import Class1

# 패키지 레벨에서 바로 사용 가능하도록
__all__ = ['function1', 'Class1']
```

## 패키지 Import 방법

### 기본 import

```python
# 패키지 전체 import
import my_package

# 패키지의 모듈 import
from my_package import module1

# 패키지의 모듈에서 특정 항목 import
from my_package.module1 import function1
```

### 예제 구조

```
calculator/
├── __init__.py
├── basic.py
├── advanced.py
└── utils.py
```

```python
# calculator/__init__.py
from .basic import add, subtract, multiply, divide
from .advanced import power, sqrt

__all__ = ['add', 'subtract', 'multiply', 'divide', 'power', 'sqrt']
```

```python
# calculator/basic.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")
    return a / b
```

```python
# calculator/advanced.py
def power(base, exponent):
    return base ** exponent

def sqrt(number):
    return number ** 0.5
```

```python
# main.py
# 방법 1: __init__.py에서 import한 항목 사용
from calculator import add, power

print(add(3, 5))    # 8
print(power(2, 3))  # 8

# 방법 2: 모듈 직접 import
from calculator import basic, advanced

print(basic.multiply(3, 5))      # 15
print(advanced.sqrt(16))         # 4.0
```

## 상대 Import vs 절대 Import

### 절대 Import

프로젝트 루트나 Python 경로 기준으로 import합니다.

```python
# 프로젝트 구조
project/
├── main.py
└── my_package/
    ├── __init__.py
    ├── module1.py
    └── subpackage/
        ├── __init__.py
        └── module2.py
```

```python
# main.py
from my_package import module1
from my_package.subpackage import module2
```

```python
# my_package/subpackage/module2.py
from my_package import module1  # 절대 import
```

### 상대 Import

현재 패키지 내에서 상대 경로로 import합니다.

```python
# my_package/subpackage/module2.py
from .. import module1        # 부모 패키지의 module1
from ..module1 import function1  # 부모 패키지의 module1에서 function1
from . import another_module  # 같은 패키지의 another_module
```

상대 import 기호:
- `.`: 현재 패키지
- `..`: 부모 패키지
- `...`: 조부모 패키지

## 패키지 예제

### 예제 1: 간단한 패키지

```
utils/
├── __init__.py
├── string_utils.py
├── math_utils.py
└── date_utils.py
```

```python
# utils/__init__.py
from .string_utils import capitalize_words, reverse_string
from .math_utils import calculate_average
from .date_utils import format_date

__all__ = [
    'capitalize_words',
    'reverse_string',
    'calculate_average',
    'format_date'
]
```

```python
# utils/string_utils.py
def capitalize_words(text):
    return text.title()

def reverse_string(text):
    return text[::-1]
```

```python
# utils/math_utils.py
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
```

```python
# utils/date_utils.py
from datetime import datetime

def format_date(date_obj, format_str="%Y-%m-%d"):
    return date_obj.strftime(format_str)
```

```python
# main.py
from utils import capitalize_words, calculate_average, format_date
from datetime import datetime

text = capitalize_words("hello world")
print(text)  # Hello World

avg = calculate_average([1, 2, 3, 4, 5])
print(avg)  # 3.0

date_str = format_date(datetime.now())
print(date_str)  # 2024-01-15
```

### 예제 2: 중첩 패키지

```
ecommerce/
├── __init__.py
├── products/
│   ├── __init__.py
│   ├── product.py
│   └── category.py
├── orders/
│   ├── __init__.py
│   └── order.py
└── utils/
    ├── __init__.py
    └── validators.py
```

```python
# ecommerce/__init__.py
from .products import Product, Category
from .orders import Order

__all__ = ['Product', 'Category', 'Order']
```

```python
# ecommerce/products/__init__.py
from .product import Product
from .category import Category

__all__ = ['Product', 'Category']
```

```python
# ecommerce/products/product.py
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
```

```python
# ecommerce/orders/order.py
from ..products import Product

class Order:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
```

```python
# main.py
from ecommerce import Product, Order

product = Product("노트북", 1000000)
order = Order(product, 2)
```

## 패키지 배포 준비

### setup.py (구식 방법)

```python
# setup.py
from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # 의존성 목록
    ],
)
```

### pyproject.toml (현대적 방법)

```toml
# pyproject.toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "my_package"
version = "0.1.0"
description = "My package description"
requires-python = ">=3.8"
dependencies = [
    # 의존성 목록
]
```

## 패키지 설치

### 개발 모드 설치

패키지를 개발 모드로 설치하면 코드 수정이 즉시 반영됩니다.

```bash
# pip install -e .
pip install -e /path/to/package
```

### 일반 설치

```bash
pip install /path/to/package
```

## __all__ 변수

패키지나 모듈에서 `from package import *`로 import할 때 어떤 항목을 가져올지 지정합니다.

```python
# my_package/__init__.py
from .module1 import function1, function2, _private_function

# __all__이 없으면 모든 공개 이름이 import됨
# __all__이 있으면 지정된 항목만 import됨
__all__ = ['function1', 'function2']
# _private_function은 import되지 않음
```

## 패키지 네임스페이스

패키지는 네임스페이스를 제공하여 이름 충돌을 방지합니다.

```python
# 두 패키지에 같은 이름의 함수가 있어도 충돌 없음
from package1 import calculate
from package2 import calculate

# 별칭 사용
from package1 import calculate as calc1
from package2 import calculate as calc2
```

## 실습 예제

### 예제: 완전한 패키지 구조

```
my_project/
├── main.py
└── myapp/
    ├── __init__.py
    ├── models/
    │   ├── __init__.py
    │   └── user.py
    ├── services/
    │   ├── __init__.py
    │   └── user_service.py
    └── utils/
        ├── __init__.py
        └── helpers.py
```

```python
# myapp/__init__.py
from .models import User
from .services import UserService

__version__ = "1.0.0"
__all__ = ['User', 'UserService']
```

```python
# myapp/models/__init__.py
from .user import User

__all__ = ['User']
```

```python
# myapp/models/user.py
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
```

```python
# myapp/services/user_service.py
from ..models import User

class UserService:
    def create_user(self, name, email):
        return User(name, email)
```

```python
# main.py
from myapp import User, UserService

service = UserService()
user = service.create_user("홍길동", "hong@example.com")
print(user.name, user.email)
```

## 요약

### Python
- **패키지**: `__init__.py` 파일이 있는 디렉토리
- **__init__.py**: 패키지 초기화 및 import 제어
- **절대 import**: 프로젝트 루트 기준으로 import
- **상대 import**: 현재 패키지 기준으로 상대 경로로 import (`.`, `..` 사용)
- **__all__**: `from package import *`로 import할 항목 지정
- **pip**: 패키지 관리자
- **setup.py / pyproject.toml**: 패키지 배포 설정

### JavaScript
- **패키지**: `package.json` 파일이 있는 디렉토리
- **npm/yarn**: 패키지 관리자
- **node_modules**: 설치된 패키지 저장 위치
- **package.json**: 패키지 메타데이터 및 의존성 관리
- **모듈 해석**: Node.js는 `node_modules`에서 자동으로 모듈을 찾음
- **상대 경로**: `./`, `../`로 상대 경로 import

### 주요 차이점
- Python은 `__init__.py`로 패키지를 식별하지만, JavaScript는 `package.json`으로 식별
- Python은 `pip`로 패키지를 관리하지만, JavaScript는 `npm`/`yarn` 사용
- Python의 `setup.py`/`pyproject.toml`은 JavaScript의 `package.json`과 유사한 역할
- Python은 가상 환경(`venv`)을 사용하지만, JavaScript는 `node_modules`를 프로젝트별로 관리
- Python의 상대 import는 JavaScript의 상대 경로 import와 유사하지만 문법이 다름

