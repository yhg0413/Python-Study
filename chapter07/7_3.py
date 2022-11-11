#변수의 범위

#지역변수 그 지역변수 그거
total = 0

def calcsum(n):
    total = 0
    for num in range(n+1):
        total += num

    return total

#전역변수 그래 그거

def kim():
    temp = "김과장의 함수"
    print(temp)

def lee():
    temp = 2**10
    return temp
def park(a):
    temp = a*2
    print(temp)

kim()
print(lee())
park(5)
#print(temp)  지역변수인 temp를 사용하려 해서 안됌.


def mex(*num):
    temp = 0
    for i in num:
        if i>= temp : temp = i

    return temp

print(mex(100,2,4,888,3,6))

#즌역변수

salerate = 0.9

def kim():
    print("오늘의 할인율:", salerate)


def lee():
    price = 1000
    print("가격 :", price * salerate)

kim()
salerate = 1.1
lee()

price = 1000

def sale():
    #price = 500 이렇게하면 변수명 겹쳐서 안에껄로 계산됌
    global price
    price = 500
    print("sale", id(price))

sale()
print("global", id(price))
print(price)
#전역변수는 가급적 쓰지말것

#docstring
#함수의 도움말
#함수의 코드 불록 앞에 문자열로 지정
#help(함수명) 호출 시 출력될 문자열

def calcsum(n):
    """1~n까지의 합계를 구해 리턴한다 """
    total = 0
    for i in range(n+1):
        total = 1

        return total
help(calcsum)

def findMin(*num):
    temp = 100
    for i in num:
        if temp > i: temp = i

    return temp
def findMax(*num):
    temp = -999999
    for i in num:
        if temp < i: temp = i

    return temp
print(findMin(2,7,6,-1,20))
print(findMax(2,7,6,-1,20))


def swap(x, y):
    temp = y
    y = x
    x = temp

    print('x', x)
    print('y', y)

a = 10
b = 20

swap(a,b)

print('a', a)
print('b', b)