#산술연산 +,-,*,/(/는 실수로 나누고 //는 정수로 나눔)
#** 은 제곱 % 나머지
print(3**3)
print(2**10)

print(5/2)
print(5//2)

print(7%2)
print(8%3)
print(9%3)

a = 0

if a%2 == 0:
    print("a 는 짝수")
else:
    print("a 는 홀수")
# 복합 대입 연산자 : 변수의 반복 사용을 줄여주는 축약 표현
# a += 1    a = a + 1

a = 5
a += 1
print(a)
a -= 2
print(a)
a *= 2
print(a)

# 문자열 연산 : 문자열 연결 (+)
s1 = "대한민국"
s2 = "만세"
print(s1 + s2)
# 문자열 연산 : 문자열 연결 (*) [문자열 * 숫자]
print("#" * 30)
print("싫어" * 3)
print("#" * 30)
print("+----" * 5 + "+")
print("싫어" * 3)
print("+----" * 5, end="+\n")

#타입 변환
#정수변환
s = "korea" + str(2002)
print(s)

print(10 + int("22"))
#실수나 텍스트가 int에 들어가면 못바꿈
print(int("1a", 16)) # 16진수를 10진수로 변환
print(int("15", 8)) # 8진수를 10진수로 변환

#실수변환 : float()
#round(숫자,[반올림 자리수]) : 실수 반올림 함수[안써도 됌 생략가능한 것]

print(int(2.54))
print(round(2.54))
print(round(2.54,1))
print(round(123456,-3))

#기타 타입변환
#bool() : 부울 변환함수
#list() : 리스트 변환 함수
#tuple() : 튜플 변환 함수
#dict() : 사전 변환 함수
