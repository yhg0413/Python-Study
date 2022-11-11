#문제 컴퓨터가 1~100사이의 정수값을 하나를 랜덤하게 선택 사용자가 그 번호를 맞추는 것 최대 시도 횟수는 5회
import random


def rand(start, end):
    return int(random.random()*(end-start+1))+start

def colleting(com):
    ansel = 0
    for i in range(1,6):
        print(i,"번째 추측값", end="")
        ansel = int(input())
        # ansel = int(input(str(i) + "번째 추측값: "))
        # result = com - ansel
        #if result == 0
        if com == ansel:
            print("정답입니다")
            break
        elif com > ansel:
            print(ansel, "보다는 큽니다.")
        else:
            print(ansel, "보다는 작습니다.")
    if com-ansel != 0:
        print("실패했습니다, 증답은", com)


def main():
    colleting(rand(1,100))

main()