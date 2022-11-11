#모듈의 정의 (util.py) 파일명이 모듈이됌

#모듈 테스트
# __name__ 변수에 모듈명이 저장됌
# 단독으로 실행된 경우 (모듈로 상용된 것이 아님)
# "__main__"으로 지정됌
# 모듈로 사용된 경우 (import에 의해 실행됀경우)
# 파일명이 지정됌
#모듈 개발시 테스트 할수 있도록 지원
# 모듈 정의
# if __name__ == "__main__" :
#   모듈 테스트 코드

#import 몇번을 하든 단 한번만 실행 됌
import util #from util import INCH, calcsum
#from util import *            이름충돌이 일어나지않을거라는 확신 있을떄만 * 쓰기 (아스탈리스크)?
#print("1inch = ", INCH)
#print("~10 = ", calcsum(10))

if __name__ == "__main__":
    print("1inch = ", util.INCH)
    print("~10 = ", util.calcsum(10))