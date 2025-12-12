# Python 기초: 반복문

## 개요

반복문은 같은 코드를 여러 번 실행할 수 있게 해줍니다. Python과 JavaScript 모두 다양한 반복문을 제공하며, 각각의 특징과 사용법이 다릅니다.

## for 문

### 리스트/배열 순회

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

### range() 함수 vs 전통적인 for 문

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
```

**비교 설명:**
- Python은 `range()` 함수로 숫자 범위를 생성합니다.
- JavaScript는 전통적인 C 스타일 `for` 문을 사용합니다.
- Python의 `range()`는 메모리 효율적입니다 (제너레이터처럼 동작).
- JavaScript의 `for` 문은 더 명시적이지만, 초기화-조건-증감을 모두 작성해야 합니다.

## while 문

조건이 참인 동안 반복 실행합니다.

**Python 예제:**
```python
# 기본 while 문
count = 0

while count < 5:
    print(count)
    count += 1

# 출력:
# 0
# 1
# 2
# 3
# 4
```

**JavaScript 예제:**
```javascript
// 기본 while 문
let count = 0;

while (count < 5) {
    console.log(count);
    count++;
}

// 출력:
// 0
// 1
// 2
// 3
// 4
```

**비교 설명:**
- 두 언어 모두 `while` 문의 구조가 거의 동일합니다.
- Python은 콜론과 들여쓰기를 사용하고, JavaScript는 중괄호를 사용합니다.
- Python은 `count += 1` 또는 `count = count + 1`을 사용합니다.
- JavaScript는 `count++`, `count += 1`, `count = count + 1` 모두 사용 가능합니다.

## break와 continue

반복문의 흐름을 제어합니다.

**Python 예제:**
```python
# break: 반복문 종료
for i in range(10):
    if i == 5:
        break
    print(i)

# 출력:
# 0
# 1
# 2
# 3
# 4

# continue: 현재 반복 건너뛰기
for i in range(10):
    if i % 2 == 0:  # 짝수면 건너뛰기
        continue
    print(i)

# 출력:
# 1
# 3
# 5
# 7
# 9
```

**JavaScript 예제:**
```javascript
// break: 반복문 종료
for (let i = 0; i < 10; i++) {
    if (i === 5) {
        break;
    }
    console.log(i);
}

// continue: 현재 반복 건너뛰기
for (let i = 0; i < 10; i++) {
    if (i % 2 === 0) {  // 짝수면 건너뛰기
        continue;
    }
    console.log(i);
}
```

**비교 설명:**
- 두 언어 모두 `break`와 `continue`를 동일하게 사용합니다.
- `break`는 반복문을 완전히 종료하고, `continue`는 현재 반복만 건너뜁니다.
- 중첩 반복문에서 `break`는 가장 가까운 반복문만 종료합니다.

## else 절과 반복문

반복문이 정상적으로 완료되면 else 블록이 실행됩니다. (break로 종료되면 실행되지 않음)

**Python 예제:**
```python
# for-else
for i in range(5):
    print(i)
else:
    print("반복 완료")

# 출력:
# 0
# 1
# 2
# 3
# 4
# 반복 완료

# break가 있으면 else 실행 안 됨
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("반복 완료")

# 출력:
# 0
# 1
# 2
```

**JavaScript 예제:**
```javascript
// JavaScript는 for-else를 지원하지 않음
// 대신 플래그 변수 사용
let found = false;
for (let i = 0; i < 5; i++) {
    if (i === 3) {
        found = true;
        break;
    }
    console.log(i);
}

if (!found) {
    console.log("반복 완료");
}
```

**비교 설명:**
- Python은 `for-else`와 `while-else`를 지원합니다.
- JavaScript는 반복문에 `else` 절을 지원하지 않습니다.
- JavaScript에서는 플래그 변수나 다른 방법으로 동일한 효과를 구현해야 합니다.

## enumerate() 함수

인덱스와 값을 함께 가져올 수 있습니다.

**Python 예제:**
```python
fruits = ["사과", "바나나", "오렌지"]

for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# 출력:
# 0: 사과
# 1: 바나나
# 2: 오렌지

# 시작 인덱스 지정
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")
```

**JavaScript 예제:**
```javascript
let fruits = ["사과", "바나나", "오렌지"];

// forEach 메서드 사용
fruits.forEach((fruit, index) => {
    console.log(`${index}: ${fruit}`);
});

// for...of와 entries() 사용
for (let [index, fruit] of fruits.entries()) {
    console.log(`${index}: ${fruit}`);
}

// 전통적인 for 문
for (let i = 0; i < fruits.length; i++) {
    console.log(`${i}: ${fruits[i]}`);
}
```

**비교 설명:**
- Python의 `enumerate()`는 인덱스와 값을 튜플로 반환합니다.
- JavaScript의 `forEach()`는 콜백 함수의 두 번째 인자로 인덱스를 제공합니다.
- JavaScript의 `entries()` 메서드는 Python의 `enumerate()`와 유사합니다.

## zip() 함수

여러 시퀀스를 동시에 순회할 수 있습니다.

**Python 예제:**
```python
names = ["홍길동", "김철수", "이영희"]
ages = [25, 30, 28]

