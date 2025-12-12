# Python 기초: 함수

## 개요

함수는 코드를 재사용 가능한 단위로 묶는 방법입니다. 같은 작업을 여러 번 반복해야 할 때 함수를 사용하면 코드가 간결해지고 유지보수가 쉬워집니다. Python과 JavaScript 모두 함수를 지원하지만, 문법과 동작 방식에 차이가 있습니다.

## 함수 정의와 호출

### 기본 함수 정의

**Python 예제:**
```python
# 함수 정의
def greet():
    print("안녕하세요!")

# 함수 호출
greet()  # 안녕하세요!
```

**JavaScript 예제:**
```javascript
// 함수 선언
function greet() {
    console.log("안녕하세요!");
}

// 함수 호출
greet();  // 안녕하세요!

// 함수 표현식
const greet2 = function() {
    console.log("안녕하세요!");
};

// 화살표 함수
const greet3 = () => {
    console.log("안녕하세요!");
};
```

**비교 설명:**
- Python은 `def` 키워드로 함수를 정의합니다.
- JavaScript는 `function` 키워드, 함수 표현식, 화살표 함수 등 여러 방법을 제공합니다.
- Python은 들여쓰기로 함수 본문을 구분하고, JavaScript는 중괄호를 사용합니다.

### 매개변수가 있는 함수

**Python 예제:**
```python
# 매개변수 하나
def greet(name):
    print(f"안녕하세요, {name}님!")

greet("홍길동")  # 안녕하세요, 홍길동님!

# 매개변수 여러 개
def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add(3, 5)  # 3 + 5 = 8
```

**JavaScript 예제:**
```javascript
// 매개변수 하나
function greet(name) {
    console.log(`안녕하세요, ${name}님!`);
}

greet("홍길동");  // 안녕하세요, 홍길동님!

// 매개변수 여러 개
function add(a, b) {
    let result = a + b;
    console.log(`${a} + ${b} = ${result}`);
}

add(3, 5);  // 3 + 5 = 8

// 화살표 함수
const add2 = (a, b) => {
    return a + b;
};
```

**비교 설명:**
- 두 언어 모두 매개변수를 함수 정의에 명시합니다.
- Python은 f-string을 사용하고, JavaScript는 템플릿 리터럴을 사용합니다.
- JavaScript는 화살표 함수로 더 간결하게 작성할 수 있습니다.

### return 문

함수에서 값을 반환할 수 있습니다.

**Python 예제:**
```python
# 값을 반환하는 함수
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8

# 여러 값 반환 (튜플로 반환)
def get_name_and_age():
    return "홍길동", 25

name, age = get_name_and_age()
print(name, age)  # 홍길동 25
```

**JavaScript 예제:**
```javascript
// 값을 반환하는 함수
function add(a, b) {
    return a + b;
}

let result = add(3, 5);
console.log(result);  // 8

// 여러 값 반환 (배열 또는 객체로 반환)
function getNameAndAge() {
    return ["홍길동", 25];
}

let [name, age] = getNameAndAge();
console.log(name, age);  // 홍길동 25

// 객체로 반환
function getUserInfo() {
    return { name: "홍길동", age: 25 };
}

let { name: userName, age: userAge } = getUserInfo();
console.log(userName, userAge);  // 홍길동 25
```

**비교 설명:**
- 두 언어 모두 `return` 키워드로 값을 반환합니다.
- Python은 튜플로 여러 값을 반환하고 언패킹할 수 있습니다.
- JavaScript는 배열이나 객체로 여러 값을 반환하고 구조 분해 할당을 사용합니다.
- Python은 `return`이 없으면 `None`을 반환하고, JavaScript는 `undefined`를 반환합니다.

## 매개변수 종류

### 기본값이 있는 매개변수

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

**JavaScript 예제:**
```javascript
function greet(name, greeting = "안녕하세요") {
    console.log(`${greeting}, ${name}님!`);
}

greet("홍길동");  // 안녕하세요, 홍길동님!
greet("홍길동", "반갑습니다");  // 반갑습니다, 홍길동님!

// 기본값이 있는 매개변수는 뒤에 위치해야 함
function calculate(price, discount = 0.1, tax = 0.1) {
    return price * (1 - discount) * (1 + tax);
}

// function calculate(discount = 0.1, price) { }  // 오류!
```

