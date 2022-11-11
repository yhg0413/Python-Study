from myapp import Application, MenuItem
import MySQLdb
import sys
from addr_repository import AddressRepositry
from addr_ui import *
##commit을 안하면 db에 작업이 안됌
#보통 클래스명이랑 테이블명이랑 같게만든다함
class DBApp(Application):
    def __init__(self):
        super().__init__()
        self.db = MySQLdb.connect(host='localhost', db='employees',
                             user='root', passwd='9647', charset="utf8")

        self.repo = AddressRepositry(self.db)


    def create_menu(self, menu):
        menu.add_menu(MenuItem("목록", self.print_list))
        menu.add_menu(MenuItem("검색", self.search))
        menu.add_menu(MenuItem("추가", self.add))
        menu.add_menu(MenuItem("수정", self.update))
        menu.add_menu(MenuItem("삭제", self.remove))
        menu.add_menu(MenuItem("종료", self.exit))

    def print_list(self):
        try:
            total = self.repo.get_total()
            rows = self.repo.get_list()
            #값이 없을경우 빈 튜플값이 리턴됌
            print_list(total,rows)
        except Exception as e:
            print(e)
    def add(self):
            print("데이터추가 =========================")
            data =input_addr_info()
            self.repo.insert(data)
            print("=" * 20)
            self.db.commit()
            print("추가완료")


    def update(self):
            print("데이터 수정 ===============")
            name = input("이름 : ")
            data = self.repo.get_one(name)

            if not data:
                print(f"{name} 데이터가 없습니다.")
                return
            data = input_update_info(data)
            self.repo.update(data)
            self.db.commit()
            print("추가 완료")


    def remove(self):
            print("데이터 삭제 ==============")
            name = input("이름 : ")
            self.repo.remove(name)
            self.db.commit()
            print("삭제 완료")

    def search(self):
            print("데이터 검색 ==============")
            name = input("이름 : ")
            where = f"where name like '%{name}%'"
            total = self.repo.get_total(where)
            row = self.repo.get_list(where)
            print_list(total,row)


    def exit(self):
        answer = input("종료하시겠습니까? ([y]/n)")
        if answer in ["y", "Y", ""]:
            self.repo.exit()
            self.db.close()
            sys.exit(0)
        print("계속해서 실행합니다")


if __name__ == '__main__':
    app = DBApp()
    app.run()