for name, age in zip(names, ages):
    print(f"{name}: {age}세")

# 출력:
# 홍길동: 25세
# 김철수: 30세
# 이영희: 28세
```

**JavaScript 예제:**
```javascript
let names = ["홍길동", "김철수", "이영희"];
let ages = [25, 30, 28];

// 전통적인 for 문
for (let i = 0; i < names.length; i++) {
    console.log(`${names[i]}: ${ages[i]}세`);
}

// forEach 사용
names.forEach((name, index) => {
    console.log(`${name}: ${ages[index]}세`);
});
```

**비교 설명:**
- Python의 `zip()`은 여러 시퀀스를 튜플로 묶어 순회합니다.
- JavaScript에는 `zip()`과 같은 내장 함수가 없습니다.
- JavaScript에서는 인덱스를 사용하거나 라이브러리(Lodash 등)를 사용해야 합니다.

## 리스트 컴프리헨션 vs 배열 메서드

리스트를 간결하게 생성하는 방법입니다.

**Python 예제:**
```python
# 기본 리스트 컴프리헨션
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# 조건문 포함
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# 중첩 반복문
matrix = [[i*j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

**JavaScript 예제:**
```javascript
// map 메서드
let squares = Array.from({length: 5}, (_, i) => i ** 2);
// 또는
squares = [...Array(5)].map((_, i) => i ** 2);
console.log(squares);  // [0, 1, 4, 9, 16]

// filter와 map 조합
let evenSquares = Array.from({length: 10}, (_, i) => i)
    .filter(x => x % 2 === 0)
    .map(x => x ** 2);
console.log(evenSquares);  // [0, 4, 16, 36, 64]

// 중첩 map
let matrix = Array.from({length: 3}, (_, i) =>
    Array.from({length: 3}, (_, j) => i * j)
);
console.log(matrix);  // [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

**비교 설명:**
- Python의 리스트 컴프리헨션은 간결하고 읽기 쉽습니다.
- JavaScript는 `map()`, `filter()` 등의 배열 메서드를 체이닝하여 사용합니다.
- Python의 컴프리헨션은 딕셔너리, 집합에도 사용 가능합니다.
- JavaScript는 배열 메서드 체이닝이 함수형 프로그래밍 스타일과 잘 맞습니다.

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

**JavaScript 예제:**
```javascript
for (let i = 2; i < 10; i++) {
    console.log(`${i}단`);
    for (let j = 1; j < 10; j++) {
        console.log(`${i} x ${j} = ${i * j}`);
    }
    console.log();
}
```

### 예제 2: 리스트 필터링

**Python 예제:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 짝수만 필터링
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # [2, 4, 6, 8, 10]

# 5보다 큰 수만 필터링
large_numbers = [x for x in numbers if x > 5]
print(large_numbers)  # [6, 7, 8, 9, 10]
```

**JavaScript 예제:**
```javascript
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// 짝수만 필터링
let evenNumbers = numbers.filter(x => x % 2 === 0);
console.log(evenNumbers);  // [2, 4, 6, 8, 10]

// 5보다 큰 수만 필터링
let largeNumbers = numbers.filter(x => x > 5);
console.log(largeNumbers);  // [6, 7, 8, 9, 10]
```

## 요약

### Python
- **for 문**: `for item in iterable` 형식으로 시퀀스 순회
- **range()**: 숫자 범위 생성 함수
- **while 문**: 조건이 참인 동안 반복
- **break/continue**: 반복문 제어
- **for-else**: 반복문이 정상 완료되면 else 실행
- **enumerate()**: 인덱스와 값 함께 순회
- **zip()**: 여러 시퀀스 동시 순회
- **리스트 컴프리헨션**: 간결한 리스트 생성

### JavaScript
- **for...of**: 이터러블 객체 순회
- **for 문**: 전통적인 C 스타일 반복문
- **while 문**: 조건이 참인 동안 반복
- **break/continue**: 반복문 제어
- **forEach()**: 배열 메서드로 순회
- **map()/filter()**: 배열 변환 및 필터링
- **entries()**: 인덱스와 값 함께 순회

### 주요 차이점
- Python은 `range()`로 숫자 범위를 생성하지만, JavaScript는 전통적인 `for` 문 사용
- Python은 `for-else`를 지원하지만, JavaScript는 지원하지 않음
- Python의 리스트 컴프리헨션은 JavaScript의 배열 메서드 체이닝과 유사한 역할
- Python의 `zip()`과 같은 내장 함수가 JavaScript에는 없음
- JavaScript는 함수형 프로그래밍 스타일의 배열 메서드가 풍부함

