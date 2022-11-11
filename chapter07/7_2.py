#가변 인수
#인수의 수가 고정되지 않음
#호출시 원하는 만큼 인수를 지정
#함수에서는 이를 튜플 변수로 받음()
#일반 인수 뒤에만 올 수 있음
#하나만 사용 가능

def intsum(*ints):
    sum = 0
    for num in ints:
        sum += num
    return sum


print(intsum(1,2,3))
print(intsum(5,7,8,11,13))
print(intsum(8,9,6,2,9,7,5,8))

#인수의 기본값
#함수 호출시 인수가 지정되지 않았을 때 사용할 값
#함수 정의시 인수에 값을 대입
#인수 목록의 마지막 부분에 배정
#중간에 배정시 구분 불가

def calcstep(begin, end, step = 1):## 전달 될시 전달 됀 값 아니면 step에 1이들감
    total = 0#기본값넣는건 무조건 끝부터 넣는거만 됌 중간에만 비우고 하는건 안댐 ex begin =1, end, step =1 xxxxxxxx
    for num in range(begin, end+1, step):
        total += num

    return total

print("1~10=", calcstep(1,10,2))
print("1~100=", calcstep(1,100))

#키워드 인수

print("3~5=",calcstep(3,5,1))
print("3~5=",calcstep(begin=3,end=5,step=1))
print("3~5=",calcstep(step=1,end=5,begin=3))
print("3~5=",calcstep(3,5,step=1))
print("3~5=",calcstep(3,step=1,end=5))