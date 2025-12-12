# Python 기초: 모듈 고급

> JavaScript 비교는 참고용입니다. Python 모듈 사용에 집중하려면 Python 예제만 실행해도 됩니다.

## 개요

모듈의 고급 기능인 `__name__ == "__main__"` 패턴, 모듈 검색 경로, 재로드, `dir()` 함수에 대해 학습합니다.

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

## 요약

### Python
- **__name__ == "__main__"**: 모듈이 직접 실행될 때만 코드 실행
- **sys.path**: 모듈 검색 경로
- **importlib.reload()**: 모듈 재로드
- **dir()**: 모듈의 속성 목록 확인

## 직접 해보기
1. `__name__ == "__main__"` 패턴을 사용해 모듈을 작성하세요.
2. `dir()` 함수를 사용해 모듈의 속성을 확인하세요.

