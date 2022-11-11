import random


def rand(start, end=100):
    return int(random.random()*(end-start+1))+start

def printHangman(Lines, i):
    for Line in Lines[:i]:
        print(Line)

def main():
    HANGMAN = """
---+
   ㅣ
   ㅇ
  /ㅣ\\
  / \\
"""
    com = rand(1, 100)
    Hangdata = HANGMAN.splitlines()
    Hangdata.pop(0) #첫번째 줄을 제거(비어있는 줄을 뺌)
    for i in range(1,8):
        mya = int(input(str(i)+"번째 추측값"))
        result = com - mya
        if result==0:
            print("정답입니다.")
            break
        elif result < 0:
            print("보다는 작습니다.")
            printHangman(Hangdata, i)
        else:
            print("보다는 큽니다")
            printHangman(Hangdata, i)
    if result != 0:
        print("정답은" + str(com)+"입니다")


#꼭꼭 곱씹기
main()