class Addr:
    def __init__(self, name, phone, addr):
        self.name = name
        self.phone = phone
        self.addr = addr

    def __str__(self):
        return f"<Addr {self.name}/{self.phone}/{self.addr}"

    def __repr__(self):
        return f"<Addr {self.name}"
#이런 데이터만 관리하는 클래스를 데이터클래스 또는 모델 클래스라고함 (웹에서는 모델클래스라고 더 많이함)