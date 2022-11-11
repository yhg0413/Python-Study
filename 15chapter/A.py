#주소록 만들기
import pickle
class UserInfo:
    def __init__(self, name,email,phone):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"<UserInfo {self.name}/{self.email}/{self.phone}>"

    def __repr__(self):#컬렉션에 담겨있는 내용을 출력할떈 이 함수가 출력 됌 str은 리스트 안에 담긴 정보로는 안됌됌
       return self.__str__()

class AddressBook():# crud 생성 읽고 지우고 등 기본 요소
    def __init__(self):
        self.book = []
        pass
    def add(self,name,email,phone):
        ui = UserInfo(name,email,phone)
        self.book.append(ui)

    def find_by_name(self, name): #보통 전체가 일치하는거 찾을때 find라 함
        for ui in self.book:
            if ui.name == name:
                #return ui #동명이인은 없다라는 가정
                return ui

    def search_by_name(self,name): #부분적으로 일치하는거 찾을때 search라고 자주함
        new_book = []
        for ui in self.book:
            if ui.name.find(name) > -1:
                new_book.append(ui)
        return new_book
    #def search_by_name(self, name):
    #   return [ui for ui in self.book if ui.name.find(name) > -1]


    def updata(self, name, email,phone):
        ui = self.find_by_name(name)
        if not ui:
            print(f"{name}은 목록에 없습니다")
            return
        ui.email = email
        ui.phone = phone

    def remove(self, name):
        ui = self.find_by_name(name)
        if not ui:
            print(f"{name}은 목록에 없습니다")
            return
        self.book.remove(ui) #ui는 book의 리스트 내용임 따라서 remove로 지울수있음

    def save(self, fpath):
        try:
            with open(fpath, 'wb') as file:
                pickle.dump(self.book, file)
        except Exception as e:
            print(e)

    def load(self, fpath):
        try:
            with open(fpath, 'rb') as file:
                self.book = pickle.load(file)
        except Exception as e:
            print(e)

    def sort(self):
        self.book.sort(key = lambda u: u.name,reverse = False)
        #u에는 self.book이 들어감 매개변수 u에넣고 u.name을 리턴 이름순으로 정열
#                                          =self.book.name
    def __str__(self):

        pass

def main():
    addr_book =AddressBook()
    file_name = "Text2.dat"
    for ix in range(1, 100):
        if ix%2 == 0:
            addr_book.add(f"홍길동{ix}", f"hong{ix}@naver", '010-1111-1111')
        else:
            addr_book.add(f"고길동{ix}", f"go{ix}@naver", '010-2222-2222')
    addr_book.save(file_name)
    addr_book.load(file_name)
    addr_book.sort()
    print(addr_book.book)


main()