#함수와 인수
#함수 정의 def 함수명(인수목록):

def calcsum(n):
    total = 0
    for num in range(n+1):
        total += num

    return total


def calcrange(begin, end):
    total = 0
    for num in range(begin, end+1):
        total += num

    return total


print(" ~ 4 = ", calcsum(4))
print(" ~ 10 = ", calcsum(10))

print("3~7 = ", calcrange(3,7))


def printsum(n):
    total = 0
    for num in range(n+1):
        total +=num
    print("~",n,"=",total)

# return 값이 필요 없는경우
# 함수는 만들때 1가지 일만 하게 만드는게 좋음
printsum(4)
printsum(10)

#pass 아무것도 안하고 넘어감 함수는 반드시 코드블럭이 있어야함
# 실제 구현을 나중으로 미루고자 할 때 pass 지정

def calctotal():
    #나중에 완성할 것
    pass

