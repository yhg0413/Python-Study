class User:
    def __init__(self,id,name, phone, addr, age):
        self.id = id
        self.name = name
        self.phone = phone
        self.addr = addr
        self.age = age

    def __str__(self):
        return f"<Addr {self.id}/{self.name}/{self.phone}/{self.addr}/{self.age}"

    def __repr__(self):
        return f"<Addr {self.name}"
#이런 데이터만 관리하는 클래스를 데이터클래스 또는 모델 클래스라고함 (웹에서는 모델클래스라고 더 많이함)