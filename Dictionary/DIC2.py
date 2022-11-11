


def main():
    users = {
        "go" : "g1234",
        "hong" : "h1234",
        "gang" : "g1234",
        "kong" : "k1234",
        "yang" : "yang"
    }

    for _ in range(3):
        id = input("아이디를 입력하세요")
        pw = input("비밀번호를 입력하세요")
        repw = users.get(id)
        if repw == pw:
            print("로그인에 성공하였습니다. 반갑습니다"+ id+"님")
            break
        elif repw == None:
            print(id + "는 존재하지 않는 아이디입니다")
        else:
            print("비밀번호가 틀립니다")
    if repw != pw:
        print("3회 이상 틀렸습니다 로그인을 제한합니다")




main()