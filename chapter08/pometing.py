#포맷팅
# ○ %d 정수
# ○ %f 실수
# ○ %s 문자열
# ○ %c 문자 하나
# ○ %h 16진수
# ○ %o 8진수
# ○ %% % 문자
# ○ %[-]폭[.유효자리수]서식, 폭에는 소수점에 포함 , 반올림 발생
def intpo():
    price = 500
    print("궁금하면" + str(price) + "원")
    # 불편 그래서 그거야 우리 하던거 드디어!

    mont = 8
    day = 15
    anni = "광복절"
    print("%d월 %d일은 %s이다." % (mont, day, anni))  # 파이썬 2버전 스타일
    # 파이썬 3버전은 다르게 쓴다고함

    ## 자리수 잡기
    value = 123
    print("###%d###" % value)
    print("###%5d###" % value)
    print("###%10d###" % value)
    print("###%-10d###" % value)
    print("###%1d###" % value)  # 입렵된 값보다 설정값이 작으면 그냥 입력됀 값이 나옴

    price = [30, 13500, 2000]
    for p in price:
        print("가격 : %d원" % p)
    print()
    for p in price:
        print("가격 : %7d" % p)
    print()
    for p in price:
        print("가격 : %-7d" % p)
    # 이런식으로 정렬해서 쓰는데 사용

def folatpo():
    # 실수 포맷팅
    f = 123.1234567
    print("%10f" % f)  # 전체자리수 10개
    print("%10.8f" % f)  # 전체자리수 10개 소수점 자리수는 8개까지 총 11자리인데 10자릴 넘지만 더 커서 그냥 더 큰값으로써짐
    print("%10.5f" % f)  # 반올림이 일어남
    print("%10.2f" % f)
    print("%.2f" % 123.126)  # 앞자린 신경안쓰고 소수점 개수만 조절하는 방식
def main():
    # 파이썬 3부터 쓰는 선형포매팅 이전까진 파이썬 2에서썻음
    # "{[:포맷문자열]} ".format(값...)
    name = "한결"
    age = 16
    height = 162.5
    print("이름:{}, 나이:{}, 키:{}".format(name,age,height))#타입을 설정 안해도 상관없을때
    print("이름:{:s}, 나이:{:d}, 키:{:f}".format(name, age, height))#타입만 설정 할때
    print("이름:{:4s}, 나이:{:3}, 키:{:.2f}".format(name, age, height))#타입이랑 자릿수까지 설정

    # "{인덱스[:포맷문자열]} ".format(값...)
    print("이름:{0}, 나이:{1}, 키:{2}".format(name, age, height))  # 인덱스 번호로 넣는거임
    print("이름:{2}, 나이:{0}, 키:{1}".format(name, age, height)) #인덱스 번호로 넣는거임
    #"{변수명[:포맷문자열]} ".format(값...)
    print("이름:{name}, 나이:{age}, 키:{height}".format(age=20, name="길동", height=160.9))  # 변수명 으로해서 넣는거

    #파이썬 3.6.부터 지원되는 포맷팅 개편하네 요즘애들은 다 이런식으로 포맷팅한데
    print(f"이름:{name}, 나이 : {age}, 키: {height:.2f}")

main()

#강조 기억해야 할것 문자열은 불변 개체다 ******************
#슬라이싱 *********************** [:] 범위주고 쪼개기
#스플릿 조인 **********
# 마지막에 배운 포맷 ********
