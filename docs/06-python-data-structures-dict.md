# Python 기초: 딕셔너리 (Dictionary)

## 개요

딕셔너리는 키-값 쌍으로 이루어진 자료구조입니다. Python의 딕셔너리는 JavaScript의 객체(Object)와 유사하지만, 몇 가지 중요한 차이점이 있습니다.

## 딕셔너리 vs 객체

**Python 예제:**
```python
# 빈 딕셔너리
empty_dict = {}
empty_dict2 = dict()

# 키-값 쌍
person = {
    "name": "홍길동",
    "age": 25,
    "city": "서울"
}

print(person)  # {'name': '홍길동', 'age': 25, 'city': '서울'}
```

**JavaScript 예제:**
```javascript
// 빈 객체
let emptyObj = {};
let emptyObj2 = new Object();

// 키-값 쌍
let person = {
    name: "홍길동",
    age: 25,
    city: "서울"
};

console.log(person);  // {name: '홍길동', age: 25, city: '서울'}
```

**비교 설명:**
- Python은 `dict()` 생성자나 `{}`로 딕셔너리를 생성합니다.
- JavaScript는 `new Object()` 생성자나 `{}`로 객체를 생성합니다.
- Python의 키는 문자열로 감싸야 하지만, JavaScript는 따옴표 없이도 사용 가능합니다.
- Python 3.7+부터 딕셔너리는 삽입 순서를 유지합니다 (JavaScript 객체도 ES2015+부터 순서 유지).

## 접근

**Python 예제:**
```python
person = {"name": "홍길동", "age": 25, "city": "서울"}

# 키로 접근
print(person["name"])  # 홍길동
print(person["age"])   # 25

# get() 메서드 (키가 없어도 오류 없음)
print(person.get("name"))      # 홍길동
print(person.get("email"))    # None
print(person.get("email", "없음"))  # 없음 (기본값)

# 키 존재 확인
print("name" in person)  # True
print("email" in person)  # False
```

**JavaScript 예제:**
```javascript
let person = {name: "홍길동", age: 25, city: "서울"};

// 키로 접근
console.log(person["name"]);  // 홍길동
console.log(person.age);      // 25 (점 표기법)

// 옵셔널 체이닝 (ES2020+)
console.log(person?.email ?? "없음");  // 없음

// 키 존재 확인
console.log("name" in person);  // true
console.log("email" in person);  // false
console.log(person.hasOwnProperty("name"));  // true
```

**비교 설명:**
- Python은 `[]`로만 접근하지만, JavaScript는 `[]`와 `.` (점 표기법) 모두 사용 가능합니다.
- Python의 `get()`은 JavaScript의 옵셔널 체이닝(`?.`)과 유사한 역할을 합니다.
- Python의 `in` 연산자는 JavaScript에도 동일하게 존재합니다.
- JavaScript는 `hasOwnProperty()`로 직접 속성만 확인할 수 있습니다.

## 수정

**Python 예제:**
```python
person = {"name": "홍길동", "age": 25}

# 값 추가/수정
person["city"] = "서울"
person["age"] = 26
print(person)  # {'name': '홍길동', 'age': 26, 'city': '서울'}

# update() 메서드
person.update({"email": "hong@example.com", "age": 27})
print(person)

# 값 제거
del person["email"]
print(person)  # {'name': '홍길동', 'age': 27, 'city': '서울'}

popped = person.pop("city")
print(popped)  # 서울
print(person)  # {'name': '홍길동', 'age': 27}
```

**JavaScript 예제:**
```javascript
let person = {name: "홍길동", age: 25};

// 값 추가/수정
person.city = "서울";
person["age"] = 26;
console.log(person);  // {name: '홍길동', age: 26, city: '서울'}

// Object.assign() 또는 스프레드 연산자
person = {...person, email: "hong@example.com", age: 27};
console.log(person);

// 값 제거
delete person.email;
console.log(person);  // {name: '홍길동', age: 27, city: '서울'}

// pop() 메서드는 없음, delete 사용
delete person.city;
console.log(person);  // {name: '홍길동', age: 27}
```

