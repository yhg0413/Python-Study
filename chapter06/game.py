import random
#강사님꺼 0:rock, 1: scissors, 2: paper
ROCK = 0
SCISSORS = 1
PAPER = 2
mwin = 0
cwin = 0
for i in range(3):
    com = int(random.random()*10)%3
    #com = int(random.random()*3) 위랑 같은 결과 random()은 0~0.999999사이 숫자만 나옴
    me = int(input("0:주먹, 1:가위, 2:보"))

#대문자와 소문자의 차이 대문자는 변하지 않을 상수처럼 계속쓸 변수
#소문자는 언제든 변하는 변수로 써서 가독성에 차이로 저장하는듯
#파이썬은 상수 선언이 없어서 이렇게 사용한다고함.
    print(i+1, "번째 판은", end = " ")
    if com == me:
      print("비겻습니다.")
    elif com == ROCK:
        if me == PAPER:
            print("내가 승.")
            mwin += 1
        else:
            print("컴터 승.")
            cwin += 1
    elif com == SCISSORS:
        if me == ROCK:
            print("내가 이겻")
            mwin += 1
        else:
            print("컴터 승.")
            cwin += 1
    elif com == PAPER:
        if me == ROCK:
            print("컴터 승.")
            cwin += 1
        else:
            print("내가 이겼.")
            mwin += 1
print("나의 승 :", mwin, "컴터 승 :", cwin, "무승부 :", 3-mwin-cwin)
if mwin == cwin:
    print("최종 비김")
elif mwin > cwin:
    print("최종 내가 이김")
else:
    print("최종 컴터가 이김")

#이렇게 하는게 가독성 좋게 만든 코드.