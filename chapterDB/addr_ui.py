from addr_models import Addr

def print_list(total,rows):
    # 값이 없을경우 빈 튜플값이 리턴됌
    print("=" * 50)
    header = ("이름", "전화번호", "주소")
    print(f"No {header[0]:10}{header[1]:10}{header[2]:10}")
    print("-" * 50)
    for ix, row in enumerate(rows, 1):  # 빈튜플이면 반복문 안돌고 탈출
        print(f"{ix} : {row.name:10} {row.phone:10} {row.addr:10} ")
    print("=" * 50)
    print(f"(총 {total} 건)")

def input_addr_info():
    name = input("이름 : ")
    phone = input("전호번호 : ")
    addr = input("주소 : ")
    return Addr(name, phone, addr)

def input_update_info(data):
    phone = input(f"전화번호({data.phone}) : ")
    if not phone:
        phone = data.phone
    addr = input(f"주소({data.addr}): ")
    if not addr:
        addr = data.addr
    print("=" * 20)
    return Addr(data.name, phone, addr)