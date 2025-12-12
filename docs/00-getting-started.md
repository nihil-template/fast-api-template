# 00. 학습 준비와 진행 방법

## 1. Python 설치 확인
```bash
python --version
```
- 3.10 이상이면 바로 진행
- 없다면 [python.org/downloads](https://www.python.org/downloads/)에서 설치

## 2. 필수 도구
- 터미널 또는 명령 프롬프트
- 코드 편집기(VS Code 권장) – 폰트 크기, 다크모드 등 미리 설정
- 선택: Jupyter Notebook(`pip install notebook`) 또는 VS Code의 Python 확장

## 3. 가상환경 활성화(권장)
```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install --upgrade pip
```
필요한 추가 패키지가 생기면 `pip install <패키지명>`으로 설치합니다.

## 4. 추천 학습 루틴
1. `docs/01-...md`를 읽으며 기본 개념 파악
2. 같은 번호의 `notebooks/0X-...ipynb`를 열어 셀을 직접 실행
3. `training/X.*.py`를 터미널에서 실행해 출력 확인
4. 각 장 “직접 해보기” 문제를 손으로 풀고, 변형/확장해 보기

### 노트북 실행
```bash
jupyter notebook notebooks/01-python-basics-types-variables.ipynb
```
또는 VS Code에서 `Open With > Notebook Editor`를 사용합니다.

### 실습 스크립트 실행
```bash
python training/1.variable.py
python training/2.if.py
# ...
```

## 5. 학습 중 참고 사항
- 문서에는 JavaScript 비교 설명이 함께 들어가 있습니다. **Python만 배우는 중이라면 비교 섹션은 건너뛰어도 괜찮습니다.**
- 헷갈리는 개념(예: `if`, `for`, `class`)은 Python 공식 문서나 `help()` 함수를 통해 추가로 확인하세요.
- 문제가 생기면 오류 메시지를 그대로 복사해 검색하거나 노트에 정리해 두면 복습이 쉬워집니다.
