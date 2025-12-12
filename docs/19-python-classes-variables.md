# Python 기초: 클래스 변수와 인스턴스 변수

> JavaScript 비교는 참고용입니다. Python 클래스를 중심으로 학습하려면 Python 예제만 실행해도 충분합니다.

## 개요

클래스에는 인스턴스 변수와 클래스 변수 두 가지가 있습니다. 각각의 특징과 사용법을 학습합니다.

## 인스턴스 변수

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

## 클래스 변수

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

## 요약

### Python
- **인스턴스 변수**: 각 인스턴스마다 독립적인 변수 (`self.변수명`)
- **클래스 변수**: 모든 인스턴스가 공유하는 변수 (클래스 내부에 직접 정의)

## 직접 해보기
1. 인스턴스 변수와 클래스 변수를 모두 사용하는 클래스를 작성하세요.
2. 클래스 변수를 수정했을 때 모든 인스턴스에 영향을 주는지 확인하세요.

