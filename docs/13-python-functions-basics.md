# Python 기초: 함수 기본

> JavaScript 비교는 참고용입니다. Python만 실습하려면 Python 예제와 설명 위주로 읽고, `notebooks/04-python-functions.ipynb`와 `training/4.functions.py`에서 함수를 직접 작성해 보세요.

## 개요

함수는 코드를 재사용 가능한 단위로 묶는 방법입니다. 같은 작업을 여러 번 반복해야 할 때 함수를 사용하면 코드가 간결해지고 유지보수가 쉬워집니다.

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

## return 문

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

## 실습 예제

```python
# 기본 함수 예제
def greet(name):
    return f"안녕하세요, {name}님!"

message = greet("홍길동")
print(message)  # 안녕하세요, 홍길동님!

# 계산 함수
def calculate(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    else:
        return None

result = calculate(10, 5, "add")
print(result)  # 15
```

## 요약

### Python
- **함수 정의**: `def` 키워드로 함수 정의
- **함수 호출**: 함수명과 괄호로 호출
- **return**: 함수에서 값 반환
- **여러 값 반환**: 튜플로 반환하고 언패킹

### JavaScript
- **함수 정의**: `function` 키워드, 함수 표현식, 화살표 함수
- **함수 호출**: 함수명과 괄호로 호출
- **return**: 함수에서 값 반환
- **여러 값 반환**: 배열이나 객체로 반환하고 구조 분해 할당

### 주요 차이점
- Python은 `def` 키워드만 사용, JavaScript는 여러 방법 제공
- Python은 들여쓰기로 블록 구분, JavaScript는 중괄호 사용
- Python은 튜플로 여러 값 반환, JavaScript는 배열/객체 사용

## 직접 해보기
1. 이름을 받아 인사말을 반환하는 함수를 작성하세요.
2. 두 숫자를 받아 더하기, 빼기, 곱하기, 나누기를 수행하는 함수를 작성하세요.
3. `training/4.functions.py`를 참고해 함수를 작성하고 실행해 보세요.

