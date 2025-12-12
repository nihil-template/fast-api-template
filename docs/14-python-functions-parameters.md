# Python 기초: 함수 매개변수

> JavaScript 비교는 참고용입니다. Python만 실습하려면 Python 예제와 설명 위주로 읽고, `notebooks/04-python-functions.ipynb`와 `training/4.functions.py`에서 함수를 직접 작성해 보세요.

## 개요

Python 함수의 다양한 매개변수 사용법에 대해 학습합니다. 기본값, 키워드 인자, 가변 인자 등을 활용하면 더 유연한 함수를 만들 수 있습니다.

## 기본값이 있는 매개변수

매개변수에 기본값을 설정할 수 있습니다.

**Python 예제:**
```python
def greet(name, greeting="안녕하세요"):
    print(f"{greeting}, {name}님!")

greet("홍길동")  # 안녕하세요, 홍길동님!
greet("홍길동", "반갑습니다")  # 반갑습니다, 홍길동님!

# 기본값이 있는 매개변수는 뒤에 위치해야 함
def calculate(price, discount=0.1, tax=0.1):  # 올바름
    return price * (1 - discount) * (1 + tax)

# def calculate(discount=0.1, price):  # 오류!
```

## 키워드 인자

함수를 호출할 때 매개변수 이름을 명시할 수 있습니다.

**Python 예제:**
```python
def introduce(name, age, city):
    print(f"이름: {name}, 나이: {age}, 도시: {city}")

# 위치 인자로 호출
introduce("홍길동", 25, "서울")

# 키워드 인자로 호출
introduce(name="홍길동", age=25, city="서울")
introduce(city="서울", name="홍길동", age=25)  # 순서 상관없음
```

## 가변 인자 (*args)

개수가 정해지지 않은 인자를 받을 수 있습니다.

**Python 예제:**
```python
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

# *args는 튜플로 전달됨
def print_args(*args):
    print(type(args))  # <class 'tuple'>
    print(args)

print_args(1, 2, 3)  # (1, 2, 3)
```

## 키워드 가변 인자 (**kwargs)

키워드 인자를 딕셔너리로 받을 수 있습니다.

**Python 예제:**
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="홍길동", age=25, city="서울")
# 출력:
# name: 홍길동
# age: 25
# city: 서울

# **kwargs는 딕셔너리로 전달됨
def print_kwargs(**kwargs):
    print(type(kwargs))  # <class 'dict'>
    print(kwargs)

print_kwargs(a=1, b=2)  # {'a': 1, 'b': 2}
```

## 매개변수 조합

여러 종류의 매개변수를 함께 사용할 수 있습니다. 순서는 중요합니다.

```python
def complex_function(required, default="기본값", *args, **kwargs):
    print(f"필수: {required}")
    print(f"기본값: {default}")
    print(f"가변 인자: {args}")
    print(f"키워드 인자: {kwargs}")

complex_function("필수값", "변경값", 1, 2, 3, name="홍길동", age=25)
# 출력:
# 필수: 필수값
# 기본값: 변경값
# 가변 인자: (1, 2, 3)
# 키워드 인자: {'name': '홍길동', 'age': 25}
```

## 실습 예제

```python
# 가변 인자 활용
def average(*numbers):
    """여러 숫자의 평균을 계산"""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

print(average(1, 2, 3))           # 2.0
print(average(10, 20, 30, 40, 50)) # 30.0

# 키워드 인자 활용
def create_user(**user_info):
    """사용자 정보를 딕셔너리로 반환"""
    return user_info

user = create_user(
    name="홍길동",
    age=25,
    email="hong@example.com",
    city="서울"
)
print(user)
```

## 요약

### Python
- **기본값**: `매개변수=기본값` 형식
- **키워드 인자**: 함수 호출 시 매개변수 이름 명시
- **가변 인자**: `*args`로 튜플로 받음
- **키워드 가변 인자**: `**kwargs`로 딕셔너리로 받음
- **순서**: 필수 → 기본값 → *args → **kwargs

## 직접 해보기
1. 기본값이 있는 매개변수를 사용해 인사말 함수를 작성하세요.
2. `*args`를 사용해 여러 숫자의 합을 계산하는 함수를 작성하세요.
3. `**kwargs`를 사용해 사용자 정보를 받아 출력하는 함수를 작성하세요.

