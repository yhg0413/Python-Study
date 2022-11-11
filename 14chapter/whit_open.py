def save(fpath, data):
    try:
        with open(fpath, "wt") as f:
            for l in data:
                l = map(str, l)
                row = ','.join(l)
                f.write(row + "\n")
    except Exception as e:
        print(e)

def load(fpath):
    try:
        with open(fpath, "rt") as f: # #f = open(fpath, "rt")와 동일 with ~as 써서 파일 클로즈할필요 없음음
            lines = f.readlines()
            data = []
            for line in lines:
                row = line.split(',')
                row = list(map(int,row)) #문자열 요소를 정수 요소로 변환
                data.append(row)
            return data
    except Exception as e:
        print(e)

def main():

    pass

main()
