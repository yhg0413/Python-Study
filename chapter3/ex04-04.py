#문자열 - 문자 코드
print(ord('a'))
print(chr(98))
for c in range(ord('A'), ord('Z')+1):
    print(chr(c), end="")

print(ord('a'))
print(chr(98))
for c in range(ord('A'), ord('Z')+1):
    print(chr(c),c)

# 진위형

a = 5
b = a == 5
print(type(b))
print(b)

if a == 5:
    print('a는 5입니다')
a = None
print(a)
#None 은 상수로 파이썬에서는 아무것도 아니라는 의미로 사용된다고함.
# int -> int( )
# float -> float( )
# str -> str( )
# bool -> bool( )
# 형변환 함수 여기까지 primitive 함수임