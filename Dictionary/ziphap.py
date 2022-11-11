#집합 정의
#{값1, 값2, ...}
#값의 중복을허용하지 않음
#키 없이 값만 중복없이 보관하고자 할때 사용

#set(다른 시퀸스) : 집합 변환 함수(문자열 튜플 리스트등) 사전은 안됌 사전은 시퀸스가아님
#.add(값) : 집합에 값 추가, 이미 값이 있으면 추가하지 않음
#.remove(값) : 집합에서 값을 제거, 값이 없는 경우 예외 발생
#집합은 비어있을수 없음 {} x
#set은 인덱스에 의한 참조가 안되고 순서가 랜덤으로 저장이 됌

#집합연산
#합집합 : 기호 ( | ) 메서드 : union 둘이 합친것 (중복제외)
#교집합 : 기호 ( & ) 메서드 : intersection 서로 둘다 가지고있는것
#차집합 : 기호 ( - ) 메서드 : difference 왼쪽에서 오른쪽 뺀것
#베타적 차집합 = 합집합-교집합 : 기호 ( ^ ) 메서드 : symmetric_difference 서로 다른거만

#부분지합
#진성 부분집합
#포함집합
#진성 포함집합
def main():
    asia = {'korea', 'china', 'japan', 'korea'}
    print(asia)

    print(set('aaabbbccc'))
    print(set([12,34,56,78]))
    print(set(('홍길동', '고길동', '둘리')))
    print(set({'boy' : '소년', 'school' : '학교' , 'book' : '책'}))#사전의 키목록을 집합으로 변환
    print(set())

    asia.add('vietnam')
    asia.add("korea")
    asia.remove("japan")
    print(asia)

    twox = {2,4,6,8,10,12}
    threex = {3,6,9,12,15}

    print("교집합", twox & threex)
    print("합집합", twox | threex)
    print("차집합", twox - threex)
    print("차집합", threex - twox)
    print("베타적 차집합", twox ^ threex)


main()