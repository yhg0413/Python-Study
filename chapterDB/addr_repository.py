from addr_models import Addr

class AddressRepositry:

    def __init__(self, db):
        self.cursor = db.cursor()

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
    def close(self):
        self.cursor.close()

    def get_total(self, where=''): # 카운트값 리턴
        sql = "select count(*) from tbladdr " + where
        self.cursor.execute(sql)
        row = self.cursor.fetchone()  # count를 써서 무조건 하나만 나와서 if도 안해도 됌
        return row[0]

    def get_list(self, where=''): #목록의 튜플을 리턴
        sql = "select * from tblAddr " + where
        self.cursor.execute(sql)
        rows=  self.cursor.fetchall()
        return (Addr(*row) for row in rows)

    def get_one(self, name):
        sql = "select * from tbladdr where name = %s"
        self.cursor.execute(sql, (name,))
        row = self.cursor.fetchone()
        if row:
            return Addr(*row) #row 튜플로 되어있어서 튜플을 펼치라는 것
        # 사전앞에 ** 를 붙이면 키워드 전달방식으로 한다?

    def insert(self, data):
        sql = "insert into tbladdr values(%s, %s, %s)"
        self.cursor.execute(sql, (data.name, data.phone, data.addr))

    def update(self, data):
        sql = """
            update tbladdr set
            phone = %s,
            addr = %s 
            where name = %s
        """
        self.cursor.execute(sql,(data.phone,data.addr,data.name))

    def remove(self, name):
        sql = "delete from tbladdr where name = %s"
        self.cursor.execute(sql, (name,))

    def exit(self,answer):
        self.cursor.close()
        self.db.close()
        print("종료합니다.")


