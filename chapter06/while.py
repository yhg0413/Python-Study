#whili문 : 조건이 참인 동안 명령 블럭을 실행
#whlie 조건:
#   명령 블록


student = 1
while student <= 5:
    print(student, "번 학생의 성적을 처리합니다")
    student +=1


    #파이썬에서만 구현가능한 계단만들기
for y in range(1, 10):
    print("*"*y)

###############################
for a in range(0, 10):
    for b in range(0, 10-a):
        print(' ',end="")
    for b in range(0, a):
        print('*',end="")
    print()

################################

for a in range(0, 10):
    for b in range(0, 5):
        print(" ", end="")
    for b in range(0, 10-a):
        print(' ',end="")
    for b in range(0, a*2-1):
        print('*',end="")
    print()

## 1부터 100까지의 합
num = 1
total = 0
while num <= 100:
    total += num
    num += 1
print("totla = ", total)

## 1부터 100까지 홀수와 짝수의 합
num = 1
total1 = 0
total2 = 0
while num <= 100:
    if (num % 2) == 0:
        total1 += num
    else:
        total2 +=num
    num += 1
print("짝수합 = ", total1, "홀수합 = ", total2)


#####################################################
#for문
#컬렉션의 요소를 하나씩 꺼내 명령 블록을 실행
#컬렉션의 모든 요소를 다 사용하면 반복을 끝냄
#for 제어변소 in 컬렉션:명령

for student in [1,2,3,4,5]:#리스트 컬렉션 []를 사용했기 때문
    print(student, "번 학생의 성적을 처리한다")
###############################

total = 0
for num in range(1, 101):
    total += num
print("total = ", total)
###############################
totla = 0
for num in range(2, 101, 2):#끝에 자리에 쓰면 그 숫자로 +연산함
    total += num
print("total = ", total)
#######################
for a in range(5):#range(5) 하나만쓰면 끝자리 숫자 증가값은 1로 됌 시작값은 0
    print("이 문장 반복")
#######################
for x in range(1,51):
    if(x%10) == 0:
        print(('+'), end = '')
    else:
        print('-', end = '')


## 무한루프
result = False
print("3+4=?")
n=0
while 1:
    a = int(input('정답입력'))
    if a == 7: break
print('굳')
for n in range(3):
    a = int(input('정답입력잼'))
    if a == 7:
        result = True
        break
if result == True : print('굳')
else : print('땡')

for a in range(0, 10):
    for b in range(0, 10-a):
        print('*',end="")
    print()

for y in range(10,0,-1):
    print('*'*y)