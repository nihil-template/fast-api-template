# Python 기초: 클래스 메서드와 정적 메서드

> JavaScript 비교는 참고용입니다. Python 클래스를 중심으로 학습하려면 Python 예제만 실행해도 충분합니다.

## 개요

클래스 메서드와 정적 메서드는 인스턴스 메서드와 다른 방식으로 동작합니다. 각각의 특징과 사용법을 학습합니다.

## 클래스 메서드 (@classmethod)

클래스 자체에 대한 작업을 수행합니다. 첫 번째 매개변수는 `cls`입니다.

```python
class Person:
    count = 0  # 클래스 변수
    
    def __init__(self, name):
        self.name = name
        Person.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count
    
    @classmethod
    def create_baby(cls, name):
        return cls(name)  # 새로운 인스턴스 생성

person1 = Person("홍길동")
person2 = Person("김철수")

print(Person.get_count())  # 2

baby = Person.create_baby("아기")
print(Person.get_count())  # 3
```

## 정적 메서드 (@staticmethod)

클래스나 인스턴스와 독립적인 함수입니다. `self`나 `cls`를 받지 않습니다.

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b

# 인스턴스 없이도 호출 가능
result1 = MathUtils.add(3, 5)
result2 = MathUtils.multiply(3, 5)

print(result1)  # 8
print(result2)  # 15

# 인스턴스를 통해서도 호출 가능
utils = MathUtils()
print(utils.add(2, 3))  # 5
```

## 요약

### Python
- **클래스 메서드**: `@classmethod` 데코레이터, 첫 번째 매개변수는 `cls`
- **정적 메서드**: `@staticmethod` 데코레이터, `self`나 `cls` 없음
- 클래스 메서드는 클래스 변수에 접근 가능, 정적 메서드는 독립적

## 직접 해보기
1. `@classmethod`를 사용해 인스턴스 개수를 세는 클래스를 작성하세요.
2. `@staticmethod`를 사용해 유틸리티 함수를 포함하는 클래스를 작성하세요.

