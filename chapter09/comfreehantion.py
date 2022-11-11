#컴피르핸션
#[수식 for 변수 in 리스트 if 조건]
#내부의 리스트를 순회하며 각 요소에 대한 수식을 적용하여 최종 요소를 생성
#if 조건을 추가하면 조건을 만족하는 요소만 추가
import random

#컴프리핸션의 대상이 되는 패턴
def getRandomList(start, end, conunt): # nums = [rand(1,100) for _ in range(6)] 랑 똑같은 역할임
    nums = []
    for _ in range(conunt):# _도 변수명으로 쓸수있고 반복문 돌릴 용도로만 쓰는변수는 이렇게 쓰는게 관례래
        r = rand(start,end)
        nums.append(r)

    return nums

def rand(start, end):
    return int(random.random()*(end-start+1))+start

def main():
    # country = ["Korea", "japan", "CHINA", "america"]
    # newlist = [c.upper() for c in country]
    #
    # print(newlist)
    nums = [n*2 for n in range(1,11)]
    for i in nums:
        print(i, end= ',')

    nums = []
    for n in range(1,11):
        nums.append(n*2)
    print(nums)

    print([n for n in range(1, 11) if n % 3 ==0])

    l = [rand(1,100) for _ in range(6)]
    print(l)

main()