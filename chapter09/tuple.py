#튜플
#불변 자료 집합
# (값, ...)
# 값, [...]
#추가/수정/삭제 불가
#읽기만 가능 --> 리스트보다 속도가 빠름
import time

def gettime():
    now = time.localtime()
    return now.tm_hour, now.tm_min


def tt():
    score = 88, 95, 70, 100, 99  # 이렇게해도 받아들임 튜플은
    print(score)

    score = 88,  # 한개짜리 튜플 만들땐 무조건 콤마붙이기
    print(score)

    score = (88,)
    print(score)

    score = (88)#이건 그냥 괄호 연산자일뿐 튜플이 되지않음
    print(score)

    score = 88
    print(score)

#튜플로 가능한 일

def tu():
    tu = 1,2,3,4,5
    print(tu[3])
    print(tu[1:4])
    print(tu+(6,7))#이거같은경우 수정이아니라 그 데이터로 리턴값을 받은거임
    print(tu * 2)
#데이터 삽입이나 삭제는 불가능 ex
#tu[1] = 100
#del tu[1]

#튜플만의 고유 기능

def tutu():
    names = "이순신", "김유신", "강감찬"
    lee, kim, kang = names #unpack #이게 순서대로 대입됌
    #lee = 이순신 kim = 김유신 kang =강감찬 이거랑 똑같음 언팩기능
    print(lee)
    print(kim)
    print(kang)

    a, b = 12, 34
    print(a,b)

    a,b = b,a
    print(a,b)
    #a,b = fun() 이 가능함 단 조건 fun이 요소 두개짜리 튜플을 리턴해야함
    #리턴하는요소의 갯수와 리턴받는요소의 갯수가 같아야함
    #def fun():
    #. . .
    #return (10,20) 이런식으로로 괄호가 없어도 통용 됌


def main():#튜블을 사용하는경우 읽기전용 리스트 만들떄 아니면 복수의 정보를 리턴하고 개별변수에 지정하고싶을때
    tt()
    tu()
    tutu()

    result = gettime()
    print(f"지금은 {result[0]}시 {result[1]}분입니다.")
    hour, minute = gettime()
    print(f"지금은 {hour}시 {minute}분 입니다.")

    d, m = divmod(7,3)

    print("몫", d)
    print("나머지",m)

    score = [88,95,70,100,99]
    tue = tuple(score)
    print(tue)

    li = list(tue)
    li[0] = 100
    print(li)

main()