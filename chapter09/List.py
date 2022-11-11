#리스트 자료의 집합
#리스트는 데이터 형의 제한이 없음 섞어서 넣기도 가능
#리스트의 요소 리스트[인덱스]
#리스트[begin:end:step]
#문자열은 쓰기가 안되지만 리스트는 불변개체가 아니기때문에 수정이 가능함 = 문자열을 리스트화시키면 가능하다 이말이지
import random
def testave():
    score = [88,95,70,100,99]
    total = 0

    for s in score:
        total += s
    print("총점:",total)
    print("평균:",total/len(score))
    print(list("Korea"))

    print(score[0])
    print(score[1])
    print(score[2])
    score[2] = 55#리스트는 불변개체가 아니라 수정가능
    print(score[2])
#list("korea") 문자열을 리스트로 바꿔주는 함수

def foring():
    nums = [0,1,2,3,4,5,6,7,8,9,]# == nums = list(range10))
    print(nums)
    print(nums[:])
    print(nums[2:5])
    print(nums[:4])
    print(nums[6:])
    print(nums[1:7:2])

    nums = list(range(10))## 처음부터 list함수는 주소값을 반환해서 list는 데이터를 주는게아니라 데이터를 가지고있고 주소값만 줌
    print(nums)
def white():
    nums = list(range(10))

    nums2 = nums  # 리스트에 대한 대입연산
    # 이거 c언어에서 그냥 주소값이 간다고 생각해 그럼 됌 배열이야 배열
    # 숫자와 bool을 제외한 모든 값은 이처럼 됌
    # 주소값 가져오는걸 참조값 reference value 라고한데
    # c와의 차이점 c는 주소값을 개발자가 관리할수있는데 여긴 못한데 원래 &연산자랑 *연산자로헀는데 여긴 걍 씀
    # 만약 참조가아니라 값만 복사하고싶으면 nums2 = nums[:] (처음부터끝까지) 이렇게하면 새로 만들어진 저장공간에 저장된 같은 값을가진 데이터를
    # 받을수있음
    print(nums)
    print(nums == nums2)
    nums2[0] = -1
    print(nums)
    print(nums2)

    nums = list(range(10))
    nums2 = list(range(10))
    print(nums == nums2)

def listdelins():
    # 기존값을 삭제하고 새로운 값으로 대체
    nums = list(range(10))
    nums[2:5] = [20, 30, 40]
    print(nums)
    nums[6:8] = [60, 70, 80, 90]  # 슬라이스 입력한 인덱스값은 삭제되고 새로운 두개의 값이 삽임이 됌
    # nums[6:5] 이런식으로할경우 처음부터 1칸도 안나오기대때문에 삭제는없고 시작칸에서 삽입만 일어난다.
    print(nums)
    nums[6:8] = [60]  # 입력한 인덱스에 비해 넣는 값이 적을경우 입력한 인덱스의 남는 칸이 삭제된다
    print(nums)

    # 기존값을 유지하고 삽입만 하기
    # nums[6:6] = [데이터] 위랑같음

def listadd():
    # 리스트도 시퀀스 문자열도 시퀀스기때문에 이러한 연산이 가능
    list1 = [1, 2, 3, 4, 5]
    list2 = [10, 11]
    listadd = list1 + list2
    print(listadd)
    listmulti = list2 * 3
    print(listmulti)
#[1, 2, 3, 4, 5, 10, 11]
#[10, 11, 10, 11, 10, 11]

def doublelist():#그냥 2차원 배열이라고 생각해
    # lol = [
    #     [1,2,3],
    #     [4,5],
    #     [6,7,8,9]
    # ]#괄호연산자에 의해 밑으로 내려도 괜찮음
    #
    # print(lol[0])
    # print(lol[2][1])
    #
    # for sub in lol:#순회방식 모든데이터를 다 방문해서 싹보는것
    #     for item in sub:
    #         print(item, end=' ')
    #     print()
    score=[
        [88,76,92,98],
        [65,70,58,82],
        [82,80,78,88]
    ]
    total = 0
    totalsub = 0
    for student in score:
        subject_total=getSubjectTotal(student)
        subjects = printAvg(student,subject_total)
        total += subject_total
        totalsub += subjects

    print(f"전체평균 {total/totalsub:.2f}")

