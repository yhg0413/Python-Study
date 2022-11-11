#myapp.py
import sys


class MenuItem:
    def __init__(self, title, action=None):
        self.title = title
        self.action = action

    def __str__(self):
        return f"<MenuItem {self.title}>"

    def __repr__(self):
        return f"<MenuItem {self.title}>"

    def run(self):
        self.action()

class Menu:
    def __init__(self):
        self.menus = []

    def add_menu(self, menu_item):
        self.menus.append(menu_item)

    def print_(self):
        print("[메뉴]", end = "")
        for i, menu in enumerate(self.menus):
            print(f"{i}:{menu.title}  ", end="")
        print()

    def run(self, select):
        if select >= len(self.menus):
            print("잘못된 메뉴 선택입니다.")
            return

        self.menus[select].run()
        pass
class Application:
    def __init__(self):
        self.menu = Menu() # Menu 안엔 아까 넣은 "열기" "저장" "목록보기" "종료 등이 들어감 이 구성으 실행할 메소드를 만들어야함
        self.create_menu(self.menu)


    def create_menu(selfself,menu):
        pass
    def run(self): # 사용자랑 상호작용하며 이뤄지기 때문에 사용자가 종료할때까지 실행돼야해서 무한루프
        while True:
            self.menu.print_()
            sel = int(input("[선택]"))
            self.menu.run(sel)



if __name__ == "__main__":


    pass