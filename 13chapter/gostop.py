#고스톱 패 썩기 및 패 분배
import random

#출력하기
def print_result(deck,users):
    I = 0
    for N in users:
        I+=1
        print(f"{I} 번째 사용자 : {N}")
    print("사용하지 않은 패",deck)




def main():
    deck = []
    user_deck = []
    A = []
    Man = int(input("몇명이서 참여하시겠습니까"))
    for dec in range(48):
        deck.append(dec)
    for N in range(Man):
        user_deck.append(N)
        for N_card in range(6):
            A.append(random.choice(deck))
            deck.remove(A[N_card])
        user_deck[N] = A
        A=[]
    print_result(deck,user_deck)


main()