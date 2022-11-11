




def save(text_name,data):
    f=open(text_name, "wt", encoding="utf8")
    for l in data:
        l = map(str, l) #l의 요소들을 문자열로 만듬
        row = ','.join(l)
        f.write(row+"\n")
    f.close()
    pass

def main():
    data=[
        [1,2,3,54,45],
        [7,8,3,4,5],
        [1,12,13,4,26]
    ]
    save("data.csv",data)



    pass

main()