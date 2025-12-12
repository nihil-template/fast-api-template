# Python 기초: 클래스 상속

> JavaScript 비교는 참고용입니다. Python 클래스를 중심으로 학습하려면 Python 예제만 실행해도 충분합니다.

## 개요

상속은 기존 클래스를 확장하여 새로운 클래스를 만드는 방법입니다. 코드 재사용과 확장성을 높일 수 있습니다.

## 기본 상속

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

## super() 함수

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

## 다중 상속

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

## 요약

### Python
- **상속**: `class Child(Parent):` 형식
- **super()**: 부모 클래스의 메서드 호출
- **다중 상속**: 여러 부모 클래스로부터 상속 가능

## 직접 해보기
1. 상속을 이용해 `Employee(Person)` 클래스에서 `salary`를 관리하는 메서드를 구현해 보세요.
2. `super()`를 사용해 부모 클래스의 메서드를 호출하는 예제를 작성하세요.

