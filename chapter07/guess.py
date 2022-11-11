import random

#파이썬은 함수명이랑 변수명이랑 겹쳐도 되기는함
def rand(start, end):
    number = int(random.random()*(end-start)) + start
    return number

def main():
    start = 1
    end = 6
    for i in range(5):
        number = rand(start,end)
        print(number)

main()#entry point 함수의 시작점 자바나 c의 int main(void) 이런거