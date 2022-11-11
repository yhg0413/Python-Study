#예외 처리
#복구가 불가능한 것을 에러 라고 부르고
#복구가 가능한 것을 예외 라고한다
#예외가 발생했을때 디폴트는 종료인데 명령을 줄시 다른걸 술수있음
#예외 발생을 감지하고 복수하는 방법을 예외 처리라고 함
#예외의 종류
#NameError :명칭이 업거나 초기화되지 않은 변수를 사용할떄 나옴
#ValueError : 타입은 맞지만 값의 형식이 잘못되었다
#ZeroDivisonError # 0을 나눈 경우
#IndexError : 첨자 범위를 벗어남
#TypeError : 타입이 맞지않아. 숫자가 필요한곳에 문자열등을 사용한 경우
#try:
#   실행할 명령 (시도
#except 예외 as 변수: (실패
#   오류 처리문
#else: (성공 옵션임 안써도 괜찮음
#   예외가 발생하지 않을 때의 처리

str = "89점"
try:
    score = int(str)
    print(score)
except:
    print("예외가 발생했습니다.")
print("작업 완료")#트라이 익셉트 필요할떄 자주 쓰기

#예외 발생을 감지하고 복구하는 방법
str = "89"
try:
    score = int(str)
    print(score)
    a = str[5] #에러 발생
except ValueError:
    print("점수의 형식이 잘 못 되었습니다.")
except IndexError:
    print("첨자 범위를 벗어남")

try:
    score = int(str)
    print(score)
    a = str[5] #에러 발생
except (ValueError, IndexError):#편하게 쓰는대신 구체적 오류를 확인 불가
    print("점수의 형식이나 첨자 범위를 벗어났습니다.")

str = "89점"
try:
    score = int(str)
    print(score)
except ValueError as e:#좀더 구체적인 뭐가 잘못됐는지 알수있음
    print(e)
except IndexError as e:
    print(e)
print("작업완료")