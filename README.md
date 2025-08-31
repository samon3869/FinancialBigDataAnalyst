## 1. 주피터 노트북 개발환경 세팅
### ① WSL 및 파이썬 가상환경 세팅
[WSL 및 파이썬 가상환경 세팅](https://github.com/samon3869/Costaurant/blob/main/env-settings.md)
### ② 주피터 노트북 커널 가상환경에 연결
```bash
# ① 가상환경 생성/활성화
pyenv activate fda_env

# ② 커널 패키지 설치
pip install ipykernel

# ③ 커널 등록 (가상환경 내부에만)
python -m ipykernel install --sys-prefix --name fda_env --display-name "Python 3.11.9 (fda_env)"
``` 

> [!TIP]
> 커널 등록 코드 설명 (가상환경 전용)
>
> **python -m ipykernel install --sys-prefix**:
> 현재 활성 파이썬(=가상환경)의 ipykernel로 그 가상환경 내부에 커널 명세(kernelspec)를 만듭니다. → 커널이 환경과 함께 관리·삭제되어 유령 커널이 남지 않습니다.
>
> 설치 위치(예)
> > \<env>/share/jupyter/kernels/\<name>/kernel.json
예: ~/.pyenv/versions/3.11.9/envs/fda_env/share/jupyter/kernels/fda_env/kernel.json
> 
> **--name myenv**: 커널 디렉토리/ID 이름(내부 식별자).
> 
> **--display-name "Python (myenv)"**: 주피터/VS Code 커널 선택 메뉴에 보여질 이름.


## 2. 파이썬 모듈 검색 경로

```python
import sys, pprint
pprint.pp(sys.path)
```

/home/bbang2/.pyenv/versions/3.11.9/lib/python311.zip
→ 표준 라이브러리(zip 형태). zipimport로 압축된 stdlib 모듈을 읽어올 수 있게 넣어둔 경로예요(환경에 따라 있을 수도, 없을 수도).

/home/bbang2/.pyenv/versions/3.11.9/lib/python3.11
→ 표준 라이브러리(순수 파이썬) 디렉터리. json, pathlib 같은 기본 모듈들이 여기 있어요.

/home/bbang2/.pyenv/versions/3.11.9/lib/python3.11/lib-dynload
→ **C로 빌드된 확장 모듈(.so)**이 있는 곳. 예: math, unicodedata 같은 내장 확장 모듈들이 여기서 로드돼요.

'' (빈 문자열)
→ 현재 작업 디렉터리(대화형은 CWD, 스크립트 실행 시 스크립트가 있는 폴더).

주의: 여기 경로에 json.py 같은 파일이 있으면 **표준 라이브러리와 이름 충돌(섀도잉)**이 납니다.
/home/bbang2/.pyenv/versions/fda_env/lib/python3.11/site-packages
→ 가상환경(fda_env)의 site-packages. pip install한 서드파티 패키지들이 여기에 깔려요.


> [!TIP]
> 탐색 순서 = 리스트 순서. 먼저 찾는 모듈이 이깁니다.
> 빈 문자열('') 때문에 로컬 파일명이 표준/설치 패키지와 같으면 충돌할 수 있어요.
> .pth 파일이나 PYTHONPATH가 있으면 sys.path에 추가 경로가 들어올 수 있습니다.

## 3. 필요 라이브러리 기재

### ① 현재 환경에 설치된 패키지 전부 기재(requirements.txt)하는 방식

```bash
# 1) 필요한 패키지 설치
pip install pandas

# 2) 현재 환경을 고정해 저장
pip freeze > requirements.txt
```

### ② 상위 패키지만 명시(requirements.in)하고 하위패키지는 자동기재(requirements.txt)

```bash
# 1) pip-tools 설치
pip install pip-tools

# 2) 상위 패키지 명시
cat > requirements.in <<'REQ'
pandas
matplotlib
cerp
distfit
scipy
geneticalgorithm
benfordslaw
networkx
REQ

# 3) 하위 패키지포함하여 자동 기재
pip-compile --generate-hashes requirements.in   # → requirements.txt 생성
```

> [!TIP] HEREDOC 문법
> cat : 표준입력(STDIN)을 받아 표준출력(STDOUT)에 그대로 내보내는 명령.
> requirements.in : cat의 출력을 파일로 덮어쓰기(overwrite) 리다이렉션.
> <<'REQ' : heredoc 시작. 아래에 나오는 줄들을 표준입력으로 넘겨줌. 마지막에 딱 REQ만 적힌 줄을 만나면 입력 종료.
> 즉, “REQ와 REQ 사이의 내용을 requirements.in 파일로 저장해라”는 뜻이에요.

### ③ git clone후 라이브러리 세팅시

```bash
pip install -r requirements.txt
```