def printAvg(student,subject_total):
    subjects = len(student)
    avg = subject_total / subjects
    print(f"총점 {subject_total} 평균 {avg:.2f}")
    return subjects

def getSubjectTotal(student):
    subject_total = 0
    for subject in student:
        subject_total += subject
    return subject_total

def findMin(*numbers):
    min = 999999
    for num in numbers:
        if num<min:
            min = num
    return min
def findMax(*numbers): #함수를 정의하는 인자에 *불으면 인자를 튜플로 묶어라 라는기능(묶는 이유는 변수를 여러게 받기위해서 처음부터 리스트로 받으려면 할 필요없음
    #max = -999999 # 범용성이 떨어짐 = 어떤경우에 실패할수있음
    max = numbers[0] # 이렇게 해야함 그럼 비교수가 가장 첫번째 자리수가 됌
    for num in numbers[1:]: # 0은 이미 들어갔으니까 0을 굳이 비교할 필요가없음 따라서 1부터 시작하면됌
        if num>max:
            max = num
    return max
    #findMax(list)  # = 이건 리스트를 튜플에 씌우게됌 ([1,2,3,4,5,6]) 이렇게 들어가기 때문에 2중으로 씌여서 위껄론 안됌

    #위를 하기 위한 함수

#리스트 삽입
#.append(값) : 리스트 끝에 값을 추가
#.insert(위치, 값):지정 위치에 값을 삽입

def apend():
    nums = [1,2,3,4]
    nums.append(5)
    print(nums)

def inser():
    nums = [1,2,3,4]
    nums.insert(2,99)
    print(nums)
def rand(start, end):
    return int(random.random()*(end-start+1))+start
def getRandomList(start, end, conunt):
    nums = []
    for _ in range(conunt):# _도 변수명으로 쓸수있고 반복문 돌릴 용도로만 쓰는변수는 이렇게 쓰는게 관례래
        r = rand(start,end)
        nums.append(r)

    return nums

#슬라이싱을 이용한 삽입
def inserttos():
    nums = [1,2,3,4]
    nums[2:2] = [90,91,92] #새로운 값 삽입

    nums = [1,2,3,4]
    nums[2] = [90,91,92] # 지정한 위치에 엘리먼트에 리스트로 삽입
    print(nums)#이게 되네 자료형이 안정해져있으니까 뭐든 들어갈수있음 리스트안에 리스트 들어가기가 가능

#리스트 끼리 병합하는법
def extendList():
    list1 = [1,2,3,4,5]
    list2 = [10,11]
    list3 = list1+list2 # 새로운 리스트를 리턴 +연산자를 이용할경우 리턴값을 받을 새로운변수가 필요함
    print(list3)# list1 = list1+list2도 결과는 같지만 컴퓨터 내부의 효율면에서 .extend()가 더 좋다고함
    list1.extend(list2) # 기존 리스트 확장 .extend()를 사용하면 원본을 변경하면서 붙일수있음
    print(list1)

#삭제
#.remove(값) : 리스트에서 값을 찾아 첫번째 해당 요소를 제거
#.del(리스트[인덱스]) : 지정한 인덱스의 요소를 제거
#[시작:끝] = [] : 지정한 범위의 요소를 제거
#.pop() : 리스트의 끝 요소를 삭제하고 삭제한 요소를 리턴
#.pop(인덱스) : 지정한 인덱스의 요소를 삭제하고 삭제한 요소를 리턴

def deleit():
    score = [1,2,3,4,5,6,7,8,9,10]
    score.remove(10) # 삭제하려는 값이 없으면 오류남
    print(score)

    del(score[1:2])
    print(score)

    score[1:4] = []
    print(score)

    print(score.pop())
    print(score.pop())
    print(score.pop(0)) # 앞부터 삭제하고 뒤에 append하면 Queue형식
    print(score)#score.pop()이거로하면 스택방식


