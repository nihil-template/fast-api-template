# Python 기초: 클래스와 객체지향 프로그래밍

## 개요

클래스는 객체지향 프로그래밍(OOP)의 기본 단위입니다. 클래스를 통해 관련된 데이터와 함수를 하나로 묶어 관리할 수 있습니다. Python과 JavaScript 모두 클래스를 지원하지만, JavaScript는 ES6부터 클래스를 지원하며, 내부적으로는 프로토타입 기반입니다.

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

**JavaScript 예제:**
```javascript
// 클래스 정의 (ES6+)
class Person {
    // 빈 클래스
}

// 인스턴스 생성
let person1 = new Person();
let person2 = new Person();

console.log(person1.constructor.name);  // "Person"
```

**비교 설명:**
- Python은 `class` 키워드로 클래스를 정의합니다.
- JavaScript는 ES6부터 `class` 키워드를 지원하지만, 내부적으로는 프로토타입 기반입니다.
- Python은 `new` 키워드 없이 인스턴스를 생성하지만, JavaScript는 `new` 키워드가 필요합니다.
- Python은 `type()`으로 타입을 확인하지만, JavaScript는 `constructor.name`을 사용합니다.

### __init__ 메서드 / constructor

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

**JavaScript 예제:**
```javascript
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
}

// 인스턴스 생성
let person = new Person("홍길동", 25);
console.log(person.name);  // 홍길동
console.log(person.age);   // 25
```

**비교 설명:**
- Python은 `__init__` 메서드로 초기화하고, `self`를 첫 번째 매개변수로 사용합니다.
- JavaScript는 `constructor` 메서드로 초기화하고, `this`를 사용합니다.
- Python은 `self.속성`으로 인스턴스 변수를 설정하고, JavaScript는 `this.속성`을 사용합니다.
- Python은 `new` 키워드 없이 호출하지만, JavaScript는 `new` 키워드가 필수입니다.

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

**JavaScript 예제:**
```javascript
class Person {
    constructor(name) {
        this.name = name;  // this.name은 인스턴스 변수
    }
    
    getName() {
        return this.name;  // this를 통해 인스턴스 변수 접근
    }
}

let person = new Person("홍길동");
console.log(person.getName());  // 홍길동
```

**비교 설명:**
- Python은 `self`를 명시적으로 첫 번째 매개변수로 받습니다.
- JavaScript는 `this`를 암묵적으로 사용하며, 매개변수로 받지 않습니다.
- Python의 `self`는 명시적이어서 더 명확하지만, JavaScript의 `this`는 더 간결합니다.
- JavaScript의 `this`는 호출 컨텍스트에 따라 바뀔 수 있어 주의가 필요합니다 (화살표 함수는 렉시컬 `this`).

## 인스턴스 변수와 클래스 변수

### 인스턴스 변수

각 인스턴스마다 독립적인 변수입니다.

```python
class Person:
    def __init__(self, name):
        self.name = name  # 인스턴스 변수

person1 = Person("홍길동")
person2 = Person("김철수")

print(person1.name)  # 홍길동
print(person2.name)  # 김철수 (독립적)
```

### 클래스 변수

모든 인스턴스가 공유하는 변수입니다.

```python
class Person:
    species = "Homo sapiens"  # 클래스 변수
    
    def __init__(self, name):
        self.name = name

person1 = Person("홍길동")
person2 = Person("김철수")

print(person1.species)  # Homo sapiens
print(person2.species)  # Homo sapiens
print(Person.species)   # Homo sapiens (클래스로 직접 접근)
```

## 클래스 메서드와 정적 메서드

### 클래스 메서드 (@classmethod)

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

### 정적 메서드 (@staticmethod)

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

## 상속

기존 클래스를 확장하여 새로운 클래스를 만들 수 있습니다.

### 기본 상속

```python
# 부모 클래스
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name}가 소리를 냅니다."

# 자식 클래스
class Dog(Animal):
    def speak(self):
        return f"{self.name}가 멍멍 짖습니다."

class Cat(Animal):
    def speak(self):
        return f"{self.name}가 야옹 웁니다."

dog = Dog("바둑이")
cat = Cat("나비")

print(dog.speak())  # 바둑이가 멍멍 짖습니다.
print(cat.speak())  # 나비가 야옹 웁니다.
```

