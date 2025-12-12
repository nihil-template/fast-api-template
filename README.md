# Python 학습 가이드

이 저장소는 **완전 초보를 위한 Python 기초 커리큘럼**을 담고 있습니다. 아래 순서를 따라서 문서 → 노트북 → 실습 스크립트를 번갈아 가며 학습하면 됩니다.

## 준비물
- Python 3.10 이상 설치 (권장: [python.org](https://www.python.org/downloads/))
- 터미널 또는 명령 프롬프트
- 코드 편집기 (VS Code 권장)
- 선택: Jupyter Notebook / VS Code의 노트북 뷰어

### 가상환경 생성 (선택)
```bash
python -m venv .venv
source .venv/bin/activate  # Windows는 .venv\Scripts\activate
pip install --upgrade pip
```

## 저장소 구조
| 경로 | 설명 |
| --- | --- |
| `docs/` | 각 장의 개념 정리 (마크다운) |
| `notebooks/` | 동일 주제를 실습할 수 있는 Jupyter 노트북 |
| `training/` | 각 장과 1:1로 대응되는 Python 스크립트 실습 |

> 문서에는 Python과 JavaScript 비교가 함께 들어있습니다. **JavaScript 경험이 없다면 Python 코드와 설명만 읽고 넘어가도 무방**합니다.

## 추천 학습 순서
1. `docs/00-getting-started.md` – 환경 설정과 학습법 점검
2. `docs/01-python-basics-types.md`부터 순서대로 읽어 개념 이해
3. 같은 주제의 `notebooks/0X-...ipynb`를 열어 셀을 직접 실행
4. `training/X.*.py`를 실행해 터미널에서 결과 확인
5. 스스로 예제를 변형해 보고, 이해가 부족하면 다시 문서를 참고

### 문서 구조
각 문서는 하나의 개념만 학습할 수 있도록 구성되어 있습니다:
- **01-04**: 타입과 변수 (기본 타입, 변수, 타입 확인, 타입 변환)
- **05-06**: 조건문 (조건문, 논리 연산자)
- **07-10**: 반복문 (for, while, 제어, 고급 기법)
- **11-12**: 자료구조 (리스트, 딕셔너리)
- **13-17**: 함수 (기본, 매개변수, 람다, 스코프, 문서화)
- **18-23**: 클래스 (기본, 변수, 메서드, 상속, 특수 메서드, 캡슐화)
- **24-26**: 모듈 (기본, 내장 모듈, 고급)
- **27-28**: 패키지 (기본, 고급)

### 실습 스크립트 실행
```bash
python training/1.variable.py
python training/2.if.py
# ...
```

실행 결과가 예상과 다르면 스크립트를 수정해 다시 실행해 보세요. 노트북 또한 `jupyter notebook notebooks/01-...ipynb` 또는 VS Code로 열어 코드를 직접 실행할 수 있습니다.

## 추가 팁
- 각 장 뒤에는 “직접 해보기” 과제가 포함되어 있으니 반드시 손으로 따라 하세요.
- 궁금한 내용은 Python 공식 문서(https://docs.python.org/3/)를 병행 참고하면 좋습니다.
- 학습 중 모르는 용어가 나오면 README에 메모하거나 Issues로 정리해 두면 복습에 도움이 됩니다.
