import MySQLdb
db = MySQLdb.connect(host = 'localhost', db = 'employees',
                    user='root', passwd= '9647', charset="utf8")

cursor = db.cursor()


print("접속에 성공")

cursor.execute("drop table if exists tbladdr")
cursor.execute(
"""
create table tbladdr(
    name char(16) primary key,
    phone char(16),
    addr text
)
""")#text = db의 제약을 받지않는 자료형


cursor.execute("insert into tbladdr values('김상형','123-4567', '오산')")
cursor.execute("insert into tbladdr values('한경은','555-1004', '수원')")
cursor.execute("insert into tbladdr values('한주완','444-1092', '대전')")

cursor.execute("select * from tbladdr order by addr")

# table = cursor.fetchall()
# for record in table:
#     print(table)
#     print(record)
#     print(f"이름: {record[0]}, 전화: {record[1]}, 주소: {record[2]}")


#  크리에이트 했던 순서로 들어감 위에 *를 사용했기 때문
# 위랑 같은 결과
# cursor.execute("select * from tbladdr order by addr")
# while True:
#     record = cursor.fetchone()
#     if record == None: break
#     print(f"이름: {record[0]}, 전화: {record[1]}, 주소: {record[2]}")


#where절이 없는경우 보통 fatchall 사용 사용할경운 그때끄때 달라짐


# primary key를 사용했을떄
name = input("검색할 사용자를 입력하세요 ")
#cursor.execute(f"select addr from tbladdr where name = '{str}'")
sql = "select addr from tbladdr where name = %s"
cursor.execute(sql,(name,))
record = cursor.fetchone() # primary key를 where문에 써서 fetchone이면 충분함

#레코드에 값이 들어있는지 확인
if record : print(f"{name}은 {record[0]}에 살고있습니다")
else : print(f"{name}은 없는 이름입니다.")

#primary key를 사용하지 않았을 경우 김상형 이라는 데이터가 여러개 나올수있기때문에
#fatchall()를 사용하는것이다 근데 fatchall()을 사용해서 데이터값이 없을 경우
#비어있는 튜플이 리턴됌 하지만 결국 false랑 같은 결과 fatchall()은 루프를 돌라고
#튜플로 리턴된다고함 만약 튜플이 아니면 반복문에서 오류가 나기 때문
try:
    print("데이터 추가 ===============")
    name = input("이름 : ")
    phone = input("전화번호 : ")
    addr = input("주소 : ")
    print("="*20)
    sql = "insert into tbladdr values(%s, %s, %s)"
    cursor.execute(sql, (name, phone, addr))
    db.commit()
    print("추가 완료")
except Exception as e:
    print(e)

addr = input("변경 주소 : ")
name = input("변경자 명 : ")
sql = "UPDATE tbladdr SET addr = %s WHERE name = %s"
cursor.execute(sql, (addr, name))
db.commit()
print("업데이트 완료")
cursor.execute("select * from tbladdr order by addr")

while True:
    record = cursor.fetchone()
    if record == None: break
    print(f"이름: {record[0]}, 전화: {record[1]}, 주소: {record[2]}")

cursor.execute("DELETE FROM tblAddr WHERE name = '김상형'")
db.commit()
print("삭제완료")



#필요한 작업 실행

cursor.close()
db.close()
