# Python 기초: 조건문

> JavaScript 비교 내용은 선택입니다. Python 입문자라면 Python 예제와 설명만 읽고, 연습은 `notebooks/02-python-basics-conditionals.ipynb`와 `training/2.if.py`에서 직접 실행해 보세요.

## 개요

조건문은 조건에 따라 다른 코드를 실행할 수 있게 해줍니다. Python과 JavaScript 모두 유사한 조건문 구조를 가지고 있지만, 문법과 동작 방식에 차이가 있습니다.

## 기본 if 문

**Python 예제:**
```python
# 기본 if 문
age = 20

if age >= 18:
    print("성인입니다")
```

**JavaScript 예제:**
```javascript
// 기본 if 문
let age = 20;

if (age >= 18) {
    console.log("성인입니다");
}
```

**비교 설명:**
- Python은 콜론(`:`)과 들여쓰기로 블록을 구분합니다.
- JavaScript는 중괄호(`{}`)로 블록을 구분합니다.
- Python은 조건식에 괄호가 필요 없지만, JavaScript는 괄호가 필요합니다.
- Python은 들여쓰기가 문법의 일부이지만, JavaScript는 들여쓰기가 선택사항입니다.

## if-else 문

**Python 예제:**
```python
# if-else 문
age = 15

if age >= 18:
    print("성인입니다")
else:
    print("미성년자입니다")
```

**JavaScript 예제:**
```javascript
// if-else 문
let age = 15;

if (age >= 18) {
    console.log("성인입니다");
} else {
    console.log("미성년자입니다");
}
```

**비교 설명:**
- 두 언어 모두 `if-else` 구조가 동일합니다.
- Python은 `else:` 뒤에 콜론이 필요합니다.
- JavaScript는 `else` 뒤에 중괄호가 필요합니다.

## if-elif-else 문

여러 조건을 확인할 때 사용합니다.

**Python 예제:**
```python
# if-elif-else 문
score = 85

if score >= 90:
    print("A등급")
elif score >= 80:
    print("B등급")
elif score >= 70:
    print("C등급")
else:
    print("D등급")
```

**JavaScript 예제:**
```javascript
// if-else if-else 문
let score = 85;

if (score >= 90) {
    console.log("A등급");
} else if (score >= 80) {
    console.log("B등급");
} else if (score >= 70) {
    console.log("C등급");
} else {
    console.log("D등급");
}
```

**비교 설명:**
- Python은 `elif` 키워드를 사용합니다.
- JavaScript는 `else if`를 사용합니다 (두 단어로 구분).
- 두 언어 모두 여러 조건을 체인으로 연결할 수 있습니다.

## 중첩 조건문

조건문 안에 조건문을 사용할 수 있습니다.

**Python 예제:**
```python
# 중첩 조건문
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("운전 가능합니다")
    else:
        print("면허가 필요합니다")
else:
    print("미성년자는 운전할 수 없습니다")
```

**JavaScript 예제:**
```javascript
// 중첩 조건문
let age = 25;
let hasLicense = true;

if (age >= 18) {
    if (hasLicense) {
        console.log("운전 가능합니다");
    } else {
        console.log("면허가 필요합니다");
    }
} else {
    console.log("미성년자는 운전할 수 없습니다");
}
```

**비교 설명:**
- 두 언어 모두 중첩 조건문을 지원합니다.
- Python은 들여쓰기로 중첩 레벨을 구분하고, JavaScript는 중괄호로 구분합니다.

## 실습 예제

### 예제 1: 점수 등급 판정

**Python 예제:**
```python
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

scores = [95, 87, 72, 65, 45]
for score in scores:
    print(f"점수: {score}, 등급: {get_grade(score)}")
```

### 예제 2: 사용자 입력 처리

**Python 예제:**
```python
# 사용자 입력을 받아 조건 확인
age = int(input("나이를 입력하세요: "))

if age < 0:
    print("잘못된 입력입니다")
elif age < 13:
    print("어린이입니다")
elif age < 20:
    print("청소년입니다")
elif age < 65:
    print("성인입니다")
else:
    print("노인입니다")
```

## 요약

### Python
- **조건문**: `if`, `elif`, `else`로 조건에 따른 분기 처리
- 들여쓰기로 블록을 구분하며, 콜론(`:`)이 필요함
- 여러 조건을 `elif`로 체인 연결 가능
- 중첩 조건문 지원

### JavaScript
- **조건문**: `if`, `else if`, `else`로 조건에 따른 분기 처리
- 중괄호(`{}`)로 블록을 구분하며, 조건식에 괄호가 필요함
- 여러 조건을 `else if`로 체인 연결 가능
- 중첩 조건문 지원

### 주요 차이점
- Python은 들여쓰기로 블록 구분, JavaScript는 중괄호로 블록 구분
- Python은 `elif` 키워드 사용, JavaScript는 `else if` 사용
- Python은 조건식에 괄호 불필요, JavaScript는 괄호 필요

## 직접 해보기
1. 사용자 입력 점수를 받아 90점 이상이면 "합격", 나머지는 "불합격"을 출력하는 스크립트를 만들어 보세요.
2. `training/2.if.py`를 실행하면서 `number1`, `number2` 값을 바꿔 조건 분기가 어떻게 달라지는지 확인하세요.
3. 중첩 조건문을 사용해 나이와 면허 여부에 따라 운전 가능 여부를 판단하는 코드를 작성하세요.

