# Python 기초: 클래스 기본

> JavaScript 비교는 참고용입니다. Python 클래스를 중심으로 학습하려면 Python 예제만 실행해도 충분합니다. `notebooks/07-python-classes-oop.ipynb`와 `training/7.classes.py`에서 클래스를 직접 정의해 보세요.

## 개요

클래스는 객체지향 프로그래밍(OOP)의 기본 단위입니다. 클래스를 통해 관련된 데이터와 함수를 하나로 묶어 관리할 수 있습니다.

## 클래스 정의

### 기본 클래스

**Python 예제:**
```python
# 클래스 정의
class Person:
    pass  # 빈 클래스

# 인스턴스 생성
person1 = Person()
person2 = Person()

print(type(person1))  # <class '__main__.Person'>
```

### __init__ 메서드

인스턴스가 생성될 때 자동으로 호출되는 초기화 메서드입니다.

**Python 예제:**
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 인스턴스 생성
person = Person("홍길동", 25)
print(person.name)  # 홍길동
print(person.age)   # 25
```

### 인스턴스 메서드

클래스 내부에 정의된 함수로, 인스턴스를 통해 호출합니다.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"안녕하세요, 저는 {self.name}이고 {self.age}세입니다."
    
    def have_birthday(self):
        self.age += 1
        return f"{self.name}의 생일입니다! 나이가 {self.age}세가 되었습니다."

person = Person("홍길동", 25)
print(person.introduce())      # 안녕하세요, 저는 홍길동이고 25세입니다.
print(person.have_birthday())  # 홍길동의 생일입니다! 나이가 26세가 되었습니다.
```

## self vs this

**Python 예제:**
```python
class Person:
    def __init__(self, name):
        self.name = name  # self.name은 인스턴스 변수
    
    def get_name(self):
        return self.name  # self를 통해 인스턴스 변수 접근

person = Person("홍길동")
print(person.get_name())  # 홍길동
```

**비교 설명:**
- Python은 `self`를 명시적으로 첫 번째 매개변수로 받습니다.
- JavaScript는 `this`를 암묵적으로 사용하며, 매개변수로 받지 않습니다.
- Python의 `self`는 명시적이어서 더 명확합니다.

## 요약

### Python
- **클래스**: `class` 키워드로 정의
- **인스턴스**: `new` 없이 생성 (`Person()`)
- **__init__**: 인스턴스 초기화 메서드
- **self**: 인스턴스 자신을 가리키는 명시적 참조

## 직접 해보기
1. `Person` 클래스를 정의하고 이름과 나이를 받아 초기화하세요.
2. `introduce()` 메서드를 추가해 자기소개를 출력하세요.
3. `training/7.classes.py`를 실행해 보고 클래스를 직접 작성해 보세요.

