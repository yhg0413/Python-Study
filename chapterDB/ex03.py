from myapp import Application, MenuItem
import MySQLdb
import sys

class DBApp(Application):
    def __init__(self):
        super().__init__()
        self.db = MySQLdb.connect(host='localhost', db='employees',
                             user='root', passwd='9647', charset="utf8")
        self.cursor = self.db.cursor()
        self.cursor.execute("drop table if exists tbladdr")
        self.cursor.execute(
            """
            create table tbladdr(
                name char(16) primary key,
                phone char(16),
                addr text
            )
            """
        )
        self.cursor.execute("insert into tbladdr values('김상형','123-4567', '오산')")
        self.cursor.execute("insert into tbladdr values('한경은','555-1004', '수원')")
        self.cursor.execute("insert into tbladdr values('한주완','444-1092', '대전')")

        self.cursor.execute("select * from tbladdr order by addr")
    def create_menu(self, menu):
        menu.add_menu(MenuItem("목록", self.print_list))
        menu.add_menu(MenuItem("추가", self.add))
        menu.add_menu(MenuItem("수정", self.update))
        menu.add_menu(MenuItem("삭제", self.remove))
        menu.add_menu(MenuItem("종료", self.exit))
    def print_list(self):
        self.cursor.execute("select * from tbladdr")
        self.cursor.execute("select * from tbladdr order by addr")
        i = 0
        print("="*20)
        print("")
        while True:
            record = self.cursor.fetchone()
            if record == None: break
            i = i + 1
            print(f"{i} : {record[0]}, 전화: {record[1]}, 주소: {record[2]}")
        print(f"총 {i}건")

    def add(self):
        print("추가")

    def search(self):
        try:
            print("데이터 검색 ==============")
            name = input("이름 : ")

            sql = f"select count(*) from tbladdr where name like'%{name}%'"
            self.cursor.execute(sql)
            row = self.cursor.fetchone()
            total = row[0]
            if total == 0:
                print("검색어가 없습니다.")
                return

            sql = f"select * from tbladdr where name like '%{name}%'"
            self.cursor.execute(sql)
            row = self.cursor.fetchall()

            print("=" * 50)
            header = ("이름", "전화번호", "주소")
            print(f"No {header[0]:10}{header[1]:10}{header[2]:10}")
            print("-" * 50)

            for rows in row:
                print(f"이름 : {rows[0]} 전화번호 : {rows[1]} 주소 : {rows[2]}")

        except Exception as e:
            print(e)

    def update(self):
        try:
            print("데이터 추가 ===============")
            name = input("이름 : ")
            phone = input("전화번호 : ")
            addr = input("주소 : ")
            print("=" * 20)
            sql = "insert into tbladdr values(%s, %s, %s)"
            self.cursor.execute(sql, (name, phone, addr))
            self.db.commit()
            print("추가 완료")
        except Exception as e:
            print(e)

    def remove(self):
        print("삭제")

    def exit(self):
        answer = input("종료하시겠습니까? ([y]/n)")
        print(answer)
        if answer in ["y", "Y", ""]:
            self.cursor.close()
            self.db.close()
            print("종료합니다.")
            sys.exit(0)

        print("계속해서 실행합니다")

if __name__ == '__main__':
    app = DBApp()
    app.run()