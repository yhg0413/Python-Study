#컬렉션관리

#enumerate(시퀸스[, start])start디폴트는 0
#시퀀스의 인덱스 요소를 튜플 묶어서 순회

#변수명 또는 함수명 지을때의 관례

#EX
# selesrate    SalesRate    sales_rate    salesRate     sales-rate
# menudic      MenuDic      menu_dic      menuDic       menu-dic
# printaverage PrintAverage print_average print_Average print-average
# 이건 ㄴㄴ     Pascal case  snake case    camel case    kebab case(프로그래밍에선 -연산자로 인식해서 못쓰고 HTML에선 씀)
#                           c/c++         자바에서 자주사용 파이썬은 다 상관없음 케밥빼고
#함수는 동사로 시작되게 만드는게 좋음
def enumerateM():
    score = [88,95,70,100,99]

    for i,value in enumerate(score,1):#ix, value = 0, 88(튜플의 언팩기능을 이용한 것) 튜플사용하는데 인덱스 번호가 필요할때 많이사용
        print("성적 : ", i, value)
    race = ['저그', '테란', '프로토스']
    print(list(enumerate(race)))

    for no, s in enumerate(score, 1):
        print(str(no) + "번 학생의 성적 : " ,s)
#zip(시퀸스1, 시퀸스2) -> [(값1,값2),...]
#시퀸스 길이가 다른경우 가장 짧은 시퀀스의 길이에 맞춤

def zips():
    dates = ['월', '화', '수', '목', '금', '토', '일']
    food = ["갈비탕", "순대국", "칼국수", "삼겹살"]
    price = ["6000", "5000", "7000", "6000", "1"]

    menu = zip(dates, food,price)#zip도 가변인수 처리가 되어있어 변수의 개수는 상관없음
    for d, f, p in menu:
        print(f"{d}요일 메뉴 : {f} 가격 : {p}")

    menu_dic = dict(zip(dates, food))#사전을 제일 많이쓰는 경우
    print(menu_dic)

#any(), all()
#any(시퀸스) 시퀸스에 하나라도 True가 있으면 True 리턴
#all(시퀸스) 시퀀스에 모든 요소가 True이면 Treu 리턴

def main():
    zips()

main()
