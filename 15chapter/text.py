#연산자 메서드
#연산자를 재정의 할 수 있는 함수
#연산자 별로 함수명이 정해져 있음
# ○ == : __eq__
# ○ != : __ne__
# ○ < : __lt__
# ○ > : __gt__
# ○ <= : __le__
# ○ >= : __ge__
# ○ + : __add__, __radd__
# ○ - : __sub__, __rsub__
# ○ * : __mul__, __rmul__
# ○ / : __div__, __rdiv__
# ○ // : __floordiv__, __rfloordiv__
# ○ % : __mod__, __rmod__
# ○ ** : __pow__, __rpow__
# ○ << : __lshift__
# ○ >> : __rshift__

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

def main():
    kim = Human("김상형", 29)
    sang = Human("김상형",29)
    moon = Human("문종민",44)

    print(kim == sang)
    print(kim == moon)
    # == 을 기준으로 kim이 self에 대입되고 오른쪽은 other에 대입됌

main()