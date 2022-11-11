#액세스
#파이썬은 기본적으로 정보 은폐기능을 지원하지 않음
#getter/setter 로 정보(프로퍼티)를 보호
# @property - 함수명이 프로퍼티 명이 되어 getter 함수로 작동
# @프로퍼티명.setter 프로퍼티의 setter()함수 정의

class Date:
    def __init__(self, month):
        self.inner_month = month
    # 장식자 라고부름
    @property #getter
    def month(self):
        return self.inner_month

    @month.setter
    def month(self, month):
        if 1<= month <=12:
            self.inner_month = month
class Date2:
    def __init__(self, month):
        self.__month = month
    def getmonth(self):
        return self.__month

    def setmonth(self, month):
        if 1<=month<=12:
            self.__month=month

    month = property(getmonth,setmonth)

today = Date2(8)
today.month = 15

print(today.month)
#print(today.__month) 데이터 클래스 밖에서 직접읽거나 쓰거나를 못함 __한 변수는