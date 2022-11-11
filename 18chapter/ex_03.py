#디버그 #shift + F9

#F8 Step Over = 한라인씩 넘어가며 디버깅 함수안은 들어가지 않음
#F7 Step Into = 한라인씩넘어가되 함수가 있으면 안에까지 들감 단 오픈되어있지 않을경우 못들어감

def seqgen(data): #함수안에 yiled를 사용한 함수를 제네레이터라고함
    for index in range(0,len(data),2): #반복문을 끝날때까지 yield 줄을 계속 실행하며 리턴
        yield  data[index:index+2]

solarterm = seqgen("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")

for k in solarterm:
    print(k, end = ',')
print()
print(solarterm)