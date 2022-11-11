#클래스 메소드

class Car:
    count = 0 #클래스 멤버 변수 라고말함
    #인스턴스와 무관함
    def __init__(self, name):
        self.name = name
        Car.count += 1
    #데코레이터 ->@ 장식자
    @classmethod #보통 사용하는건 COUNT같은 사용용도 할때 사용함
    def outcount(cls):
        print(cls.count)
            #class의 약자
# pride = Car("프라이드")
# korando = Car("코란도")
# Car.outcount()

#정적 메서드
class Car2:
    @staticmethod #이게 붙으면 self도 못쓰고 클래쓰도 못씀 그냥 함수가 되지만 사용은 가능
    def hello():
        print("오늘도 안전 운행 합시다.")
    count = 0

    def __init__(self, name):
        self.name = name
        Car2.count += 1

    @classmethod
    def outcount(cls):
        print(cls.count)

Car2.hello()