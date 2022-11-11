#pickle 모듈
#파이썬 자료형 그래도 저장하고, 그대로 로드(복원)
#반드시 binary 모드로 오픈해야함
#다른 언어와 호한성이 없음
#import pickle
#저장하기
# pickle.dump(data,file)
# -data : 저장할 데이터
# -file:"bw"로 오픈한 파일 객체
# 로드하기
# data = pickle.load(file)
# -file : "br"로 오픈한 객체
# -data : 복원한 데이터
#사용할떄 확장명을 dat로 해서 만드는게 좋음
import pickle

def save(fpath, data):
    try:
        with open(fpath, 'wb') as file:
            pickle.dump(data, file)
    except Exception as e:
        print(f"{fpath} 파일 쓰기에 실패했습니다")
        print(e)

def load(fpath):
    try:
        with open(fpath, "rb") as file:
            data = pickle.load(file)
            return data
    except Exception as e:
        print(e)

def main():
    data = [
        [1,2,3,4,5],
        [6,7,8,9,10],
        [11,12,13,14,15]
    ]

    save("./data/data2.dat", data)
    data2 = load("./data/data2.dat")
    print(data2)

main()