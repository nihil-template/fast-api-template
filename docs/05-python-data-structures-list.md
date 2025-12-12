# Python 기초: 리스트 (List)

## 개요

리스트는 순서가 있는 변경 가능한 시퀀스입니다. Python의 리스트는 JavaScript의 배열과 유사하지만, 몇 가지 중요한 차이점이 있습니다.

## 리스트 vs 배열

**Python 예제:**
```python
# 빈 리스트
empty_list = []
empty_list2 = list()

# 요소가 있는 리스트
fruits = ["사과", "바나나", "오렌지"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "문자열", 3.14, True]

print(fruits)  # ['사과', '바나나', '오렌지']
```

**JavaScript 예제:**
```javascript
// 빈 배열
let emptyArray = [];
let emptyArray2 = new Array();

// 요소가 있는 배열
let fruits = ["사과", "바나나", "오렌지"];
let numbers = [1, 2, 3, 4, 5];
let mixed = [1, "문자열", 3.14, true];

console.log(fruits);  // ['사과', '바나나', '오렌지']
```

**비교 설명:**
- Python은 `list()` 생성자나 `[]`로 리스트를 생성합니다.
- JavaScript는 `new Array()` 생성자나 `[]`로 배열을 생성합니다.
- 두 언어 모두 다양한 타입의 요소를 혼합하여 저장할 수 있습니다.
- Python의 리스트와 JavaScript의 배열은 거의 동일한 개념입니다.

## 접근

**Python 예제:**
```python
fruits = ["사과", "바나나", "오렌지"]

# 인덱스로 접근 (0부터 시작)
print(fruits[0])   # 사과
print(fruits[1])   # 바나나
print(fruits[-1])  # 오렌지 (마지막 요소)

# 슬라이싱
print(fruits[0:2])    # ['사과', '바나나']
print(fruits[:2])     # ['사과', '바나나'] (처음부터)
print(fruits[1:])     # ['바나나', '오렌지'] (끝까지)
print(fruits[:])      # 전체 복사
```

**JavaScript 예제:**
```javascript
let fruits = ["사과", "바나나", "오렌지"];

// 인덱스로 접근 (0부터 시작)
console.log(fruits[0]);   // 사과
console.log(fruits[1]);   // 바나나
console.log(fruits[fruits.length - 1]);  // 오렌지 (마지막 요소)

// 슬라이싱 (slice 메서드)
console.log(fruits.slice(0, 2));    // ['사과', '바나나']
console.log(fruits.slice(0, 2));    // ['사과', '바나나'] (처음부터)
console.log(fruits.slice(1));      // ['바나나', '오렌지'] (끝까지)
console.log(fruits.slice());        // 전체 복사
```

**비교 설명:**
- Python은 음수 인덱스로 뒤에서부터 접근할 수 있습니다 (`-1`은 마지막 요소).
- JavaScript는 음수 인덱스를 직접 지원하지 않지만, `length`를 사용하거나 `at()` 메서드(ES2022)를 사용할 수 있습니다.
- Python의 슬라이싱은 `[start:end]` 형식이고, JavaScript는 `slice(start, end)` 메서드를 사용합니다.
- Python의 슬라이싱이 더 간결하고 직관적입니다.

## 수정

**Python 예제:**
```python
fruits = ["사과", "바나나", "오렌지"]

# 요소 변경
fruits[0] = "포도"
print(fruits)  # ['포도', '바나나', '오렌지']

# 요소 추가
fruits.append("딸기")  # 끝에 추가
print(fruits)  # ['포도', '바나나', '오렌지', '딸기']

fruits.insert(1, "수박")  # 특정 위치에 삽입
print(fruits)  # ['포도', '수박', '바나나', '오렌지', '딸기']

# 요소 제거
fruits.remove("바나나")  # 값으로 제거
print(fruits)  # ['포도', '수박', '오렌지', '딸기']

popped = fruits.pop()  # 마지막 요소 제거하고 반환
print(popped)  # 딸기
print(fruits)  # ['포도', '수박', '오렌지']

fruits.pop(0)  # 인덱스로 제거
print(fruits)  # ['수박', '오렌지']
```

**JavaScript 예제:**
```javascript
let fruits = ["사과", "바나나", "오렌지"];

// 요소 변경
fruits[0] = "포도";
console.log(fruits);  // ['포도', '바나나', '오렌지']

// 요소 추가
fruits.push("딸기");  // 끝에 추가
console.log(fruits);  // ['포도', '바나나', '오렌지', '딸기']

fruits.splice(1, 0, "수박");  // 특정 위치에 삽입
console.log(fruits);  // ['포도', '수박', '바나나', '오렌지', '딸기']

// 요소 제거
let index = fruits.indexOf("바나나");
if (index > -1) {
    fruits.splice(index, 1);  // 값으로 제거
}
console.log(fruits);  // ['포도', '수박', '오렌지', '딸기']

let popped = fruits.pop();  // 마지막 요소 제거하고 반환
console.log(popped);  // 딸기
console.log(fruits);  // ['포도', '수박', '오렌지']

fruits.shift();  // 첫 번째 요소 제거
console.log(fruits);  // ['수박', '오렌지']
```

