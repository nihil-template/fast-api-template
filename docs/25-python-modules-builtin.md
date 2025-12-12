# Python 기초: 내장 모듈

> JavaScript 비교는 참고용입니다. Python 모듈 사용에 집중하려면 Python 예제만 실행해도 됩니다.

## 개요

Python은 많은 내장 모듈을 제공합니다. 자주 사용하는 내장 모듈들을 학습합니다.

## math 모듈

수학 함수를 제공합니다.

```python
import math

print(math.pi)        # 3.141592653589793
print(math.sqrt(16))  # 4.0
print(math.pow(2, 3)) # 8.0
```

## datetime 모듈

날짜와 시간을 다룹니다.

```python
from datetime import datetime, date

# 현재 날짜와 시간
now = datetime.now()
print(now)  # 2024-01-15 10:30:45.123456

# 날짜만
today = date.today()
print(today)  # 2024-01-15

# 날짜 포맷팅
formatted = now.strftime("%Y년 %m월 %d일 %H시 %M분")
print(formatted)  # 2024년 01월 15일 10시 30분
```

## random 모듈

난수를 생성합니다.

```python
import random

# 0과 1 사이의 난수
print(random.random())

# 정수 범위의 난수
print(random.randint(1, 10))

# 리스트에서 랜덤 선택
fruits = ["사과", "바나나", "오렌지"]
print(random.choice(fruits))

# 리스트 섞기
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)
```

## os 모듈

운영체제 관련 기능을 제공합니다.

```python
import os

# 현재 작업 디렉토리
print(os.getcwd())

# 환경 변수
print(os.getenv("PATH"))

# 파일 존재 확인
print(os.path.exists("file.txt"))

# 파일 경로 조작
path = os.path.join("folder", "file.txt")
print(path)  # folder/file.txt (또는 folder\file.txt)
```

## 요약

### Python
- **math**: 수학 함수
- **datetime**: 날짜와 시간
- **random**: 난수 생성
- **os**: 운영체제 관련 기능

## 직접 해보기
1. `random` 모듈을 사용해 주사위를 10번 굴려 평균값을 출력하세요.
2. `datetime` 모듈을 사용해 현재 날짜와 시간을 포맷팅해 출력하세요.

