import sys
from myapp import Application, MenuItem


class NotepadApp(Application):
    def __init__(self):
        super().__init__() #부모클래스 생성자 호출


    def create_menu(self, menu):
        menu.add_menu(MenuItem("열기", self.open))
        menu.add_menu(MenuItem("저장", self.save))
        menu.add_menu(MenuItem("목록 보기", self.print_list))
        menu.add_menu(MenuItem("종료", self.exit))  # 아 메뉴 아이템에 넣어서 메뉴아이템 1을 실행하면 open이 실행됌 이런식으로 아
    def open(self):
        print("열기를 실행합니다.")

        pass
    def save(self):
        print("저장를 실행합니다.")
        pass
    def print_list(self):
        print("목록 보기를 실행합니다.")
        pass
    def exit(self):
        print("종료를 실행합니다.")
        sys.exit(0) # 0 = 정상적인 종료
        pass


class AddressBookApp(Application):

    pass

#클래스화 하는 이유는 범용성있게 만들어서 여기저기서 쓸려고 하는거임.
#클래스에서 아무것도 상속받지않을때 최상이 부모인 오브젝트에서 상속을 받음
def main(): # 이코드 떄문에 메인함수가 실행됌 그래서 아래처럼 하애함
    # menu = Menu()
    # #itemp = MenuItem("열기", lambda : print"열기 실행")
    # #menu.add(item)
    # menu.add_menu(MenuItem("열기",lambda :print("열기실행")))
    # menu.add_menu(MenuItem("저장",lambda : print("저장 실행")))
    # menu.add_menu(MenuItem("목록보기",lambda : print("목록보기 실행")))
    # menu.add_menu(MenuItem("종료", lambda : print("종료 실행")))
    # menu.print_()
    #
    # menu.run(1)
    # menu.run(2)
    # menu.run(4)
    app = NotepadApp()
    app.run()
    pass
if __name__ == "__main__":
    main()
    pass