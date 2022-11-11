users = {
        "go" : "g1234",
        "hong" : "h1234",
        "gang" : "g1234",
        "kong" : "k1234",
        "yang" : "yang"
    }

def get_user_info():
    id = input("아이디를 입력하세요")
    pw = input("비밀번호를 입력하세요")

    return id, pw

def check_login(user_id, password):#내꺼
    if user_id in users:
        pw = users.get(user_id)
        if password == pw:
            print("로그인 성공")
            return True
        else:
            print("비밀번호가 틀렸어")
    else:
        print("아이디가 없음")
    return False

def check_login2(user_id, password):#강사님꺼
    if user_id not in users:
        print(f"{user_id}는 존재하지 않는 ID 입니다")
        return False
    elif users[user_id] == password:
        return True
    else:
        print(f"비밀번호가 틀렸습니다")
        return False

def print_result(result, user_id):
    if result:
        print(f"로그인에 성공했습니다. 반갑습니다. {user_id}님")
    else:
        print("로그인에 실패했습니다. \n다음 기회에...")

def main():
    result = False

    for i in range(3):
        user_id, password = get_user_info()
        result = check_login2(user_id, password)
        if result:
            break
    print_result(result, user_id)

main()