**비교 설명:**
- 두 언어 모두 기본값을 매개변수에 직접 할당합니다.
- Python은 `매개변수=기본값` 형식이고, JavaScript도 동일합니다.
- 두 언어 모두 기본값이 있는 매개변수는 뒤에 위치해야 합니다.
- JavaScript는 ES6부터 기본 매개변수를 지원합니다.

### 키워드 인자

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

**JavaScript 예제:**
```javascript
// JavaScript는 키워드 인자를 직접 지원하지 않음
// 객체를 매개변수로 사용하여 유사한 효과 구현
function introduce({ name, age, city }) {
    console.log(`이름: ${name}, 나이: ${age}, 도시: ${city}`);
}

// 객체로 호출
introduce({ name: "홍길동", age: 25, city: "서울" });
introduce({ city: "서울", name: "홍길동", age: 25 });  // 순서 상관없음

// 기본값과 함께 사용
function introduce2({ name, age = 0, city = "알 수 없음" }) {
    console.log(`이름: ${name}, 나이: ${age}, 도시: ${city}`);
}
```

**비교 설명:**
- Python은 키워드 인자를 직접 지원합니다.
- JavaScript는 키워드 인자를 직접 지원하지 않지만, 객체 구조 분해를 사용하여 유사한 효과를 얻을 수 있습니다.
- Python의 키워드 인자가 더 명시적이고 간단합니다.
- JavaScript의 객체 방식은 더 유연하지만 코드가 더 길어집니다.

### 가변 인자 (*args)

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

**JavaScript 예제:**
```javascript
// rest 매개변수 사용
function sumAll(...args) {
    let total = 0;
    for (let num of args) {
        total += num;
    }
    return total;
}

console.log(sumAll(1, 2, 3));        // 6
console.log(sumAll(1, 2, 3, 4, 5));  // 15

// ...args는 배열로 전달됨
function printArgs(...args) {
    console.log(Array.isArray(args));  // true
    console.log(args);
}

printArgs(1, 2, 3);  // [1, 2, 3]
```

**비교 설명:**
- Python은 `*args`로 가변 인자를 받고, 튜플로 전달됩니다.
- JavaScript는 `...args` (rest 매개변수)로 가변 인자를 받고, 배열로 전달됩니다.
- 두 언어 모두 가변 인자를 사용하여 유연한 함수를 만들 수 있습니다.
- JavaScript의 rest 매개변수는 ES6부터 지원됩니다.

### 키워드 가변 인자 (**kwargs)

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

**JavaScript 예제:**
```javascript
// JavaScript는 **kwargs를 직접 지원하지 않음
// 객체를 매개변수로 사용
function printInfo(obj) {
    for (let [key, value] of Object.entries(obj)) {
        console.log(`${key}: ${value}`);
    }
}

printInfo({ name: "홍길동", age: 25, city: "서울" });
// 출력:
// name: 홍길동
// age: 25
// city: 서울

// 또는 rest 매개변수와 객체 구조 분해 조합
function printInfo2({ ...kwargs }) {
    console.log(typeof kwargs);  // "object"
    console.log(kwargs);
}
```

**비교 설명:**
- Python은 `**kwargs`로 키워드 인자를 딕셔너리로 받을 수 있습니다.
- JavaScript는 `**kwargs`를 직접 지원하지 않지만, 객체를 매개변수로 사용하여 유사한 효과를 얻을 수 있습니다.
- Python의 `**kwargs`가 더 간결하고 명시적입니다.

### 매개변수 조합

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

## 람다 함수 (익명 함수)

간단한 함수를 한 줄로 정의할 수 있습니다.

**Python 예제:**
```python
# 일반 함수
def square(x):
    return x ** 2

# 람다 함수
square_lambda = lambda x: x ** 2

print(square(5))          # 25
print(square_lambda(5))   # 25

# 람다 함수는 주로 다른 함수의 인자로 사용
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]
```

**JavaScript 예제:**
```javascript
// 일반 함수
function square(x) {
    return x ** 2;
}

// 화살표 함수 (람다와 유사)
const squareLambda = x => x ** 2;

console.log(square(5));          // 25
console.log(squareLambda(5));   // 25

// 화살표 함수는 주로 다른 함수의 인자로 사용
let numbers = [1, 2, 3, 4, 5];
let squared = numbers.map(x => x ** 2);
console.log(squared);  // [1, 4, 9, 16, 25]
```

