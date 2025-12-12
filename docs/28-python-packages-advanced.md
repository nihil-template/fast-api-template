# Python 기초: 패키지 고급

> JavaScript 비교는 참고용입니다. Python 패키지 구성을 체험하려면 Python 섹션만 따라도 충분합니다.

## 개요

패키지 배포, 설치, `__all__` 변수, 네임스페이스 등 패키지의 고급 기능에 대해 학습합니다.

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

## 패키지 배포 준비

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

## 요약

### Python
- **__all__**: `from package import *`로 import할 항목 지정
- **pip**: 패키지 관리자
- **pyproject.toml**: 패키지 배포 설정
- **네임스페이스**: 이름 충돌 방지

## 직접 해보기
1. `__all__` 목록에 함수를 추가/삭제하면서 `from my_package import *` 결과가 어떻게 달라지는지 확인하세요.
2. `pyproject.toml`을 작성해 패키지를 배포 준비하세요.

