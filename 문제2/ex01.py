import MySQLdb
#시작하면 pip install mysqlclient 하기
db = MySQLdb.connect(host = 'localhost', db = 'employees',
                    user='root', passwd= '9647', charset='utf8')

cursor = db.cursor()


print("접속에 성공")

sql ="""
SELECT E.first_name,E.last_name, D.dept_name,DE.from_date,DE.to_date
FROM employees E
	inner JOIN dept_emp DE
	ON E.emp_no = DE.emp_no
	INNER JOIN departments D 
	ON DE.dept_no = D.dept_no
WHERE DE.to_date = '9999-01-01'
ORDER BY E.first_name, E.last_name
"""
cursor.execute(sql)

rows = cursor.fetchall()##커서에 있는 모든 데이터를 가져오는 함수?
for row in rows:
    print(row)


cursor.close()
db.close()
