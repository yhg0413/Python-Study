def test(str):
        score = int(str)
        print(score)


def work():
    str = "89점"
    try:
        test(str)
    except Exception as e:
        print(e) #Exception 모든 에러에서 반응 함
    print("작업완료")


def work2():
    str = "89"
    try:
        test(str)
    except ValueError as e:
        e.print()
        print(e)
    except IndexError as e:
        e.print()
        print(e)
    print("작업완료")
###### raise : 개발자에 의 해 임의로 예외를 발생시킴

def calcsum(n):#주의 사항 raise에서 발생시큰 예외객체와 except예외 객체와 같아야한다
    if n < 0:
        raise ValueError

    total = 0
    for i in range(n+1):
        total += i
    return total


def main():
    work()# 이경우는 이렇게 테스트 함수 안쓰고 안에서 따로 돌리는게 낫다고함
    work2()

    try:
        print("~10=", calcsum(10))
        print("~-5=", calcsum(-5))
    except ValueError:
        print("입력값이 잘못되었습니다.")

main()