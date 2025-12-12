# Python 기초: 타입 확인

> JavaScript 비교 섹션은 선택 사항입니다. Python만 학습 중이라면 Python 예제와 설명 위주로 읽고 넘어가도 괜찮습니다. 실습은 `training/1.variable.py`와 노트북 `notebooks/01-python-basics-types-variables.ipynb`에서 진행하세요.

## 개요

변수의 타입을 확인하는 것은 프로그래밍에서 중요한 작업입니다. Python에서는 `type()` 함수와 `isinstance()` 함수를 사용하여 변수의 타입을 확인할 수 있습니다.

## type() 함수

변수의 타입을 확인할 수 있습니다.

**Python 예제:**
```python
age = 25
name = "홍길동"
price = 19.99

print(type(age))   # <class 'int'>
print(type(name))  # <class 'str'>
print(type(price)) # <class 'float'>
```

**JavaScript 예제:**
```javascript
let age = 25;
let name = "홍길동";
let price = 19.99;

console.log(typeof age);   // "number"
console.log(typeof name);  // "string"
console.log(typeof price); // "number"
```

**비교 설명:**
- Python의 `type()`은 타입 객체를 반환합니다.
- JavaScript의 `typeof`는 타입 이름 문자열을 반환합니다.
- JavaScript는 `typeof`로는 객체의 구체적인 타입을 구분하기 어렵습니다 (예: 배열, 객체, null 모두 "object").

## isinstance() 함수

변수가 특정 타입인지 확인할 수 있습니다. `type()`보다 더 안전한 방법입니다.

**Python 예제:**
```python
age = 25
name = "홍길동"

print(isinstance(age, int))   # True
print(isinstance(age, str))   # False
print(isinstance(name, str))  # True

# 여러 타입 중 하나인지 확인
print(isinstance(age, (int, float)))  # True
```

**JavaScript 예제:**
```javascript
let age = 25;
let name = "홍길동";

console.log(age instanceof Number);   // false (원시 타입은 false)
console.log(typeof age === "number"); // true
console.log(typeof name === "string"); // true

// 배열이나 객체의 경우
let arr = [1, 2, 3];
console.log(Array.isArray(arr));      // true
console.log(arr instanceof Array);   // true
```

**비교 설명:**
- Python의 `isinstance()`는 상속 관계도 고려하여 타입을 확인합니다.
- JavaScript의 `instanceof`는 프로토타입 체인을 확인하지만, 원시 타입에는 작동하지 않습니다.
- JavaScript는 `Array.isArray()` 같은 특수한 타입 확인 함수를 제공합니다.
- Python의 `isinstance()`는 여러 타입을 튜플로 전달하여 하나라도 일치하는지 확인할 수 있습니다.

## type() vs isinstance()

`type()`과 `isinstance()`의 차이점을 이해하는 것이 중요합니다.

```python
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

# type() 사용
print(type(dog) == Dog)      # True
print(type(dog) == Animal)  # False (정확히 일치해야 함)

# isinstance() 사용
print(isinstance(dog, Dog))    # True
print(isinstance(dog, Animal)) # True (상속 관계 고려)
```

## 실습 예제

```python
# 다양한 타입의 변수
age = 25
name = "홍길동"
price = 19.99
is_active = True
data = None

# type()으로 타입 확인
print(f"age의 타입: {type(age)}")
print(f"name의 타입: {type(name)}")
print(f"price의 타입: {type(price)}")

# isinstance()로 타입 확인
print(f"age는 int인가? {isinstance(age, int)}")
print(f"name은 str인가? {isinstance(name, str)}")
print(f"age는 (int, float) 중 하나인가? {isinstance(age, (int, float))}")
```

## 요약

### Python
- `type()`: 변수의 정확한 타입 객체를 반환
- `isinstance()`: 변수가 특정 타입(또는 상속 관계)인지 확인, 더 안전한 방법
- `isinstance()`는 여러 타입을 튜플로 전달하여 확인 가능

### JavaScript
- `typeof`: 타입 이름 문자열을 반환
- `instanceof`: 프로토타입 체인 확인 (원시 타입에는 작동하지 않음)
- `Array.isArray()`: 배열 확인 전용 함수

### 주요 차이점
- Python의 `type()`은 타입 객체를 반환하지만, JavaScript의 `typeof`는 문자열을 반환
- Python의 `isinstance()`는 상속 관계를 고려하지만, JavaScript의 `instanceof`는 원시 타입에 작동하지 않음
- Python은 `isinstance()`를 사용하는 것이 더 안전하고 권장됨

## 직접 해보기
1. 문자열 `"42"`를 정수로 변환한 뒤 `type()`과 `isinstance()`로 타입을 확인하세요.
2. 여러 타입의 변수를 만들고 `isinstance()`를 사용해 타입을 확인하는 코드를 작성하세요.
3. `type()`과 `isinstance()`의 차이를 보여주는 예제 코드를 작성하세요.

