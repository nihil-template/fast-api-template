# Python 기초: 접근 제어와 프로퍼티

> JavaScript 비교는 참고용입니다. Python 클래스를 중심으로 학습하려면 Python 예제만 실행해도 충분합니다.

## 개요

Python은 접근 제어자를 제공하지 않지만, 관례를 통해 구현합니다. 또한 프로퍼티를 사용해 getter와 setter를 Python스럽게 구현할 수 있습니다.

## 접근 제어

### 공개 (Public)

기본적으로 모든 멤버는 공개입니다.

```python
class Person:
    def __init__(self, name):
        self.name = name  # 공개 변수

person = Person("홍길동")
print(person.name)  # 접근 가능
```

### 보호 (Protected)

언더스코어 하나(`_`)로 시작하는 멤버는 보호된 것으로 간주합니다.

```python
class Person:
    def __init__(self, name):
        self._name = name  # 보호된 변수 (관례상)
    
    def get_name(self):
        return self._name

person = Person("홍길동")
print(person._name)      # 접근 가능하지만 권장하지 않음
print(person.get_name()) # 권장 방법
```

### 비공개 (Private)

언더스코어 두 개(`__`)로 시작하는 멤버는 비공개로 간주합니다.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 비공개 변수
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age > 0:
            self.__age = age

person = Person("홍길동", 25)
# print(person.__age)  # 오류! 직접 접근 불가
print(person.get_age())  # 25 (메서드로 접근)
```

## 프로퍼티 (Property)

getter와 setter를 더 Python스럽게 구현할 수 있습니다.

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("나이는 0 이상이어야 합니다.")
        self._age = value

person = Person("홍길동", 25)
print(person.age)      # 25 (getter 호출)
person.age = 30        # setter 호출
print(person.age)      # 30
# person.age = -5      # ValueError 발생
```

## 요약

### Python
- **공개**: 기본적으로 모든 멤버는 공개
- **보호**: `_변수명` (관례상)
- **비공개**: `__변수명` (네임 맹글링)
- **프로퍼티**: `@property` 데코레이터로 getter/setter 구현

## 직접 해보기
1. 비공개 변수를 사용하는 클래스를 작성하고 getter/setter를 구현하세요.
2. `@property`를 사용해 프로퍼티를 구현하세요.

