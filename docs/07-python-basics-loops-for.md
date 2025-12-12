# Python 기초: for 반복문

> JavaScript 비교 섹션은 참고용입니다. Python 중심으로 학습하려면 Python 예제만 실행해도 충분합니다. 실습은 `notebooks/03-python-basics-loops.ipynb`와 `training/3.loop.py`에서 직접 코드를 수정하며 진행하세요.

## 개요

`for` 반복문은 시퀀스(리스트, 문자열 등)의 각 요소를 순회하거나, 특정 횟수만큼 반복 실행할 때 사용합니다. Python의 `for` 문은 JavaScript와 다른 특징을 가지고 있습니다.

## 리스트/배열 순회

**Python 예제:**
```python
# 리스트 순회
fruits = ["사과", "바나나", "오렌지"]

for fruit in fruits:
    print(fruit)

# 출력:
# 사과
# 바나나
# 오렌지
```

**JavaScript 예제:**
```javascript
// 배열 순회
let fruits = ["사과", "바나나", "오렌지"];

// for...of 문
for (let fruit of fruits) {
    console.log(fruit);
}

// forEach 메서드
fruits.forEach(fruit => {
    console.log(fruit);
});

// 전통적인 for 문
for (let i = 0; i < fruits.length; i++) {
    console.log(fruits[i]);
}
```

**비교 설명:**
- Python의 `for...in`은 시퀀스의 값을 직접 순회합니다.
- JavaScript의 `for...of`는 Python의 `for...in`과 유사합니다.
- JavaScript의 `for...in`은 객체의 키를 순회하므로 배열에는 권장하지 않습니다.
- JavaScript는 `forEach()` 메서드도 제공합니다.

## range() 함수

숫자 범위를 생성하여 반복할 때 사용합니다.

**Python 예제:**
```python
# 0부터 4까지 (5는 제외)
for i in range(5):
    print(i)

# 출력:
# 0
# 1
# 2
# 3
# 4

# 시작값과 끝값 지정
for i in range(1, 6):
    print(i)

# 출력:
# 1
# 2
# 3
# 4
# 5

# 간격 지정
for i in range(0, 10, 2):
    print(i)

# 출력:
# 0
# 2
# 4
# 6
# 8

# 역순 (10부터 1까지)
for i in range(10, 0, -1):
    print(i)
```

**JavaScript 예제:**
```javascript
// 0부터 4까지
for (let i = 0; i < 5; i++) {
    console.log(i);
}

// 시작값과 끝값 지정
for (let i = 1; i < 6; i++) {
    console.log(i);
}

// 간격 지정
for (let i = 0; i < 10; i += 2) {
    console.log(i);
}

// 역순
for (let i = 10; i > 0; i--) {
    console.log(i);
}
```

**비교 설명:**
- Python은 `range()` 함수로 숫자 범위를 생성합니다.
- JavaScript는 전통적인 C 스타일 `for` 문을 사용합니다.
- Python의 `range()`는 메모리 효율적입니다 (제너레이터처럼 동작).
- JavaScript의 `for` 문은 더 명시적이지만, 초기화-조건-증감을 모두 작성해야 합니다.

## 문자열 순회

**Python 예제:**
```python
# 문자열 순회
text = "Python"
for char in text:
    print(char)

# 출력:
# P
# y
# t
# h
# o
# n
```

## 딕셔너리 순회

**Python 예제:**
```python
# 딕셔너리 순회
person = {"name": "홍길동", "age": 25, "city": "서울"}

# 키만 순회
for key in person:
    print(key)

# 값만 순회
for value in person.values():
    print(value)

# 키-값 쌍 순회
for key, value in person.items():
    print(f"{key}: {value}")
```

## 실습 예제

### 예제 1: 구구단 출력

**Python 예제:**
```python
for i in range(2, 10):
    print(f"{i}단")
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")
    print()
```

### 예제 2: 리스트 합계 계산

**Python 예제:**
```python
numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total += num

print(f"합계: {total}")  # 합계: 15
```

## 요약

### Python
- **for 문**: `for item in iterable` 형식으로 시퀀스 순회
- **range()**: 숫자 범위 생성 함수 (`range(start, stop, step)`)
- 리스트, 문자열, 딕셔너리 등 모든 이터러블 객체를 순회 가능
- `range()`는 메모리 효율적이며 제너레이터처럼 동작

### JavaScript
- **for...of**: 이터러블 객체 순회
- **for 문**: 전통적인 C 스타일 반복문 (`for (초기화; 조건; 증감)`)
- **forEach()**: 배열 메서드로 순회
- 배열, 문자열 등 이터러블 객체를 순회 가능

### 주요 차이점
- Python은 `range()`로 숫자 범위를 생성하지만, JavaScript는 전통적인 `for` 문 사용
- Python의 `for` 문은 더 간결하고 읽기 쉬움
- JavaScript는 `forEach()` 메서드로 함수형 스타일 순회 가능

## 직접 해보기
1. `range()`를 사용해 1부터 10까지의 숫자를 출력하는 코드를 작성하세요.
2. 리스트 `["사과", "바나나", "오렌지"]`를 `for` 문으로 순회하며 각 과일 이름을 출력하세요.
3. 중첩 `for` 문을 사용해 구구단을 출력하는 코드를 작성하세요.

