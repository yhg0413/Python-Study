#가상환경(Virtual environment)

#파이썬에서는 한라이브러리에 대해 하나의 버전만 설치가 가능
# 여러개의 프로젝트를 진행하는 경우
# 프로젝트마다 동일 패키지에 대해 다른 라이브러리를 사용하는 경우 문제
#이를 방지하기 위한격리된 독립적인 가상환경을 제공
#일반적으로 프로젝트마다 다른 하나의 가상환경을 생성한 후 작업을 시작

#가상 환경을 만드는 대표적인 모듈
#ven: Python 3.3 버전 이후 부터 기본 모듈에 포함
#virtyalevn : phtyon 2.0버전 이후부터 사용 요즘 잘 안끔
#conda
#pyen


#가상환경 목록 보기
#conda env list : 생성된 가상환경들의 목록을 보여줌

#가상환경 만들기 : cmd에 쳐야함
#conda create --name <가상환경 이름> python = <파이썬 버전>
#conda create --name python_study pyhton=3.7
#                                 입렵안할시 3.8(최신)버저으로 자동 설치댐

#가상환경 활성화
#conda activate
#conda activate python_study
# 활성화되면 -> (python_study) C:\workspace

#가상환경 비활성화
#conda deactivate


#  가상 환경 삭제하기
# ○ conda remove --name <가상환경 이름> --all
# ○ conda remove --name python_study --all