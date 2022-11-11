#시간조사, time모듈

import time
#1970년 1월 1일 자정을 기준으로 경과한 시간을 초단위로 표현
#-->에폭(Epoch) 시간 또는 유닉스 시간이라고 부른다

print(time.time())

t = time.time()
print(time.ctime(t))#c 는 캐릭터의 약자 charicter 쓸일이 읎단다
print(time.localtime(t))#이건 전세계 공통이래 현재위치를 기반으로 시간을 해석하는 함수
now = time.localtime()
print(f"{now.tm_year}년 {now.tm_mon}월 {now.tm_mday}일")
print(f"{now.tm_hour}:{now.tm_min}:{now.tm_sec}")

import datetime
#form datetime import datetime
#now=datetime.now() 이 표현을 좀 더 자주 쓴다고 함
now = datetime.datetime.now()
print(f"{now.year}년 {now.month}월 {now.day}일")
print(f"{now.hour}:{now.minute}:{now.second}")

#실행 시간 측정
start = time.time()
i=0
for a in range(1000):
    i+=a
end = time.time()
print(end - start)
start = time.time()
i=0
for a in range(1000):
    i+=a
    print(i)

end = time.time()
print(end - start)#출력 1000번 하는데 걸린 시간

#실행 멈춤
#time.sleep(인자)

print("안녕하세요")
time.sleep(1)
print("밤에 성시경이 두 명 있으면 뭘까요?")
#time.sleep(5)
print("야간투시경입니다.")

import calendar as cal

print(cal.calendar(2018))
print(cal.month(2019, 1))#캘린더 그리기

dates = ["월", "화", "수", "목", "금", "토", "일"]

day=cal.weekday(2020,8,15)
print(f"광복절은 {dates[day]}요일입니다.")

#tmie.strftime(string,format)#현재 시간을 문자열로 바꾸는 것
#struct_time 객체를 지정한 format에 맞게 변환
#time.strptime(format[,t]) 보조자료 12 볼것#문자열을 객체로 바꾸는거

print(time.strftime('%Y-%m-%d %I:%M'))

timestring = '2019-02-20 12:12:12'
print(time.strptime(timestring, '%Y-%m-%d %I:%M:%S'))
#카메라로 사진찍었을때 파일명만들떄 이 기법 쓴다고 함
now=datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S.%f"))

for i in range(1,11):
    now = datetime.datetime.now()
    print(now.strftime("%Y%m%d%H%M%S-")+str(i),end=".jpg")
    print()
for i in range(1,11):#f""이건 문자열이면 다 가능함
    fname=now.strftime(f"%Y%m%d%H%M%S-{i:03d}.jpg")
    print(fname)