**비교 설명:**
- Python의 `append()`는 JavaScript의 `push()`와 동일합니다.
- Python의 `insert()`는 JavaScript의 `splice()`와 유사합니다.
- Python의 `remove()`는 값으로 제거하지만, JavaScript는 `indexOf()`와 `splice()`를 조합해야 합니다.
- Python의 `pop()`은 인덱스를 지정할 수 있지만, JavaScript의 `pop()`은 마지막 요소만 제거합니다.
- JavaScript의 `shift()`는 첫 번째 요소를 제거합니다 (Python에는 없음).

## 메서드

**Python 예제:**
```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# 정렬
numbers.sort()  # 원본 수정
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

sorted_numbers = sorted(numbers)  # 새 리스트 반환

# 역순 정렬
numbers.sort(reverse=True)
print(numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]

# 리스트 연결
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)  # [1, 2, 3, 4, 5, 6]

# 반복
repeated = [1, 2] * 3
print(repeated)  # [1, 2, 1, 2, 1, 2]

# 길이
print(len(numbers))  # 8

# 요소 개수
print(numbers.count(1))  # 2

# 인덱스 찾기
print(numbers.index(5))  # 2
```

**JavaScript 예제:**
```javascript
let numbers = [3, 1, 4, 1, 5, 9, 2, 6];

// 정렬
numbers.sort();  // 원본 수정 (주의: 문자열로 변환 후 정렬)
console.log(numbers);  // [1, 1, 2, 3, 4, 5, 6, 9]

// 숫자 정렬
numbers.sort((a, b) => a - b);
console.log(numbers);  // [1, 1, 2, 3, 4, 5, 6, 9]

// 역순 정렬
numbers.sort((a, b) => b - a);
console.log(numbers);  // [9, 6, 5, 4, 3, 2, 1, 1]

// 배열 연결
let list1 = [1, 2, 3];
let list2 = [4, 5, 6];
let combined = list1.concat(list2);
// 또는
combined = [...list1, ...list2];
console.log(combined);  // [1, 2, 3, 4, 5, 6]

// 반복 (직접 지원하지 않음, fill과 map 조합)
let repeated = Array(3).fill([1, 2]).flat();
// 또는
repeated = [1, 2, 1, 2, 1, 2];

// 길이
console.log(numbers.length);  // 8

// 요소 개수 (직접 지원하지 않음)
let count = numbers.filter(x => x === 1).length;
console.log(count);  // 2

// 인덱스 찾기
console.log(numbers.indexOf(5));  // 2
```

**비교 설명:**
- Python의 `sort()`는 기본적으로 숫자를 올바르게 정렬하지만, JavaScript의 `sort()`는 문자열로 변환 후 정렬하므로 비교 함수가 필요합니다.
- Python의 `+` 연산자는 리스트를 연결하지만, JavaScript는 `concat()` 또는 스프레드 연산자를 사용합니다.
- Python의 `*` 연산자는 리스트를 반복하지만, JavaScript는 직접 지원하지 않습니다.
- Python의 `count()`와 `index()`는 JavaScript에는 없지만, `filter()`와 `indexOf()`로 구현할 수 있습니다.

## 리스트 컴프리헨션 vs 배열 메서드

**Python 예제:**
```python
# 리스트 컴프리헨션
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# 조건문 포함
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]
```

**JavaScript 예제:**
```javascript
// map 메서드
let squares = Array.from({length: 5}, (_, i) => i ** 2);
console.log(squares);  // [0, 1, 4, 9, 16]

// filter와 map 조합
let evenSquares = Array.from({length: 10}, (_, i) => i)
    .filter(x => x % 2 === 0)
    .map(x => x ** 2);
console.log(evenSquares);  // [0, 4, 16, 36, 64]
```

**비교 설명:**
- Python의 리스트 컴프리헨션은 간결하고 읽기 쉽습니다.
- JavaScript는 `map()`, `filter()` 등의 배열 메서드를 체이닝하여 사용합니다.
- Python의 컴프리헨션이 더 간결하지만, JavaScript의 메서드 체이닝도 함수형 프로그래밍 스타일과 잘 맞습니다.

## 요약

### Python
- **리스트**: 순서 있는 변경 가능한 시퀀스, `[]`로 생성
- **슬라이싱**: `[start:end]` 형식으로 간결하게 사용
- **메서드**: `append()`, `insert()`, `remove()`, `pop()`, `sort()` 등
- **리스트 컴프리헨션**: 간결한 리스트 생성 방법

### JavaScript
- **배열**: 순서 있는 변경 가능한 시퀀스, `[]`로 생성
- **슬라이싱**: `slice()` 메서드 사용
- **메서드**: `push()`, `splice()`, `pop()`, `shift()`, `sort()` 등
- **배열 메서드**: `map()`, `filter()`, `reduce()` 등 함수형 메서드 풍부

### 주요 차이점
- Python은 음수 인덱스를 직접 지원하지만, JavaScript는 `length`나 `at()` 사용
- Python의 슬라이싱이 더 간결하고 직관적
- Python의 `sort()`는 기본적으로 숫자를 올바르게 정렬하지만, JavaScript는 비교 함수 필요
- Python의 리스트 컴프리헨션은 JavaScript의 배열 메서드 체이닝과 유사한 역할