def queue(): #선입선출 First In First Out FIFO
    score = [88,95,70,100,99]
    score.append(50)

    print('큐',score)
    print('큐',score.pop(0))
    print('큐',score)


def stack(): #후입선출 Last In First Out LIFO
    score = [1,2,3,4,5]
    score.append(50)

    print('스택',score)
    print('스택',score.pop())
    print('스택',score)

#검색
#.index(값) : 지정한 값을 찾아 해당 요소를 리턴, 없으면 에러 발생
#.find(값) : 지정한 값을 찾아 해당 요소를 리턴, 없으면 -1를 리턴
#.count(값) : 지정한 값이 리스트에 몇 번 나오는지 계산하여 리턴
#len(시퀀스) : 시퀀스의 길이
#max(시퀀스) : 시퀀스 요소 중 최대값 리턴
#min(시퀀스) : 시퀀스 요소 중 최소값 리턴
#값 in 시퀸스, 값 not in 시퀸스 : 값이 시퀸스에 포함되어 있는지 여부를 True/False로 리턴

def lnemaxmin():
    score = [88,95,70,100,99,88,78,50]
    print("학생수는 %d 입니다."%len(score))
    print("최고 점수는 %d점 입니다."%max(score))
    print("최소 점수는 %d점 입니다."%min(score))

def inans():#장점 대상의 수가 변경될때 관리가 쉽다
    ans = input("결제하실")
    if ans in ['yes', 'y', 'ok', '예']: # 이거아니였으면 or 문 개 난장판으로 써야함
        print("결제를 진행")
    else:
        print("걸제를 취소")


#정렬
#.sort([reverse=True][key=키에 적용할 함수])
# 리스트를 정령(디폴트는 오름차순), reverse=True로 오름차순 내림차순 선택
#.reverse() : 리스트의 순서를 역으로 바꿈
#sorted(시퀸스) : 지정한 시퀸스를 정렬하여 새로운 리스트로 리턴

def sortre():
    score=[88,95,70,100,99]

    score.sort()#내림차순 이걸 사용하면 원본까지 바뀌어버림
    print(score)

    score.reverse()#리버스
    print(score)

def sort2():
    score = [88, 95, 70, 100, 99]

    score2 = sorted(score)
    print(score2)
    print(score)

    score = [88, 95, 70, 100, 99]

    score2 = sorted(score, reverse=True)
    print(score2)
    print(score)

def key():
    #country = ["Korea", "japan", "CHINA", "america"]

    #country.sort()
    #print(country)#대소문자 값이 다르기떄문에 정렬이 대소문자 값에 따라 됌

    country = ["Korea", "japan", "CHINA", "america"]
    country.sort(key=str.upper)  # 키 오른쪽은 함수를 넣는것 각 값에 적용해야할 함수를 넣는것
    for con in country:
        print(con.upper(),end=" ")
    country.sort()
    print()

    country = ["Korea", "japan", "CHINA", "america"]

    for i in range(len(country)):
        country[i] = country[i].upper()
    country.sort()
    print(country)






    # 위 같은경우 각 4개의 자료에 str.lower을 적용한 다음 정렬을 적용함
   # print(country)


def main(): # # # # # 중요한건 슬라이싱 append pop sort 정도래 다기억해 걍~
    #doublelist()
    # min = findMin(2, 7, 5, -1, 20)
    # print('최솟값 :', min)
    # list = [1,2,3,4,5,6]
    # max=findMax(*list) # 이렇게 하면 리스트에서 나와짐 안에 있는데이터만 들어감 (1,2,3,4,5,6) 이렇게 근데 왜??
    #                     #호출할시에 *를 붙으면 묶은걸 푼다는 뜻
    # print('최대값 : ', max)
    # apend()
    # inser()
    # L = getRandomList(1,10,20)
    # print(L)
    # extendList()
    #deleit()
    #lnemaxmin()
    #inans()
    #sortre()
    #sort2()
    key()

main()