### super() 함수

부모 클래스의 메서드를 호출할 수 있습니다.

```python
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "개")  # 부모 클래스의 __init__ 호출
        self.breed = breed
    
    def info(self):
        return f"{self.name}는 {self.species} 종의 {self.breed}입니다."

dog = Dog("바둑이", "골든 리트리버")
print(dog.info())  # 바둑이는 개 종의 골든 리트리버입니다.
```

### 다중 상속

여러 부모 클래스로부터 상속받을 수 있습니다.

```python
class Flyable:
    def fly(self):
        return "날 수 있습니다."

class Swimmable:
    def swim(self):
        return "수영할 수 있습니다."

class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name

duck = Duck("도날드")
print(duck.fly())   # 날 수 있습니다.
print(duck.swim())  # 수영할 수 있습니다.
```

## 특수 메서드 (Magic Methods)

특정 연산이나 함수 호출 시 자동으로 실행되는 메서드입니다.

### __str__과 __repr__

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

### __len__과 __eq__

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

## 접근 제어 (캡슐화)

Python은 접근 제어자를 제공하지 않지만, 관례를 통해 구현합니다.

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

## 실습 예제

### 예제 1: 은행 계좌 클래스

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"{amount}원 입금되었습니다. 잔액: {self.__balance}원"
        return "입금 금액은 0보다 커야 합니다."
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            return f"{amount}원 출금되었습니다. 잔액: {self.__balance}원"
        return "출금할 수 없습니다."
    
    def get_balance(self):
        return self.__balance
    
    def __str__(self):
        return f"계좌 소유자: {self.owner}, 잔액: {self.__balance}원"

account = BankAccount("홍길동", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account)
```

### 예제 2: 상속 활용

```python
class Shape:
    def __init__(self, color):
        self.color = color
    
    def area(self):
        raise NotImplementedError("서브클래스에서 구현해야 합니다.")

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2

rect = Rectangle("빨강", 5, 3)
circle = Circle("파랑", 4)

print(f"사각형 면적: {rect.area()}")  # 사각형 면적: 15
print(f"원 면적: {circle.area()}")    # 원 면적: 50.26544
```

## 요약

### Python
- **클래스**: `class` 키워드로 정의
- **인스턴스**: `new` 없이 생성 (`Person()`)
- **__init__**: 인스턴스 초기화 메서드
- **self**: 인스턴스 자신을 가리키는 명시적 참조
- **인스턴스 변수**: 각 인스턴스마다 독립적인 변수
- **클래스 변수**: 모든 인스턴스가 공유하는 변수
- **상속**: `class Child(Parent):` 형식
- **super()**: 부모 클래스의 메서드 호출
- **특수 메서드**: `__str__`, `__repr__`, `__len__` 등
- **프로퍼티**: `@property` 데코레이터로 getter/setter 구현

### JavaScript
- **클래스**: ES6+ `class` 키워드로 정의 (프로토타입 기반)
- **인스턴스**: `new` 키워드로 생성 (`new Person()`)
- **constructor**: 인스턴스 초기화 메서드
- **this**: 인스턴스 자신을 가리키는 암묵적 참조
- **인스턴스 변수**: 각 인스턴스마다 독립적인 변수
- **정적 속성**: `static` 키워드로 클래스 변수
- **상속**: `class Child extends Parent` 형식
- **super**: 부모 클래스의 메서드 호출
- **getter/setter**: `get`/`set` 키워드로 프로퍼티 구현

### 주요 차이점
- Python은 `self`를 명시적으로 받지만, JavaScript는 `this`를 암묵적으로 사용
- Python은 `new` 없이 인스턴스를 생성하지만, JavaScript는 `new`가 필수
- Python의 특수 메서드는 JavaScript의 심볼 메서드와 유사한 역할
- JavaScript는 프로토타입 기반이지만, 클래스 문법으로 더 명확하게 표현 가능

