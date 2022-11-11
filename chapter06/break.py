
#break 반복문을 벗어나게 함

score = [92,86,68,120,65]
for s in score:
    if(s<0) or (s>100):
        print(s,"가 범위를 벗어났습니다")
        break
    print(s)

print('성적 처리 끝')

#continue 완전히 반복문을 취소하지않고 그 밑에 문장을 실행하지않고 반복문으로 다시 돌아와서 그대로 진행
for s in score:
    if(s<0) or (s>100):
        print(s,"가 범위를 벗어났습니다")
        continue
    print(s)

# 구구단

for a in range(2,10):
    for b in range(2,10):
        print(int(a),"x", int(b), "=", a*b,end="  ")
    print()
