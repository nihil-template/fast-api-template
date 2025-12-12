# Python 기초: 함수 문서화와 타입 힌트

> JavaScript 비교는 참고용입니다. Python만 실습하려면 Python 예제와 설명 위주로 읽고, `notebooks/04-python-functions.ipynb`와 `training/4.functions.py`에서 함수를 직접 작성해 보세요.

## 개요

함수의 목적과 사용법을 설명하는 문서화(Docstring)와 타입 힌트에 대해 학습합니다.

## 함수 문서화 (Docstring)

함수의 목적과 사용법을 설명하는 문자열입니다.

```python
def add(a, b):
    """
    두 숫자를 더하는 함수
    
    Args:
        a (int): 첫 번째 숫자
        b (int): 두 번째 숫자
    
    Returns:
        int: 두 숫자의 합
    """
    return a + b

# 도움말 확인
help(add)
print(add.__doc__)
```

## 타입 힌트 (Type Hints)

함수의 매개변수와 반환값의 타입을 명시할 수 있습니다. (Python 3.5+)

```python
def add(a: int, b: int) -> int:
    """두 정수를 더하는 함수"""
    return a + b

def greet(name: str) -> str:
    """인사말을 반환하는 함수"""
    return f"안녕하세요, {name}님!"

# 타입 힌트는 강제되지 않지만, 코드 가독성과 IDE 지원에 도움
result: int = add(3, 5)
greeting: str = greet("홍길동")
```

## 요약

### Python
- **Docstring**: 함수 문서화 문자열
- **타입 힌트**: 매개변수와 반환값 타입 명시 (선택사항)
- 타입 힌트는 강제되지 않지만 코드 가독성과 IDE 지원에 도움

## 직접 해보기
1. 함수에 Docstring을 추가하고 `help()` 함수로 확인해 보세요.
2. 타입 힌트를 사용해 함수를 작성하고 IDE에서 자동완성이 작동하는지 확인하세요.

