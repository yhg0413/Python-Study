#인수
#가변인수 #기호로 지정하며 타입은 튜플이 됌
#키워드 인수

def int_sum(*numbers):#가변인수
    print(numbers)
    total = 0
    for n in numbers:
        total += n
    return total

def calcstep(begin, end, step):
    total = 0
    for num in range(begin, end + 1, step):
        total += num
    return total

#키워드 가변인수
#키워드 인수를 가변 개수로 전달할 때 사용하는 방법
#**기호로 지정하여 타입은 사전이 됌

def calcstep2(**args):
    print(args)
    print(type(args))
    begin = args['begin']
    end = args['end']
    step = args['step']

    total = 0
    for num in range(begin, end+1, step):
        total += num
    return total

def calcstep3(**args):# 키워드 가변함수 파이썬만의 고유기능
    begin = args.get('begin, 1')
    end = args['end']
    step = args.get('step',1)#이렇게 get을 사용하면 디폴트 값을 잡을수있음

    total = 0
    for num in range(begin, end+1, step):
        total += num
    return total

def fun (**kwargs):#**를 두개넣으면 매개변수가 사전을 넣어야함
    dic = {'a':1, 'b':2}


def main():
    #print(int_sum(1,2,3,4,5))
    #print(int_sum())#이런경우 루프 안돌고 그냥 긑남 가변인수

    # print("3~5 = ", calcstep(3,5,1))# 위치기반만 사용한 것
    # print("3~5 = ", calcstep(begin=3, end=5, step=1))
    # print("3~5 = ", calcstep(step=1, end=5, begin=3))
    # print("3~5 = ", calcstep(3, 5, step=1))# 이건 왼쪽에 그냥인자 채우고 남는자리에 키워드 인수 쓰래
    # print("3~5 = ", calcstep(3, step=1, end=5))



    # a = 10
    # b = 20
    # print(a, b)
    # print(a, b, sep=',')
    # print(a, b, sep=',',end='$')
    # print(a, b, end='$',spe=',')

    print("3~5 = ", calcstep2(begin=3, end=5, step=1))
    print("3~5 = ", calcstep2(step=1, end=5, begin=3))
    # print("3~5=",calcstep2(end=5)) 호출시 자체는 괜찮지만 없는 키에 접근하기에 에러남 하지만 디폴트 값을주면 가능
    #인자에 리스트나 튜플늘 넣고싶을때
    #print([1,[2,5,7],3])
    #print(1,*list,3)
    #calcstep("김한슬",99,98,95,80,avg=False)
    #calsstpe(name,*score,*option)#일반변수 가변변수 키워드가변변수 순으로 배치

main()