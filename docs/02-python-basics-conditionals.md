# Python 기초: 조건문

## 개요

조건문은 조건에 따라 다른 코드를 실행할 수 있게 해줍니다. Python과 JavaScript 모두 유사한 조건문 구조를 가지고 있지만, 문법과 동작 방식에 차이가 있습니다.

## 기본 if 문

**Python 예제:**
```python
# 기본 if 문
age = 20

if age >= 18:
    print("성인입니다")
```

**JavaScript 예제:**
```javascript
// 기본 if 문
let age = 20;

if (age >= 18) {
    console.log("성인입니다");
}
```

**비교 설명:**
- Python은 콜론(`:`)과 들여쓰기로 블록을 구분합니다.
- JavaScript는 중괄호(`{}`)로 블록을 구분합니다.
- Python은 조건식에 괄호가 필요 없지만, JavaScript는 괄호가 필요합니다.
- Python은 들여쓰기가 문법의 일부이지만, JavaScript는 들여쓰기가 선택사항입니다.

## if-else 문

**Python 예제:**
```python
# if-else 문
age = 15

if age >= 18:
    print("성인입니다")
else:
    print("미성년자입니다")
```

**JavaScript 예제:**
```javascript
// if-else 문
let age = 15;

if (age >= 18) {
    console.log("성인입니다");
} else {
    console.log("미성년자입니다");
}
```

**비교 설명:**
- 두 언어 모두 `if-else` 구조가 동일합니다.
- Python은 `else:` 뒤에 콜론이 필요합니다.
- JavaScript는 `else` 뒤에 중괄호가 필요합니다.

## if-elif-else 문

여러 조건을 확인할 때 사용합니다.

**Python 예제:**
```python
# if-elif-else 문
score = 85

if score >= 90:
    print("A등급")
elif score >= 80:
    print("B등급")
elif score >= 70:
    print("C등급")
else:
    print("D등급")
```

**JavaScript 예제:**
```javascript
// if-else if-else 문
let score = 85;

if (score >= 90) {
    console.log("A등급");
} else if (score >= 80) {
    console.log("B등급");
} else if (score >= 70) {
    console.log("C등급");
} else {
    console.log("D등급");
}
```

**비교 설명:**
- Python은 `elif` 키워드를 사용합니다.
- JavaScript는 `else if`를 사용합니다 (두 단어로 구분).
- 두 언어 모두 여러 조건을 체인으로 연결할 수 있습니다.

## 중첩 조건문

조건문 안에 조건문을 사용할 수 있습니다.

**Python 예제:**
```python
# 중첩 조건문
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("운전 가능합니다")
    else:
        print("면허가 필요합니다")
else:
    print("미성년자는 운전할 수 없습니다")
```

**JavaScript 예제:**
```javascript
// 중첩 조건문
let age = 25;
let hasLicense = true;

if (age >= 18) {
    if (hasLicense) {
        console.log("운전 가능합니다");
    } else {
        console.log("면허가 필요합니다");
    }
} else {
    console.log("미성년자는 운전할 수 없습니다");
}
```

**비교 설명:**
- 두 언어 모두 중첩 조건문을 지원합니다.
- Python은 들여쓰기로 중첩 레벨을 구분하고, JavaScript는 중괄호로 구분합니다.

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

## switch 문 (JavaScript만)

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

**Python에서 switch 대체:**
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

# Python 3.10 이전 버전에서는 딕셔너리 사용
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

### 예제 1: 점수 등급 판정

**Python 예제:**
```python
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

scores = [95, 87, 72, 65, 45]
for score in scores:
    print(f"점수: {score}, 등급: {get_grade(score)}")
```

**JavaScript 예제:**
```javascript
function getGrade(score) {
    if (score >= 90) {
        return "A";
    } else if (score >= 80) {
        return "B";
    } else if (score >= 70) {
        return "C";
    } else if (score >= 60) {
        return "D";
    } else {
        return "F";
    }
}

let scores = [95, 87, 72, 65, 45];
scores.forEach(score => {
    console.log(`점수: ${score}, 등급: ${getGrade(score)}`);
});
```

### 예제 2: 사용자 입력 처리

**Python 예제:**
```python
# 사용자 입력을 받아 조건 확인
age = int(input("나이를 입력하세요: "))

if age < 0:
    print("잘못된 입력입니다")
elif age < 13:
    print("어린이입니다")
elif age < 20:
    print("청소년입니다")
elif age < 65:
    print("성인입니다")
else:
    print("노인입니다")
```

**JavaScript 예제:**
```javascript
// 브라우저 환경에서 사용자 입력 받기
let age = parseInt(prompt("나이를 입력하세요: "));

if (age < 0) {
    console.log("잘못된 입력입니다");
} else if (age < 13) {
    console.log("어린이입니다");
} else if (age < 20) {
    console.log("청소년입니다");
} else if (age < 65) {
    console.log("성인입니다");
} else {
    console.log("노인입니다");
}
```

## 요약

### Python
- **조건문**: `if`, `elif`, `else`로 조건에 따른 분기 처리
- **논리 연산자**: `and`, `or`, `not` 키워드 사용
- **삼항 연산자**: `값1 if 조건 else 값2` 형식
- **match-case**: Python 3.10+에서 패턴 매칭 지원
- 들여쓰기로 블록을 구분하며, 콜론(`:`)이 필요함

### JavaScript
- **조건문**: `if`, `else if`, `else`로 조건에 따른 분기 처리
- **논리 연산자**: `&&`, `||`, `!` 기호 사용
- **삼항 연산자**: `조건 ? 값1 : 값2` 형식
- **switch-case**: 여러 값에 대한 분기 처리 지원
- 중괄호(`{}`)로 블록을 구분하며, 조건식에 괄호가 필요함

### 주요 차이점
- Python은 키워드 기반 논리 연산자, JavaScript는 기호 기반 논리 연산자
- Python은 들여쓰기로 블록 구분, JavaScript는 중괄호로 블록 구분
- Python 3.10+는 `match-case`를 제공하지만, JavaScript는 전통적인 `switch-case` 사용
- Python의 삼항 연산자는 조건이 중간에, JavaScript는 조건이 앞에 위치

