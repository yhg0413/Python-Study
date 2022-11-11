#표준묘듈
#임포트(import) 다른 파일에 정의된 변수, 함수, 객체 등을 사용하기 전에 이를 알리는 것
#표준 모듈 파이썬에서 제공하는 모듈
#import 모듈 [as 이름] 모듈의 이름을 별칭을 넣어서 편하게 쓰기휘한거 ex random.블라블라 -> r.블라블라
#from 모듈 import 함수명
#임포트하는 파일명이 겹칠경우에 계속 서로 찾기때문에 무한루프가 일어나서 파일명은 항상 안겹치게 만들기(내부파일과도 겹치면 안됌.)
#파일명이 모듈명이다
import math

print(math.sqrt(2))

from math import sqrt
print(sqrt(2))

import math as m
print(m.sqrt(2))

from math import sqrt as sq
print(sq(2))

#math 모듈
#상수
#pi : 원주율 상수
#tau : 원주율의 2배되는 상수
#e : 자연 대수 상수
#inf : 무한대 값
#nan : 숫자가 아닌 값
# 나머지는 책 보기 책에 많다262페이지
#반올림 round() 얘는 일반 함수임 math에 포함 안돼있음

print(m.sin(m.radians(45)))
print(m.sqrt(2))
print(m.factorial(5))

#통계 모듈, statistics
#함수
#mean() : 평균
#harmoni_mean() : 조화평균
#median() : 중앙 값, 짝수인 경우 보간값 계싼
#medain_low() : 나 머 지 책 봐264페이지