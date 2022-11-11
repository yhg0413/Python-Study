#filter(판정함수,시퀀스) -> 시퀀스
# 시퀀스의 각 요소를 판정함수에 전달하여 True를 리턴하는 요소로만 구성된 새로운 시퀀스 리턴
# 판정 함수는 True 또는 False를 리턴하는 함수임 트루만 시퀀스에 넣음

def flunk(s):
    return s<60

# def filter(fn, lst): 이게 필터 함수
#     new_list = []
#     for a in lst:
#         if fn(a):
#             new_list.append(a)
#     return new_list

def is_even(s):
    return s % 2 == 0

#map 함수

def total(s,b):
    return s + b

#람다 함수
#*한 줄로 정의되는 함수의 축약 표현* / 함수의 이름이 없음 : 번수에 대입해서 사용
#lambda 인수 : 식
def increase(x):

    return x + 1
#lambda x: x + 1 위 함수와 같은 뜻

def main():
    ############################filter
    score = [45,89,72,53,94]
    for s in filter(flunk, score):
        print(s)
    even_list = list(filter(is_even, score))#list()에서 반복문이 돌며 저장하기때문에 가능함
    print(even_list)
    ###################################### map(함수,첫번째 함수의 매개변수 갯수만큼)
    score = [45,89,72,53,94]
    bonus = [2,3,0,0,5]
    for s in map(total, score, bonus):
        print(s, end = ", ")
    print()
    for i in range(5):
        print(total(score[i], bonus[i],),end=", ")
    print()

    ###################################### 람다 함수 : 함수를 정의 내린다
    #lambda x: x + 1#이식에 나온 결과값을 리턴한다 인수 : 식 (식의 결과를 인수에 리턴함)

    score = [45,89,72,53,94]
    for s in filter(lambda x:x<60, score): # 필터쓸떄 사용하는 람다함수 맵에서도 씀 람다는 함수다 * 중요 *
        print(s)
    # f = lambda x:x<60 만약 이 조건이 또 쓰인다면 이렇게 쓰면 실용적
    # for s in filter(f, score):
    #     print(s)

    for s in map(lambda x: x / 2, score):
        print(s, end = ", ")

main()

