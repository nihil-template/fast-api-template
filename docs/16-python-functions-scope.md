# Python 기초: 함수 스코프

> JavaScript 비교는 참고용입니다. Python만 실습하려면 Python 예제와 설명 위주로 읽고, `notebooks/04-python-functions.ipynb`와 `training/4.functions.py`에서 함수를 직접 작성해 보세요.

## 개요

스코프는 변수가 어디에서 접근 가능한지를 결정합니다. Python에서는 `global`과 `nonlocal` 키워드로 변수 스코프를 제어할 수 있습니다.

## 지역 변수와 전역 변수

```python
# 전역 변수
global_var = "전역 변수"

def my_function():
    # 지역 변수
    local_var = "지역 변수"
    print(global_var)  # 전역 변수 접근 가능
    print(local_var)

my_function()
# print(local_var)  # 오류! 지역 변수는 함수 밖에서 접근 불가
```

## global 키워드

함수 내에서 전역 변수를 수정할 때 사용합니다.

```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # 1

# global 없이 사용하면 지역 변수로 인식됨
def increment_wrong():
    count = count + 1  # 오류! 지역 변수 count가 정의되기 전에 사용

# increment_wrong()  # UnboundLocalError 발생
```

## nonlocal 키워드

중첩 함수에서 외부 함수의 변수를 수정할 때 사용합니다.

```python
def outer():
    x = "외부 함수"
    
    def inner():
        nonlocal x
        x = "내부 함수에서 수정"
        print(x)
    
    inner()
    print(x)

outer()
# 출력:
# 내부 함수에서 수정
# 내부 함수에서 수정
```

## 요약

### Python
- **지역 변수**: 함수 내에서만 접근 가능
- **전역 변수**: 어디서나 접근 가능
- **global**: 전역 변수 수정 시 사용
- **nonlocal**: 중첩 함수에서 외부 함수 변수 수정 시 사용

## 직접 해보기
1. 전역 변수를 선언하고 `global` 키워드를 사용해 함수 내에서 수정해 보세요.
2. 중첩 함수를 만들고 `nonlocal` 키워드를 사용해 외부 함수의 변수를 수정해 보세요.

