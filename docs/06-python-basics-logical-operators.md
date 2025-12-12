# Python 기초: 논리 연산자와 조건 표현식

> JavaScript 비교 내용은 선택입니다. Python 입문자라면 Python 예제와 설명만 읽고, 연습은 `notebooks/02-python-basics-conditionals.ipynb`와 `training/2.if.py`에서 직접 실행해 보세요.

## 개요

논리 연산자는 여러 조건을 조합할 때 사용합니다. 또한 간단한 조건문을 한 줄로 표현하는 삼항 연산자와 패턴 매칭에 대해서도 학습합니다.

## 논리 연산자

여러 조건을 조합할 때 사용합니다.

**Python 예제:**
```python
# and (그리고)
age = 25
has_license = True

if age >= 18 and has_license:
    print("운전 가능합니다")

# or (또는)
is_student = True
is_teacher = False

if is_student or is_teacher:
    print("학교 구성원입니다")

# not (아님)
is_rainy = False

if not is_rainy:
    print("날씨가 좋습니다")
```

**JavaScript 예제:**
```javascript
// && (그리고)
let age = 25;
let hasLicense = true;

if (age >= 18 && hasLicense) {
    console.log("운전 가능합니다");
}

// || (또는)
let isStudent = true;
let isTeacher = false;

if (isStudent || isTeacher) {
    console.log("학교 구성원입니다");
}

// ! (아님)
let isRainy = false;

if (!isRainy) {
    console.log("날씨가 좋습니다");
}
```

**비교 설명:**
- Python은 `and`, `or`, `not` 키워드를 사용합니다.
- JavaScript는 `&&`, `||`, `!` 기호를 사용합니다.
- Python의 논리 연산자는 키워드이므로 가독성이 좋습니다.
- JavaScript의 논리 연산자는 짧지만, 단락 평가(short-circuit evaluation)를 지원합니다.

## 삼항 연산자 (조건 표현식)

간단한 조건문을 한 줄로 표현할 수 있습니다.

**Python 예제:**
```python
# 기본 삼항 연산자
age = 20
status = "성인" if age >= 18 else "미성년자"
print(status)  # 성인

# 중첩 삼항 연산자
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(grade)  # B
```

**JavaScript 예제:**
```javascript
// 기본 삼항 연산자
let age = 20;
let status = age >= 18 ? "성인" : "미성년자";
console.log(status);  // 성인

// 중첩 삼항 연산자
let score = 85;
let grade = score >= 90 ? "A" : score >= 80 ? "B" : "C";
console.log(grade);  // B
```

**비교 설명:**
- Python의 삼항 연산자: `값1 if 조건 else 값2`
- JavaScript의 삼항 연산자: `조건 ? 값1 : 값2`
- Python은 조건이 중간에 위치하고, JavaScript는 조건이 앞에 위치합니다.
- 두 언어 모두 중첩 삼항 연산자를 지원하지만, 가독성을 위해 남용하지 않는 것이 좋습니다.

## switch 문과 match-case 문

### JavaScript의 switch 문

JavaScript는 `switch` 문을 제공하지만, Python은 제공하지 않습니다.

**JavaScript 예제:**
```javascript
// switch 문
let day = 3;
let dayName;

switch (day) {
    case 1:
        dayName = "월요일";
        break;
    case 2:
        dayName = "화요일";
        break;
    case 3:
        dayName = "수요일";
        break;
    default:
        dayName = "알 수 없음";
}

console.log(dayName);  // 수요일
```

### Python의 match-case 문

Python 3.10+는 `match-case` 문을 제공합니다 (더 강력한 패턴 매칭).

**Python 예제:**
```python
# Python 3.10+ match-case 문
day = 3

match day:
    case 1:
        dayName = "월요일"
    case 2:
        dayName = "화요일"
    case 3:
        dayName = "수요일"
    case _:
        dayName = "알 수 없음"

print(dayName)  # 수요일
```

### Python 3.10 이전 버전의 대체 방법

**Python 예제:**
```python
# 딕셔너리 사용
day = 3
day_names = {
    1: "월요일",
    2: "화요일",
    3: "수요일"
}
dayName = day_names.get(day, "알 수 없음")
print(dayName)  # 수요일
```

**비교 설명:**
- JavaScript는 전통적인 `switch-case` 문을 제공합니다.
- Python 3.10+는 `match-case` 문을 제공합니다 (더 강력한 패턴 매칭).
- Python 3.10 이전 버전에서는 딕셔너리나 if-elif 체인을 사용합니다.
- JavaScript의 `switch`는 `break`가 없으면 fall-through가 발생하지만, Python의 `match-case`는 그렇지 않습니다.

## 실습 예제

```python
# 논리 연산자 예제
age = 25
has_license = True
has_car = False

if age >= 18 and has_license:
    print("운전 가능합니다")
    if has_car:
        print("차량도 있습니다")
    else:
        print("차량은 없습니다")

# 삼항 연산자 예제
score = 85
result = "합격" if score >= 60 else "불합격"
print(f"점수: {score}, 결과: {result}")

# match-case 예제 (Python 3.10+)
day = 3
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("평일입니다")
    case 6 | 7:
        print("주말입니다")
    case _:
        print("알 수 없는 요일입니다")
```

## 요약

### Python
- **논리 연산자**: `and`, `or`, `not` 키워드 사용
- **삼항 연산자**: `값1 if 조건 else 값2` 형식
- **match-case**: Python 3.10+에서 패턴 매칭 지원
- 논리 연산자는 키워드이므로 가독성이 좋음

### JavaScript
- **논리 연산자**: `&&`, `||`, `!` 기호 사용
- **삼항 연산자**: `조건 ? 값1 : 값2` 형식
- **switch-case**: 여러 값에 대한 분기 처리 지원
- 논리 연산자는 단락 평가를 지원

### 주요 차이점
- Python은 키워드 기반 논리 연산자, JavaScript는 기호 기반 논리 연산자
- Python 3.10+는 `match-case`를 제공하지만, JavaScript는 전통적인 `switch-case` 사용
- Python의 삼항 연산자는 조건이 중간에, JavaScript는 조건이 앞에 위치

## 직접 해보기
1. 논리 연산자를 사용해 나이가 18세 이상이고 면허가 있는 경우에만 "운전 가능"을 출력하는 코드를 작성하세요.
2. 삼항 연산자를 사용해 점수가 60점 이상이면 "합격", 아니면 "불합격"을 변수에 저장하세요.
3. `match-case`를 사용해 요일 문자열에 따라 다른 메시지를 출력하는 코드를 작성해 보세요(Python 3.10 이상).

