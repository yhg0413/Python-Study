song = """by the rivers of babylon, there we set down
yeah we wept, when we remember zion.
when the wicked carried us away in captivity
required from us a song
now how shall we sing the lord's song in a strange land"""

def get_value(x):# 튜플의 두번째 값을 리턴하는 함수
    return x[1]

alphabet = dict()

for c in song:
    if c.isalpha() == False:
        continue

    c = c.lower()
    if c not in alphabet:
        alphabet[c] = 1
    else:
        alphabet[c] +=1
key = list(alphabet)
key.sort()
for c in key:
    num = alphabet[c]
    print(c, '=>', num)

alphabet_list = list(alphabet.items())
#alphabet_list.sort(key=get_value)#key = 변환 기준점 아래 람다랑 똑같음
alphabet_list.sort(key=lambda x:x[1], reverse=True)
for item in alphabet_list:
    print(item, end = " ")
print()
for a, c in alphabet_list:
    print(f"{a}, : {c}")