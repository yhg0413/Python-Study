#상속 : 기존 클래스 정의를 그대로 자신의 것으로 취하는 방법

#class 자식클래스명(부모클래스명):
# 자식 클래스 정의 bass super 다 부모클래스를 나타냄
# 자식은 child sub 객체지향프로그래밍은 그림으로 설명한다고함
#UML


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(str(self.age) + "살" + self.name + "입니다.")

class Student(Human):#자식(부모)
    def __init__(self, name, age, stunum):
        super().__init__(name, age) # Human의 __init__을 실행한다는 것 상속에 한에서 직접호출하게 됌
        self.stunum = stunum
#오버라이드시 주의점 이름과 매개변수의 개수가 같이야함
    def intro(self): # 재정의하지않으면 부모꺼 그대로 쓰는데 재정의해서 다릏게 사용됌 : 메서드 오버라이드 라고함 (method override)
            super().intro()
            print("학번: " + str(self.stunum))

    def study(self):
        print("하늘천 따지 검을 현 누를 황")

#상속하는 이유는 여러개의 클래스에서 겹치는 부분을 따로 때서 한번에 수정하고 편하게 사용하기 위해서 사용함
def main():
    kim = Human("김상형", 29)
    kim.intro()

    lee = Student("이승우", 45, 930011)
    lee.intro()
    lee.study()

main()