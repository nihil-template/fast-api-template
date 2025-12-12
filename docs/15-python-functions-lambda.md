# Python 기초: 람다 함수

> JavaScript 비교는 참고용입니다. Python만 실습하려면 Python 예제와 설명 위주로 읽고, `notebooks/04-python-functions.ipynb`와 `training/4.functions.py`에서 함수를 직접 작성해 보세요.

## 개요

람다 함수는 간단한 함수를 한 줄로 정의할 수 있는 방법입니다. 주로 다른 함수의 인자로 사용됩니다.

## 람다 함수 기본

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

## 람다 함수 활용

**Python 예제:**
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

# 필터링
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6, 8, 10]
```

## 실습 예제

```python
# 람다로 리스트 변환
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# 람다로 필터링
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # [2, 4]
```

## 요약

### Python
- **람다 함수**: `lambda 매개변수: 표현식` 형식
- 표현식 하나만 포함 가능
- 주로 `map()`, `filter()`, `sorted()` 등의 인자로 사용

### JavaScript
- **화살표 함수**: `(매개변수) => 표현식` 형식
- 여러 문 포함 가능
- 주로 배열 메서드의 인자로 사용

## 직접 해보기
1. `lambda`를 사용해 리스트의 각 원소를 제곱하는 코드를 작성하세요.
2. `lambda`와 `filter()`를 사용해 짝수만 필터링하는 코드를 작성하세요.
3. `lambda`와 `sorted()`를 사용해 딕셔너리 리스트를 정렬하세요.

