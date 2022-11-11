from user_models import User

def print_list(total,rows):
    # 값이 없을경우 빈 튜플값이 리턴됌
    print("=" * 50)
    header = ("이름", "전화번호", "주소", "나이")
    print(f"No {header[0]:10}{header[1]:10}{header[2]:10}{header[3]:10}")
    print("-" * 50)
    for ix, row in enumerate(rows, 1):  # 빈튜플이면 반복문 안돌고 탈출
        print(f"{row.id}: {row.name:10} {row.phone:10} {row.addr:10} {row.age:10} ")
    print("=" * 50)
    print(f"(총 {total} 건)")

def input_addr_info():
    name = input("이름 : ")
    phone = input("전호번호 : ")
    addr = input("주소 : ")
    age = input("나이 : ")
    return User("",name, phone, addr, age)

def input_update_info(data):
    phone = input(f"전화번호({data.phone}) : ")
    if not phone:
        phone = data.phone
    addr = input(f"주소({data.addr}): ")
    if not addr:
        addr = data.addr

    age = input(f"나이({data.age}): ")
    if not age:
        age = data.age
    print("=" * 20)
    return User(data.id,data.name, phone, addr, age)