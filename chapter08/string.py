#문자열 분리
#첨자 문자열[정수] 0부터 인덱싱
#     문자열[-정수] 끝에서부터 인덱싱
# 문자열안에서 문자열과 문자열의 거리를 offset이라고 함

#슬라이씽

def lenpe():
    s = "python"

    print(s[2])
    print(s[-2])

    for c in s:#위 같은 경우는 컬렉션 안의 있는것들을 모두 사용할때까지 반복
        print(c, end=",")#켈력션은 시퀀스에 포함이 된다고함 Sequence 문자열 등등이 있다함
    print()
    for i in range(len(s)): #len() 문자열의 길이를 숫자로 바꾸는 함수
        print(s[i], end=",")
def slaising():#슬라이싱
    # 문자열[bigin:end:step] step의 디폴트 값은 1
    s = "0123456789"
    print(s[2:5])  # 인덱스의 2<5까지
    print(s[3:])  # 3부터 끝까지
    print(s[:4])  # 0부터 끝까지

    file = "20200101-104830.jpg"
    print("촬영날짜" + file[4:6]+"월", file[6:8]+"일")
    print("촬열시간" + file[9:11] + "월" + file[11:13] + "일")
    print("확장자 " + file[-3:])

    dates = "월화수목금토일"
    print(dates[::2])
    print(dates[::-1])
    d2 = dates[:]## 슬라이싱은 다른변수에 저장할시 문자열로 저장이 됌(추려낸 문자열)
    print(type(d2))
    #if str == str[::-1]: true 회문판독하기 ex토마도 문자열을 바로 하면 첫번째 글자를 먼저 비교해서 str[1]이 아니라 str도 유효



#문자열 매서드
#시퀀스 = 순서를 가지는 자료형 리스트 등은 전부 사용가능한 함수
#검색
#.find(str) : str 문자열을 찾아 인덱스를 반환, 없으면 -1 반환 (숫자로 몇번째인지 반환함)
#.rfind(str) : 뒤에서 str 문자열을 찾아 인덱스 반환, 없으면 -1 반환 마지막 쪽에있는걸 계산하는데 -가 아니라 +로 나옴
#.index(str) : find()와 동일, 없으면 예외 발생 없으면 오류남
#.count(str) : str 문자열이 몇번 등장하는지 리턴 .은 객체 라는 뜻(class)
#.연산자 = `이거래 누구누구의~ 란 뜻이라는듯


#조사
# 단어 in 문자열 -> bool  (in연사자임)
# 단어 not in 문자열 -> bool
# .startswith(str) -> bool == 함수보단 메서드 라고 부름 시작부터 입력된 문자열이 있을시
# .endswith(str) -> bool 참 아니면 거짓으로 나옴 끝부터 문자열이 있을시
def methed():

    #검색
    s = "python programing"
    print(len(s))
    print(s.find('o'))
    print(s.rfind('o'))
    print(s.index('i'))
    print(s.count('n'))

    #조사
    print('a' in s)
    print('z' in s)
    print('pro' in s)
    print('x' not in s)

    name = "홍길동"
    if name.startswith("홍"):
        print("홍씨입니다.")

    if name.startswith("김"):
        print("김씨입니다.")

    file = "figure.jpg"
    if file.endswith(".jpg"):
        print("JPG 그림 파일 입니다")


    #이렇게 입력 받을땐 항상 제대로 입력했는지 확인해야함

#기타 메서드
#isalpha            is로 시작하는 메서드는 전부다 bool로 나옴
#islower
#isupper
#isspace
#isalnum 영어랑 숫자로만 되어있느냐
#isdecimal
#isdigit 숫자로만 되어있느냐
#issumeric
#isidentifier
#isprintable
#나머지 메서드 교재에 있음 보셈 많다
def check():
    height = input("키 : ")
    if height.isnumeric():
        print("키 = ", height)
    else:
        print("숫자만 입력하세요")

#변경 문자열을 중간에 바꾸는게아니라 중간을 바꾼 전체를 바꿔버리는것
#s를 바꾸는게아니라 return값을 출력하는거임
#파이썬에서 문자열은 불변개체이고 읽는건 되지만 쓰기는 안됌(부분수정이 안됌)
def strchenge():
    s = "Good morning. my love KIM"

    #s = "hello"
    # s[2] = 'L'
    #print(s)

    print(s.lower())#전부 소문자로
    print(s.upper())#전부 대문자로
    print(s.swapcase())#소문자랑 대문제 바꿔
    print(s.capitalize())#첫 글자만 대문자 나머지는 다 소문자
    print(s.title())#모든 단어의 첫 글자를 대문자로 나머지는 소문자로 변환

    s = "    angel    "

    print(s + "님")
    print(s.strip()+"님")#공백제거
    print(s.lstrip() + "님")#공백 왼쪽제거
    print(s.rstrip() + "님")#공백 오른쪽제거

#분할
#.slpit(구분자)
#구분자를 기준을 단어를 분리하여 리스트로 리턴, 디폴트는 공백
#.splitlines()
#개행 문자(\n)를 기준으로 분리 개행문자만 있는 경우 비어있는 문자열로 처리
#잘려서 나온 리스트 값을 토큰이라고 부름
#결합문자열.join(문자열) ex ",".join(문자열)
#글자들을 결합문자열로 연결하여 하나의 문자열로 리턴

def slpit2():
    s = "짜장 짬뽕 탕수육"
    print(s.split())

    s2 = "서울->대전->대구->부산"
    cities = s2.split("->")
    print(cities)

    for city in cities:
        print(city)

    trabler = """
    강나루 건너서
    밀밭 길을
    
    구름에 달 가듯이
    가는 나그니
    """
    poet = trabler.splitlines()
    for line in poet:
        print(line)
    print(len(poet))

def jo():
    s = "._."
    print(s.join("대한민국"))
    print("._.".join("대한민국"))
#대체
#.replace (a,b) a의 값을 b로 바꿔버림
#.center
#.ljust
#.rjust

def dect():
    s = "독도는 일본땅. 대마도는 일본땅"
    print(s)
    print(s.replace("일본","한국"))
    print(s)#원문은 그대로라서 안바뀜

    message = "안녕하세요"
    print(message.center(30))#좌우로 15칸씩
    print(message.ljust(30))#왼쪽으로 30칸 밈
    print(message.rjust(30))#오른쪽으로 30칸



def main():
    trabler = """
        강나루 건너서
        밀밭 길을

        구름에 달 가듯이
        가는 나그니
        """#들여쓰기도 데이터기때문에 띄어져서 나옴
    poet = trabler.splitlines()# 각각 잘라서 리스트화시킴
    for line in poet:#여기서 7이 나온이유는 내가 들여쓰기해서마지막칸이 띄어씌기때문에 데이터가 잡힘 그래서 7로나옴
        print(line.center(30))# 각 리스트마다 중앙으로 밀어줌
main()
