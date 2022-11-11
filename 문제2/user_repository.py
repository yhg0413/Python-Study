from user_models import User

class UserRepositry:

    def __init__(self, db):
        self.cursor = db.cursor()

        self.cursor.execute("drop table if exists user")
        self.cursor.execute(
            """
            create table user(
                id INT PRIMARY KEY AUTO_INCREMENT,
                name varchar(16),
                phone char(16),
                addr text,
                age int
            )
            """
        )
        self.cursor.execute("select * from User order by addr")

    def close(self):
        self.cursor.close()

    def get_total(self, where=''): # 카운트값 리턴
        sql = "select count(*) from User " + where
        self.cursor.execute(sql)
        row = self.cursor.fetchone()  # count를 써서 무조건 하나만 나와서 if도 안해도 됌
        return row[0]

    def get_list(self, where=''): #목록의 튜플을 리턴
        sql = "select * from user " + where
        self.cursor.execute(sql)
        rows=  self.cursor.fetchall()
        return (User(*row) for row in rows)

    def get_one(self, name):
        sql = "select * from user where name = %s"
        self.cursor.execute(sql, (name,))
        row = self.cursor.fetchone()
        if row:
            return User(*row) #row 튜플로 되어있어서 튜플을 펼치라는 것
        # 사전앞에 ** 를 붙이면 키워드 전달방식으로 한다?

    def insert(self, data):
        sql = "insert into user(name,phone,addr,age) values(%s,%s,%s,%s)"
        self.cursor.execute(sql, (data.name, data.phone, data.addr,data.age))

    def update(self, data):
        sql = """
            update user set
            phone = %s,
            addr = %s,
            age = %s
            where name = %s
        """
        self.cursor.execute(sql,(data.phone,data.addr,data.age,data.name))

    def remove(self, name):
        sql = "delete from user where name = %s"
        self.cursor.execute(sql, (name,))

    def exit(self):
        self.cursor.close()
        print("종료합니다.")


