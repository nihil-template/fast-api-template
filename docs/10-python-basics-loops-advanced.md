# Python 기초: 고급 반복문 기법

> JavaScript 비교 섹션은 참고용입니다. Python 중심으로 학습하려면 Python 예제만 실행해도 충분합니다. 실습은 `notebooks/03-python-basics-loops.ipynb`와 `training/3.loop.py`에서 직접 코드를 수정하며 진행하세요.

## 개요

`enumerate()`, `zip()`, 그리고 리스트 컴프리헨션 등 Python의 고급 반복문 기법에 대해 학습합니다.

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

## 리스트 컴프리헨션

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

### 예제 1: 리스트 필터링

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

### 예제 2: enumerate와 zip 활용

**Python 예제:**
```python
names = ["홍길동", "김철수", "이영희"]
ages = [25, 30, 28]

# enumerate와 zip 함께 사용
for index, (name, age) in enumerate(zip(names, ages), start=1):
    print(f"{index}. {name}: {age}세")
```

## 요약

### Python
- **enumerate()**: 인덱스와 값 함께 순회
- **zip()**: 여러 시퀀스 동시 순회
- **리스트 컴프리헨션**: 간결한 리스트 생성
- 컴프리헨션은 딕셔너리, 집합에도 사용 가능

### JavaScript
- **forEach()**: 배열 메서드로 순회 (인덱스 제공)
- **entries()**: 인덱스와 값 함께 순회
- **map()/filter()**: 배열 변환 및 필터링
- 배열 메서드 체이닝으로 함수형 스타일 구현

### 주요 차이점
- Python의 리스트 컴프리헨션은 JavaScript의 배열 메서드 체이닝과 유사한 역할
- Python의 `zip()`과 같은 내장 함수가 JavaScript에는 없음
- JavaScript는 함수형 프로그래밍 스타일의 배열 메서드가 풍부함

## 직접 해보기
1. 리스트 컴프리헨션을 사용해 1~30 중 3의 배수만 담긴 리스트를 만들어 보세요.
2. `enumerate()`를 사용해 리스트의 각 요소에 번호를 매겨 출력하세요.
3. `zip()`을 사용해 두 개의 리스트를 동시에 순회하며 각 요소를 조합해 출력하세요.

