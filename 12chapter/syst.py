#시스템 읽기전용

#port sys
import sys
print("버젼:",sys.version)
print("플렛폼",sys.platform)
print("바이트 순서", sys.byteorder)
for i in sys.path:
    print("모듈 경로 ", i)
#sys.exit(0) 걍 끝내버림
#sys.exit(-1) 하면 맨마지막에 exit코드 -1이라고 뜸
#모듈 경로  C:\Users\i\anaconda3\envs\12chapter\lib 이부분에 저거있음 함수들

print(sys.argv) # 파일경로.인자1 ,인자2
#개발 완료시엔 파이참으로 실행하지 않음
#가장 첫번쨰줄은 실행시킨 파이선파일명이 나옴