**비교 설명:**
- Python은 `lambda` 키워드로 람다 함수를 정의합니다.
- JavaScript는 화살표 함수(`=>`)로 람다와 유사한 기능을 제공합니다.
- Python의 람다는 표현식 하나만 포함할 수 있지만, JavaScript의 화살표 함수는 여러 문을 포함할 수 있습니다.
- JavaScript의 화살표 함수는 `this` 바인딩이 다릅니다 (렉시컬 `this`).

## 스코프 (Scope)

변수가 어디에서 접근 가능한지를 결정합니다.

### 지역 변수와 전역 변수

```python
# 전역 변수
global_var = "전역 변수"

def my_function():
    # 지역 변수
    local_var = "지역 변수"
    print(global_var)  # 전역 변수 접근 가능
    print(local_var)

my_function()
# print(local_var)  # 오류! 지역 변수는 함수 밖에서 접근 불가
```

### global 키워드

함수 내에서 전역 변수를 수정할 때 사용합니다.

```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # 1

# global 없이 사용하면 지역 변수로 인식됨
def increment_wrong():
    count = count + 1  # 오류! 지역 변수 count가 정의되기 전에 사용

# increment_wrong()  # UnboundLocalError 발생
```

### nonlocal 키워드

중첩 함수에서 외부 함수의 변수를 수정할 때 사용합니다.

```python
def outer():
    x = "외부 함수"
    
    def inner():
        nonlocal x
        x = "내부 함수에서 수정"
        print(x)
    
    inner()
    print(x)

outer()
# 출력:
# 내부 함수에서 수정
# 내부 함수에서 수정
```

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

## 실습 예제

### 예제 1: 계산기 함수

```python
def calculator(a, b, operation="add"):
    """간단한 계산기 함수"""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "0으로 나눌 수 없습니다"
    else:
        return "지원하지 않는 연산입니다"

print(calculator(10, 5))              # 15
print(calculator(10, 5, "multiply")) # 50
print(calculator(10, 0, "divide"))   # 0으로 나눌 수 없습니다
```

### 예제 2: 가변 인자 활용

```python
def average(*numbers):
    """여러 숫자의 평균을 계산"""
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

print(average(1, 2, 3))           # 2.0
print(average(10, 20, 30, 40, 50)) # 30.0
```

### 예제 3: 키워드 인자 활용

```python
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
# {'name': '홍길동', 'age': 25, 'email': 'hong@example.com', 'city': '서울'}
```

### 예제 4: 람다 함수 활용

```python
# 리스트 정렬
students = [
    {"name": "홍길동", "score": 85},
    {"name": "김철수", "score": 92},
    {"name": "이영희", "score": 78}
]

# 점수로 정렬
sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)
for student in sorted_students:
    print(f"{student['name']}: {student['score']}")
```

## 요약

### Python
- **함수 정의**: `def` 키워드로 함수 정의
- **매개변수**: 위치 인자, 기본값, 키워드 인자 사용 가능
- **가변 인자**: `*args`로 개수 불명확한 인자, `**kwargs`로 키워드 인자 딕셔너리
- **return**: 함수에서 값 반환
- **람다 함수**: `lambda` 키워드로 간단한 함수를 한 줄로 정의
- **스코프**: `global`, `nonlocal`로 변수 스코프 제어
- **Docstring**: 함수 문서화
- **타입 힌트**: 매개변수와 반환값 타입 명시 (선택사항)

### JavaScript
- **함수 정의**: `function` 키워드, 함수 표현식, 화살표 함수
- **매개변수**: 위치 인자, 기본값 사용 가능 (ES6+)
- **가변 인자**: `...args` (rest 매개변수)로 배열로 받음
- **return**: 함수에서 값 반환
- **화살표 함수**: `=>`로 간단한 함수 정의, `this` 바인딩이 다름
- **스코프**: `let`, `const`는 블록 스코프, `var`는 함수 스코프
- **주석**: JSDoc으로 함수 문서화
- **타입**: TypeScript를 사용하면 타입 명시 가능

### 주요 차이점
- Python은 키워드 인자(`**kwargs`)를 직접 지원하지만, JavaScript는 객체 구조 분해를 사용
- Python의 `*args`는 튜플, JavaScript의 `...args`는 배열
- Python의 람다는 표현식 하나만, JavaScript의 화살표 함수는 여러 문 가능
- JavaScript의 화살표 함수는 `this` 바인딩이 렉시컬 스코프를 따름
- Python은 `global`, `nonlocal`로 스코프 제어, JavaScript는 변수 선언 키워드로 제어