**비교 설명:**
- Python의 `update()`는 JavaScript의 `Object.assign()` 또는 스프레드 연산자와 유사합니다.
- Python의 `del`은 JavaScript의 `delete` 연산자와 동일합니다.
- Python의 `pop()`은 값을 반환하지만, JavaScript 객체에는 `pop()` 메서드가 없습니다.

## 메서드

**Python 예제:**
```python
person = {"name": "홍길동", "age": 25, "city": "서울"}

# 모든 키
print(person.keys())    # dict_keys(['name', 'age', 'city'])

# 모든 값
print(person.values())  # dict_values(['홍길동', 25, '서울'])

# 모든 키-값 쌍
print(person.items())   # dict_items([('name', '홍길동'), ('age', 25), ('city', '서울')])

# 순회
for key in person:
    print(f"{key}: {person[key]}")

for key, value in person.items():
    print(f"{key}: {value}")

# 길이
print(len(person))  # 3
```

**JavaScript 예제:**
```javascript
let person = {name: "홍길동", age: 25, city: "서울"};

// 모든 키
console.log(Object.keys(person));    // ['name', 'age', 'city']

// 모든 값
console.log(Object.values(person));  // ['홍길동', 25, '서울']

// 모든 키-값 쌍
console.log(Object.entries(person));   // [['name', '홍길동'], ['age', 25], ['city', '서울']]

// 순회
for (let key in person) {
    console.log(`${key}: ${person[key]}`);
}

for (let [key, value] of Object.entries(person)) {
    console.log(`${key}: ${value}`);
}

// 길이
console.log(Object.keys(person).length);  // 3
```

**비교 설명:**
- Python은 딕셔너리 메서드로 직접 호출하지만, JavaScript는 `Object` 정적 메서드를 사용합니다.
- Python의 `items()`는 튜플의 리스트를 반환하지만, JavaScript의 `entries()`는 배열의 배열을 반환합니다.
- Python의 `keys()`, `values()`, `items()`는 뷰 객체를 반환하지만, JavaScript는 배열을 반환합니다.
- JavaScript는 `for...in` 루프를 사용할 수 있지만, 프로토타입 체인을 순회할 수 있으므로 주의가 필요합니다.

## 딕셔너리 컴프리헨션

**Python 예제:**
```python
# 딕셔너리 컴프리헨션
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 조건문 포함
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

**JavaScript 예제:**
```javascript
// 객체 컴프리헨션은 없음, Object.fromEntries() 사용
let squares = Object.fromEntries(
    Array.from({length: 5}, (_, i) => [i, i ** 2])
);
console.log(squares);  // {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

// 조건문 포함
let evenSquares = Object.fromEntries(
    Array.from({length: 10}, (_, i) => i)
        .filter(x => x % 2 === 0)
        .map(x => [x, x ** 2])
);
console.log(evenSquares);  // {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

**비교 설명:**
- Python은 딕셔너리 컴프리헨션을 직접 지원합니다.
- JavaScript는 객체 컴프리헨션을 지원하지 않지만, `Object.fromEntries()`와 배열 메서드를 조합하여 사용할 수 있습니다.
- Python의 딕셔너리 컴프리헨션이 더 간결하고 읽기 쉽습니다.

## 요약

### Python
- **딕셔너리**: 키-값 쌍, `{}`로 생성
- **접근**: `dict[key]` 또는 `dict.get(key, default)`
- **메서드**: `keys()`, `values()`, `items()`, `update()`, `pop()` 등
- **딕셔너리 컴프리헨션**: 간결한 딕셔너리 생성

### JavaScript
- **객체**: 키-값 쌍, `{}`로 생성
- **접근**: `obj[key]` 또는 `obj.key` (점 표기법)
- **메서드**: `Object.keys()`, `Object.values()`, `Object.entries()` 등
- **스프레드 연산자**: 객체 복사 및 병합

### 주요 차이점
- Python의 키는 문자열로 감싸야 하지만, JavaScript는 따옴표 없이도 사용 가능
- Python은 `get()` 메서드로 안전한 접근, JavaScript는 옵셔널 체이닝 사용
- Python의 `items()`는 튜플 리스트, JavaScript의 `entries()`는 배열의 배열
- Python의 딕셔너리 컴프리헨션은 JavaScript에 없지만, `Object.fromEntries()`로 유사하게 구현 가능

