# Python 기초: 반복문 제어 (break, continue, else)

> JavaScript 비교 섹션은 참고용입니다. Python 중심으로 학습하려면 Python 예제만 실행해도 충분합니다. 실습은 `notebooks/03-python-basics-loops.ipynb`와 `training/3.loop.py`에서 직접 코드를 수정하며 진행하세요.

## 개요

반복문의 흐름을 제어하는 `break`, `continue`, 그리고 Python에만 있는 `for-else`와 `while-else`에 대해 학습합니다.

## break 문

반복문을 완전히 종료합니다.

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
```

**비교 설명:**
- 두 언어 모두 `break`를 동일하게 사용합니다.
- `break`는 반복문을 완전히 종료합니다.
- 중첩 반복문에서 `break`는 가장 가까운 반복문만 종료합니다.

## continue 문

현재 반복만 건너뛰고 다음 반복으로 진행합니다.

**Python 예제:**
```python
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
// continue: 현재 반복 건너뛰기
for (let i = 0; i < 10; i++) {
    if (i % 2 === 0) {  // 짝수면 건너뛰기
        continue;
    }
    console.log(i);
}
```

**비교 설명:**
- 두 언어 모두 `continue`를 동일하게 사용합니다.
- `continue`는 현재 반복만 건너뛰고 다음 반복으로 진행합니다.

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

## 실습 예제

```python
# break 예제: 특정 값 찾기
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 5

for num in numbers:
    if num == target:
        print(f"{target}를 찾았습니다!")
        break
else:
    print(f"{target}를 찾지 못했습니다.")

# continue 예제: 짝수만 출력
for i in range(1, 11):
    if i % 2 != 0:  # 홀수면 건너뛰기
        continue
    print(i)
```

## 요약

### Python
- **break**: 반복문 완전히 종료
- **continue**: 현재 반복만 건너뛰기
- **for-else / while-else**: 반복문이 정상 완료되면 else 실행 (break로 종료되면 실행 안 됨)

### JavaScript
- **break**: 반복문 완전히 종료
- **continue**: 현재 반복만 건너뛰기
- 반복문에 else 절 지원하지 않음 (플래그 변수로 대체)

### 주요 차이점
- Python은 `for-else`와 `while-else`를 지원하지만, JavaScript는 지원하지 않음
- 두 언어 모두 `break`와 `continue`는 동일하게 사용

## 직접 해보기
1. `break`를 사용해 리스트에서 특정 값을 찾으면 반복문을 종료하는 코드를 작성하세요.
2. `continue`를 사용해 1부터 20까지의 숫자 중 3의 배수만 출력하는 코드를 작성하세요.
3. `for-else`를 사용해 리스트에서 값을 찾지 못했을 때 메시지를 출력하는 코드를 작성하세요.

