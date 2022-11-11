#리스트의 사본 : 시퀀스.copy() -> 시퀀스 복사본
import copy
#프리미티브 (숫자 부울린 만 자료값이 정해져있는 것들은 스택영역에 저장되어있음 Stack
#하지만 시퀀스처럼 유동적인 변수들은 전역번수에 저장되서 변수명들이 어드레스값을 가지게 됌 튜플 셋 리스트 딕션 전부

def test_list(): # 왜그런지 알지? list2에 list1의 주소값이 들어가서 서로 같은 어드레스 가르켜서 값이 같은거
    list1 = [1, 2, 3]
    list2 = list1

    print(list1 == list2)

    list2[1] = 100

    print(list1)
    print(list2)

    print(list1 == list2)

def copy_list():
    list1 = [1,2,3]
    list2 = list1.copy()  # = list2 = list[:]

    print(list1 == list2)
    list2[1] = 100
    print(list1)
    print(list2)

    print(list1 == list2)

def copy_list2():
    list0 = ['a', 'b']
    list1 = [list0, 1, 2]
    list2 = list1.copy()

    list2[0][1] = 'c'
    list2[1]=-1
    print(list1)
    print(list2)
    print(list0)
    list2 = copy.deepcopy(list1)
    print(list1)
    print(list2)

def deep_copy_list(): # 완벽하게 참조에 참조한 값까지 전부다 값만 가져와서 데이터로 저장함 어드레스로 받아오지않고 주소만들고 값만 가져와 저장하기기
    list0 = ['a', 'b']
    list1 = [list0, 1, 2]
    list2 = copy.deepcopy(list1)

    list2[0][1] = 'c'
    list2[1]=-1
    print(list1)
    print(list2)
    print(list0)

def test(numbers):#이렇게해도 결국엔 주소값을 보낸거기때문에 변수의 자체값이 바뀜
    numbers[0] = -1
    print(numbers)

#def test2():
 #   numbers = [1,2,3]
def test2():
    numbers = [1,2,3]
    return numbers

def main():
    deep_copy_list()
    # list1 = [1,2,3]
    # test(list1) # numbers = list1
    # print(list1)

    #test2()# 이렇게 할경우 함수에서 나와도 안에 선언안 전역변수에 있는 리스트가 안사라짐 메모리만 먹는데 그걸 파이썬이 알아서 삭제함
    list2 = test2()#이래하면 당연히 안사라지죠
    print(list2)

    #이중 리스트를 카피할때도 deepcopy사용하기
    #대부분의 함수가 새로운 변수로 리턴되는 이유는
    #그 함수 안에서 카피를 사용해서 그 값으로 리턴하기 때문이라고 함.
main()