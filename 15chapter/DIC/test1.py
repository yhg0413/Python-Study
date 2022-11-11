#모듈 경로
#sys 모듈의 path 리스트를 먼저 조사
# 현재 어킹 디렉토리가 제일 먼저 조사 됌
# 그 다음 PYTHONPATH 환경 변수의 디렉터리 검색

import sys
import util

#import는 워킹디렉토리에서 찾음 파이참은 = 프로젝트 디렉토리
print(util.INCH)

for path in sys.path:
    print(path)
#시스템속성 -> 환경변수 -> 시스템변수 -> 새로만들기 -> 변수이름 PYTHONPATH 경로는 암대나