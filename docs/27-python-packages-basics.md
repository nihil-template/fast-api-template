# Python 기초: 패키지 기본

> JavaScript 비교는 참고용입니다. Python 패키지 구성을 체험하려면 Python 섹션만 따라도 충분합니다. `notebooks/09-python-packages.ipynb`, `training/my_package/`, `training/9.packages.py`를 열어 실제 패키지를 import하는 과정을 연습하세요.

## 개요

패키지는 여러 모듈을 하나의 디렉토리로 묶어 관리하는 방법입니다. 패키지를 사용하면 대규모 프로젝트를 체계적으로 구성할 수 있습니다.

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

## 상대 Import vs 절대 Import

### 절대 Import

프로젝트 루트나 Python 경로 기준으로 import합니다.

```python
# main.py
from my_package import module1
from my_package.subpackage import module2
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

## 요약

### Python
- **패키지**: `__init__.py` 파일이 있는 디렉토리
- **__init__.py**: 패키지 초기화 및 import 제어
- **절대 import**: 프로젝트 루트 기준으로 import
- **상대 import**: 현재 패키지 기준으로 상대 경로로 import (`.`, `..` 사용)

## 직접 해보기
1. 간단한 패키지를 만들고 `__init__.py`를 작성하세요.
2. 상대 import와 절대 import를 사용해 패키지 내 모듈을 import하세요.

