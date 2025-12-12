# Python 기초: while 반복문

> JavaScript 비교 섹션은 참고용입니다. Python 중심으로 학습하려면 Python 예제만 실행해도 충분합니다. 실습은 `notebooks/03-python-basics-loops.ipynb`와 `training/3.loop.py`에서 직접 코드를 수정하며 진행하세요.

## 개요

`while` 반복문은 조건이 참인 동안 반복 실행합니다. 조건이 거짓이 될 때까지 계속 실행되므로, 무한 루프에 주의해야 합니다.

## 기본 while 문

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

## 무한 루프

조건이 항상 참이면 무한 루프가 발생합니다. `break`로 종료할 수 있습니다.

**Python 예제:**
```python
# 무한 루프 (주의!)
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# 출력:
# 0
# 1
# 2
# 3
# 4
```

**JavaScript 예제:**
```javascript
// 무한 루프 (주의!)
let count = 0;
while (true) {
    console.log(count);
    count++;
    if (count >= 5) {
        break;
    }
}
```

## 사용자 입력과 함께 사용

**Python 예제:**
```python
# 사용자 입력을 받아 반복
while True:
    user_input = input("명령을 입력하세요 (종료: quit): ")
    if user_input == "quit":
        break
    print(f"입력한 명령: {user_input}")
```

## 실습 예제

### 예제 1: 숫자 맞추기 게임

**Python 예제:**
```python
import random

target = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("1부터 100 사이의 숫자를 맞춰보세요: "))
    attempts += 1
    
    if guess == target:
        print(f"정답입니다! {attempts}번 만에 맞췄습니다.")
        break
    elif guess < target:
        print("더 큰 수입니다.")
    else:
        print("더 작은 수입니다.")
```

### 예제 2: 짝수만 출력

**Python 예제:**
```python
count = 0
while count < 10:
    if count % 2 == 0:
        print(count)
    count += 1

# 출력:
# 0
# 2
# 4
# 6
# 8
```

## 요약

### Python
- **while 문**: 조건이 참인 동안 반복
- `while 조건:` 형식
- 조건이 거짓이 될 때까지 반복 실행
- 무한 루프에 주의 (`break`로 종료)

### JavaScript
- **while 문**: 조건이 참인 동안 반복
- `while (조건) { }` 형식
- 조건이 거짓이 될 때까지 반복 실행
- 무한 루프에 주의 (`break`로 종료)

### 주요 차이점
- Python은 콜론과 들여쓰기 사용, JavaScript는 중괄호 사용
- 두 언어 모두 동일한 구조와 동작 방식

## 직접 해보기
1. `training/3.loop.py`에서 `while` 문을 수정해 짝수만 출력하도록 바꿔 보세요.
2. `while` 문을 사용해 1부터 100까지의 합을 계산하는 코드를 작성하세요.
3. 사용자 입력을 받아 "quit"를 입력할 때까지 반복하는 프로그램을 작성하세요.

