#클래스 : 관련 정보와 정보의 조작함수(메서드를) 묶어서 관리
#class 키워드로 정의
# 사용하기 위해서는 인스턴스를 생성한 후 사용
#파스칼 표기법 사용(대문자로 시작)

#생성자
#__init__(self)
#클래스의 인스턴스를 생성할 때 자동을 ㅗ호출
#맴버 변수 정의 및 초기화 역할
#객체 = 객체명(인수) == 클래스명() : 해당클래스의 인스턴스 생성 및 변수를 인스턴스 내에 삽입
class Account:
    def __init__(self,balance):# 생성자 함수 #__가 앞뒤로 있는건 파이썬이 이용하는 특수한 함수다 라고 보면됌
        self.balance = balance #init은 초기화를 상징함

    def deposit(self, money):#메서드의 처음에는 관행상 self가 와야함
        self.balance+=money

    def inquire(self):
        print(f"잔액은 {self.balance}원 입니다.") #self가 없으면 클래스내 생성된 인스턴스 변수보고 그다음 지역변수 그다음 전역 보고 없으면 땡

def call_account(balance, money):
    account = Account(balance) #Account의 인스턴스 생성 대문자로 시작했기때문에 클래스라는걸 알수있음 (클래스명으로 함수호출한 사례)
    #init가 호출되고 값이 init로 전달됌
    account.deposit(money)
    account.inquire()
#################################################################################################
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def intro(self):
        print(f"{self.age}살 {self.name}입니다")
    def __str__(self):
        return f"<나이 : ({self.age}), 이름 : ({self.name})>"

def input_name_age():
    name = input("이름 : ")
    age = int(input("나이 : "))
    return name, age


def test():
    name, age = input_name_age()
    kim = Human(name, age)
    kim.intro()

    lee = Human("이승우", 45)
    lee.intro()

    info = kim.__str__()
    print(info)
    print(kim.name)
    kim.age = 20
    kim.intro()

#######################################################################################################
class Stack:
    def __init__(self,size=10):#얘는 인스턴스화 될때만 나옴
        self.data = []
        self.size = size

    def push(self,data):
        if len(self.data) < self.size:
            self.data.append(data)
        pass
    def pop(self):
        if len(self.data) != 0:
           self.data.pop()
        pass
    def clear(self):
        self.data = []
    def print_s(self):
        print(self.data)
    def __str__(self): #__str__은 프린터 함수에 들어갈때만 호출되서 나온다
        return f"<Stack size({self.size}, data: {self.data}>"
                # 관례 양식이니까 기억하기 < 내용 >

class Stack2:# r교수님 버젼
    def __init__(self,size=10):
        self.data = []
        self.size = size

    def push(self,data):
        if len(self.data) == self.size: #FULL
            return
        self.data.append(data)
    def pop(self):
        if len(self.data) == 0: #EMPTY
            return
        return self.data.pop()
    def clear(self):
        self.data = []
    def print_s(self):
        print(self.data)
    def __str__(self):
        return f"<Stack size({self.size}, data: {self.data}>"
#########################################################################
## 상속

def main():

    S = Stack2(10)
    for i in range(1,12):
        S.push(i)
    for i in range(1,7):
        S.pop()
    print(S)
    S.print_s()
    S.clear()

    test()


main()