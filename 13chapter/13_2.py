#finally
#예외 발생 여부와 상관없이 항상 호출

def comm():
    try:
        print("네트워크 접속")
        d = 0
        if d != 0:
            return
        a = 2/d
        print("네트워크 통신 수행")
    except:
        pass
    finally: #어떤 이유에서건 try 블럭을 벗어나게되면 반듯이 실행하게 됌 리턴도 하기전에 꼭 함
        print("접속 해제")
    print("작업 완료")
#####################
#assert 조건, 메세지 단정문 if + raise
#조건이 True이면 통과, False이면 메세지를 가지는 예외 발생
def main():
    comm()
    score = 128
    assert score <= 100, "점수는 100 이하여야 합니다."#score는 100이하여야만하고 아니면 에러
    print(score)#           에러메시지로 이게 뜸

main()