import random
#x와 y의 값을 교환하세요

x = 10
y = 20
z = x
x = y
y = z

print('x : ', x)
print('y : ', y)


#가위 바위 보 게임 만들기

me = input('가위 바위 보 중 입력하십시오')
com = 2

if me == '가위':
    me = 1
elif me == '바위':
    me = 0
elif me == '보':
    me = 2
else:
    print("잘못 됀 입력입니다.")

print(me, com,sep = "<--나  컴퓨터-->")

if me == com:
    print("비겼습니다.")
elif (me == 1 and com == 2) or (me == 0 and com == 1) or (me == 2 and com == 0):
    print("나의 승리")
else:
    print("나의 패패")

#강사님꺼 0:rock, 1: scissors, 2: paper
#com = 0
#me = 1

# if com == me:
#   print("비겻습니다.")
# elif com == 0:
#   if me == 1: print("컴터 승.")
#   else: print("내가 이겻.")
# elif com == 1:
#   if me == 0: print("내가 이겻")
#   else: print("컴터 승.")
# elif com == 2:
#   if me == 0: print("컴터 승.")
#   else: print("내가 이겼.")
#좋은 코드는 아니라함 컴터가 뭐냈는지 알기위해서 위로 가야해서 별로 안좋은거임
#한눈에 봐도 알수있게 만들어야 좋은 코드

#강사님꺼 0:rock, 1: scissors, 2: paper
com = int(random.random()*10)%3
me = int(input("0:주먹, 1:가위, 2:보"))
ROCK = 0
SCISSORS = 1
PAPER = 2
#대문자와 소문자의 차이 대문자는 변하지 않을 상수처럼 계속쓸 변수
#소문자는 언제든 변하는 변수로 써서 가독성에 차이로 저장하는듯
#파이썬은 상수 선언이 없어서 이렇게 사용한다고함.
if com == me:
   print("비겻습니다.")
elif com == ROCK:
   if me == PAPER: print("내가 승.")
   else: print("컴터 승.")
elif com == SCISSORS:
   if me == ROCK: print("내가 이겻")
   else: print("컴터 승.")
elif com == PAPER:
   if me == ROCK: print("컴터 승.")
   else: print("내가 이겼.")
#이렇게 하는게 가독성 좋게 만든 코드.