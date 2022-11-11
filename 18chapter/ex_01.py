#고급 문법

#열거 가능 객체 이 규격의 객체들은 포문에 사용 가능함
#for 반복문의 순회 대상 객체
#해당 객체의 __iter__(메서드) 메서드로 열거 가능 가능 채 체 획득
#열거 가능 개체는 __iter__() 메서드를 정의해야 함
#매 루프마다 __next()__ 함수를 통해 다음 요소를 추출
#더 이상 요소가 없는데 __next()__ 를 호출하는 경우
#StopIteration 예외가 발생하고 for 반복문 을 끝냅
#(메서드들 구현 되어있음)
num = [1,2,3]
it = iter(num)
while True:
    try:
        num = next(it)
    except StopIteration:
        break
    print(num)

class Seq:
    def __init__(self, data):
        self.data =data
        self.index = -2

    def __iter__(self):
        self.index = -2
        return self

    def __next__(self):
        self.index += 2
        if self.index >= len(self.data):
            #self.index = -2 #하면 반복가능
            raise StopIteration
        return self.data[self.index:self.index+2]

solarterm = Seq("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")


for k in solarterm:
    print(k, end = ',')
print()
for i in solarterm:
    print(i, end = ',')
print()
def seqgen(data): #함수안에 yiled를 사용한 함수를 제네레이터라고함
    for index in range(0,len(data),2): #반복문을 끝날때까지 yield 줄을 계속 실행하며 리턴
        yield  data[index:index+2]

solarterm = seqgen("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")

for k in solarterm:
    print(k, end = ',')
print()
print(solarterm)

#일급 시민 자바는 이게 안됌 함수가 없기때문
#함수도 일반 변수와 동일한 특성을 가짐
#이름을 가진다
#다른 변수에 대입할 수 있다.
#인수로 전달할 수 있다.
#리턴값이 될 수 있다.
#컬렉션에 저장할 수 있다.
#--> 위와 같은 특성을 가지는 것을 일급시민이라고 함.

def add(a, b):
    print(a + b)

def calc(op, a, b):
    op(a,b)

def multi(a, b):
    print(a * b)



plus = add
plus(1,2)

calc(add, 1, 2)
calc(multi,1,2)

#지역 함수
#함수 안에 함수를 정의해서 사용
#함수가 정의 된 함수 내에서만 사용 가능
#--> 함수의 이름 충돌 방지
#함수를 리턴한 경우 함수 밖에서도 사용 가능

def calcsum(n):
    def add(a,b):
        return a + b

    total = 0
    for i in range(n+1):
        total = add(total, i)

    return total

print("~10 = ", calcsum(10))

def makeHello(message):
    def hello(name):
        print(message + ", " + name)
    return hello

enghello = makeHello("Good Morning") # message변수같은경우 closure 라고 함
kohello = makeHello("안녕하세요") #원래면 이 대입 실행후 message는 사라졌어야함 사실 지역변수도 hip에 저장됐었음 참조하는 주소값만 stack에 저장됌
#하지만 closure 가 되어 데이터값이 남아있음 변수로써 저장했기때문.

enghello("Mr Kim")
kohello("홍길동")

#함수 데코레이터
#데코레이터 미사용시
def inner():
    print("결과를출력합니다.")

def outer(func):
    print("-"*20)
    func()
    print("-"*20)

outer(inner)

def inner():
    print("결과출력")

def outer(func):
    def wrapper():
        print("-"*20)
        func()
        print("-"*20)
    return wrapper

inner = outer(inner)
inner()

def outer(func):
    def wrapper():
        print("-"*20)
        func()
        print("-"*20)
    return wrapper

@outer # == inner()을 실행할 시  inner = outer(inner)을 실행한거랑 똑같이 간주하겠다
def inner():
    print("결과를 출력합니다.")

inner()