#if 조건문
#단일 라인 표현식
#if 조건 : 명령
#파이썬은 들여쓰기로 반복문이나 조건문에 그 조건이나 반복에 속한다고 표현함
#age = int(input("나이를 입력하세요 : "))

#if age < 19:
 #   print("애들은 가라")

#비교 연산자

a = 3

if a == 3:
    print('3이다')
if a > 5:
    print('5보다 크다')
if a < 5:
    print('5보다 작다')

#문자열에 비교연산자

country = "Korea"

if country == "Korea":
    print("한국입니다")
if country != "Korea":
    print("한국이 아닙니다")

if "korea" > "japan":
    print("한국이 더 크다")
if "korea" < "japan":
    print("일본이 더 크다")
#문자열끼리는 글자 하나하나 빼서 계산함 형변환으로는 계산 불가

#거짓값 * * * * * * * * *
# False
# None
# 0
# "" : 비어있는 문자열
# [],() : 비어있는 컬렉션

print(None, bool(None))
print(0, bool(0))
print("", bool(""))
print([], bool([]))
print((), bool(()))

#if 조건문 논리연산자

a = 3
if a > 1 and a <10:
    print('ok')
# 1 < a < 10 랑 같은데 비교하는 대상을 줄임으로써 속도를 높이는 쇼트 서기트기법 파이썬만 이 표현가능
# 다른언어는 1<a<10 이렇게 안해줌

a = 3
b = 5
if a == 3 or b == 4:
    print('ok')

# 블록 구조
# if문의 명령이 여러 줄인 경우
# 이들 명령은 모두 동일한 들여쓰기를 해야함

#else 문
#if문에서 조건이 False인 경우 실행할 명령 지정
age = input("당신의 나이는?")
if int(age) < 19:#콜론은 새로운 코드 블록이 필요하단거 들여쓰기가 새로 올거라고 하는거라고함
    print("애들은 가라")
    print("공부 열심히 하세요")
else:
    print("어서 옵쇼")
    print("즐거운 시간 되세요")

#elif 문 걍 elseif임 ㅇㅋ 조건쓰고 클론 잊지말기

test = input("점수") # test = int(input("점수")) 이게 맞음
a = int(test)
if a == 100:
    print("와 백점 A +")
elif a >= 90:
    print("A")
elif a >= 80:
    print("B")
elif a >= 70:
    print("C")
else:
    print("F")



money = 6500
if money >= 20000:
    print("탕탕탕탕수육")
elif money >= 10000:
    print("쟁쟁쟁반자장")
elif money >= 6000:
    print("짬뽕")
elif money >= 4000:
    print("자장면")
else:
    print("단무지")

#if문 중복

man = 0
age = 2
if man == True:
    if age > 19:
        print("성인 남자입니다")
    else:
        print("미성년 남자입니다")
else:
    if age > 19:
        print("성인 여자입니다")
    else:
        print("미성년 여자입니다")
