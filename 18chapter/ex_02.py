#제네레이터
#객체로 순회가능한 객체를 만다는 거는 다소 귀찮은 작업
#제네레이터 함수로 대체 가능
#함수에서 데이터를 연속 리턴(yidef = return 대신사용)
#함수가 끝나면 (또는 return 실행할경우) StopIteration 예외 발생
#함수를 호출하면함수가 실행되는 것이 아니고 순회 가능 객체가 리턴
#순회 가능 객체로 순회할 때 실제 함수가 실행됨



#클래스 데코레이터
# __callable__ 매서드
#클래스를 함수 호출하듯이 사용했을 때 호출되는 메서드

class Outer:
    def __init__(self, func):
        self.func = func

    def __call__(self):#클래스를 함수처럼 사용함 크래서 실행 됌
        print("-"*20)
        self.func()
        print("-"*20)
@Outer
def inner():
    print("결과를 출력합니다")

if __name__ == "__main__":
    #inner = Outer(inner) 클래스 생성자를 이용한 방식
    inner() #객체의 인스턴스를 함수 호출하듯이 사용했을때 __call__이 호출이 됌

