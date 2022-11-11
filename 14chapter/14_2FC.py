#파일 관리 함수
#shutil 패키지 shell utility
#shutil.copy(a, b) : a파일을 b파일로 복사해라 a b 둘다 파일에 대한 경로
#shutil.move(a, b) : a의 경로를 b로 옮겨라
#shutil.rmtree(path) : 디렉토리를 삭제함 원래는 비어있는 디렉토리만 삭제할수있다 . 근데 이걸쓰면 하위개체 전부다 같이 삭제

#os.rename(a,b) 이름 바꾸기
#os.remove(f) 지우기


#디렉토리 관리함시
# os.chdir(d) : 워킹디렉토리를 바꿈
# os.madir(d) : 디렉토리 생성
# os.rmdir(d) : 디렉통리 제거
# os.getcwd() : 현재 디렉토리 문자열로 반환
#
# os.listdir(d) : 디렉토리 목록을 리스트로 반환
# #is로 시작하는 모든 함수의 리턴타입은 True or False
#
# os.path.isabs(f) : 절대 경로인지 검사
# os.path.abspath(f) : 파일의 절대 경로를 구함
# os.path.realpath(f) :원본파일의 경로를 구함
# os.path.exists(f) : 파일의 존재 여부를 조사함 디렉토리 포함?
# os.path.isfile(f) : 파일인지 조사함
# os.path.isdir(f) : 디렉토리인지 조사함
#os.path.join(path,f)


import shutil
import os

def dumpdir(path):
    files = os.listdir(path)
    for f in files:
        fullpath = os.path.join(path,f)#디렉토리와 파일의 경로를 결합할때 사용함 path는 디렉토리 경로 f에는 파일 이름이 들어감 그래서 파일의 절대 경로값으로 만들어 줌 ㅇㅋ?
        if os.path.isdir(fullpath):
            print(f"[{fullpath}]")
            dumpdir(fullpath) #재귀호출
        else:
            print("\t", f)

shutil.copy("/temp/live.txt", "/temp/live3.txt")

def main():
    dumpdir('/temp')

main()
