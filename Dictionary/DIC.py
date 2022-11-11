#10.1 사전
# 사전(Dictionnary)은 키와 값의 쌍을 저장하는 대용량의 자료구조. 해시알고리즘을 사용하여
# 일대일로 대응되는 특성이 있어 맵이라고도 부르고 관련된 키의 값의 쌍이라고 해서 연관배열이라고도 부른다
# 슬라이싱을 지원하지 않음 왜냐 위치정보가 없어서
# key : 특성 유일한 값으로 중복되선 안됌
# value : 값
#중복검사를 해야하기때문에 연산자를 지원하지않음 함수로 붙이거나 해야함
#dict() 함수가있음(변환)
#다른 언어에서는 map 이라고 함함
#순서는 의미가없음
#{
#   키1:값1,
#   키2:값2,
#   ...
#}
#get() = 있으면 값을 리턴 없으면 None을 리턴함 단 옆의 인자로 값을 따로 리턴가능



###################################

# dic = {
#         'boy' : '소년',
#         'school' : '학교',
#         'book' : '책'
#     }
#     name = 'boy'
#     print(dic[name])

###################################

    # dic = {
    #      'boy' : '소년',
    #      'school' : '학교',
    #      'book' : '책'
    #  }
    # print(dic.get('boy'))
    # print(dic.get('girl'))
    # print(dic.get("girl", "사전에 없는 단어입니다."))
    #
    # if 'student' in dic:#이게 get이랑 같은 역할함
    #     print('사전에 있는 단어')
    # else:
    #     print('이 단어는 없음')

######################################

#사전 관리
#사전[키] : 키의 값을 리턴, 키가 존재하지 않는 경우 에러 발생
#사전.get(키[, 기본값]): 키의 값을 리턴, 키가 존재하지 않는 경우, None리턴, 키가 없을 때 리턴할 값 지정가능
#.keys() : 키 목록 리턴
#.values() : 값 목록 리턴
#.items() : (키,값) 튜플 목록 리턴


# dic['boy'] = '남자아이'   #기존값 수정 있으면 바꿈
# dic['girl'] = '소녀'      #새로운 엔트리 추가 없으면 만들어보ㅓ림
# del dic["book"]         # 기존 엔트리 삭제
# print(dic)





def main():
    dic = {
         'boy' : '소년',
         'school' : '학교',
         'book' : '책'
     }
    print(dic.get('boy'))
    print(dic.get('girl'))
    print(dic.get("girl", "사전에 없는 단어입니다."))

    if 'student' in dic:#이게 get이랑 같은 역할함
        print('사전에 있는 단어')
    else:
        print('이 단어는 없음')
    print(dic.keys())
    print(dic.values())
    print(dic.items())

    keylist = dic.keys()#리스트의 역할을 하게 만듬 하지만 append 나 insert는 불가 하고싶으면
    for key in keylist: # = for key in dic.keys():
        print(key, dic[key])# 가장 기초적인 사전 순회방법

    li = list(dic.keys()) # 사전이 가진 키의 목록을 리스트화
    print(li)

    li = list(dic) # 이거도 키만 리스트화 시켜라~ 같은뜻
    print(li)

    dic = {
        'boy': '소년',
        'school': '학교',
        'book': '책'
    }
    dic2 = {
        'student': '학생',
        'teacher': '선생',
        'book': '서적'
    }
    dic.update(dic2)#겹치는 키가 있을시에 인자에 들어간것으로 업데이트함 책->서적
    print(dic)

    li = [
        ["boy", "소년"],
        ["school", "학교"],
        ["teacher","선생님"]
    ]
    dic = dict(li)#형변활할려면 저렇게 2차원으로 무조건 있어야함 아니면 안됌 키와 벨류값이 있어야함
    print(dic)

main()
