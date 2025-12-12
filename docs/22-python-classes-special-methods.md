# Python 기초: 특수 메서드 (Magic Methods)

> JavaScript 비교는 참고용입니다. Python 클래스를 중심으로 학습하려면 Python 예제만 실행해도 충분합니다.

## 개요

특수 메서드는 특정 연산이나 함수 호출 시 자동으로 실행되는 메서드입니다. `__str__`, `__repr__`, `__len__`, `__eq__` 등을 학습합니다.

## __str__과 __repr__

객체를 문자열로 표현합니다.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

person = Person("홍길동", 25)
print(str(person))   # Person(name=홍길동, age=25)
print(repr(person))  # Person('홍길동', 25)
```

## __len__과 __eq__

```python
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __len__(self):
        return self.pages
    
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title and self.pages == other.pages
        return False

book1 = Book("Python 기초", 300)
book2 = Book("Python 기초", 300)
book3 = Book("Python 고급", 300)

print(len(book1))      # 300
print(book1 == book2)  # True
print(book1 == book3)  # False
```

## 요약

### Python
- **__str__**: 사용자 친화적인 문자열 표현
- **__repr__**: 개발자용 문자열 표현
- **__len__**: `len()` 함수 지원
- **__eq__**: `==` 연산자 지원

## 직접 해보기
1. `__str__`과 `__repr__`을 구현한 클래스를 작성하세요.
2. `__len__`과 `__eq__`를 구현한 클래스를 작성하세요.

