#random 모듈
#.randint(begin, end)end포함 사이의 정수 난수 리턴
#.randrange(begin, end)end 미호팜 비긴부터 엔드까지 정수 난수 리턴
#.uniform(begin,end):begin~end 사이의 실수를 리턴(end) 미포함
#.cohice(시퀀스) : 시퀀스에서 랜덤하게 요소 선택하여 리턴
#.shuffle(시퀀스) : 시퀀스의 내용을 랜덤하게 썩음
#.sample(시퀀스,count) : 시퀀스에서 랜덤하게 count개의 요소 리턴
import random
def main():
    for i in range(5):
        print(random.randrange(1,10))

    for i in range(5):
        print(random.uniform(1,10))
    for i in range(5):
        print(random.randint(1,10))
    food = ["짜장면", "짬뽕", "탕수육", "군만두"]
    print(random.choice(food))

    i = random.randrange(len(food))
    print(food[i])

    print(food)
    random.shuffle(food)
    print(food)

    food = ["짜장면", "짬뽕", "탕수육", "군만두"]
    print(random.sample(food,2))

    nums = random.sample(range(1,46),6)
    nums.sort()
    print(nums)



main()