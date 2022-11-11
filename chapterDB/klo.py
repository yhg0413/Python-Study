import MySQLdb

db = MySQLdb.connect(host='localhost', db='employees',
                     user='root', passwd='9647')

cursor = db.cursor()

print("접속에 성공")

sql = """

"""
cursor.execute(sql)

#필요한 작업 실행

cursor.close()
db.close()
