#14.1 파일 입출력

#파일쓰기
#open(파일경로, 모드)
# 모드
# r : 읽기, 파일이 없는 경우 예외 발생
# w : 쓰기, 파일이 없으면 새로 생김 보통 처음이지만 자기가 쓰고싶은곳에 씀 닫고 다시쓸경우 아예 초기화하고 새로씀
# a : 추가 기존 내용 끝에다가 내용 덧붙이겠다 = 파일은 안닫고 w를로 계속 쓰는것과 같음
# x : 쓰기용으로 여나 기존 파일이 있는 경우 실패
# t : text 모드로 열기  문자파일은 이걸로열고
# b : binary 모드로 열기 그림이나 숫자등인 파일은 이거로 열래
# 마지막에는 항상 close를 할것
def text_write():
    f = open("temp/live.txt", "wt",encoding="utf8")
    f.write("""삶이 그대를 속일지라도
슬퍼하거나 노하지 말라!
우울한 날들을 견디면
믿으라, 기쁨의 날이 오리니""")
    f.close()

    f = open("temp/live.txt", "wt",encoding="utf8")
    f.write("""삶이 그대를 속일지라도
슬퍼하거나 노하지 말라!
우울한 날들을 견디면
믿으라, 기쁨의 날이 오리니""")
    f.close()
def text_write2():
    f = open("temp/live2.txt", "wt")
    f.write("""삶이 그대를 속일지라도
슬퍼하거나 노하지 말라!
우울한 날들을 견디면
믿으라, 기쁨의 날이 오리니""")
    f.close()

    f = open("temp/live2.txt", "wt")
    f.write("""삶이 그대를 속일지라도
슬퍼하거나 노하지 말라!
우울한 날들을 견디면
믿으라, 기쁨의 날이 오리니""")
    f.close()


##############
#파일 읽기
#f.read() -> 파일 전체 내용
#f.read(n) -> n개의 내용
#f.readline() -> 한줄
#f.readlines() -> 전체 라인 리스트(각 라인 끝에 개행문제가 들어 있음)

def text_read():
    try:
        f = open("/temp/live.txt", "rt",encoding="utf8")
        text = f.read()
        print(text)
    except FileNotFoundError:
        print("파일이 없습니다.")
    finally:
        f.close()

    try:
        f = open("/temp/live.txt", "rt",encoding="utf8")
        while True:
            text = f.read(10)
            if len(text) == 0: break
            print(text,end = '')
        print()
    except FileNotFoundError:
        print("파일이 없읍니다.")
    finally:
        f.close()

def text_readline():
    try:
        f = open("/temp/live.txt", "rt",encoding="utf8")
        text = ""
        line = 1
        while True:
            row = f.readline()
            if not row: break
            text += str(line) + " : " + row
            line += 1
    except FileNotFoundError:
        print("파일이 없습니다.")
    finally:
        f.close()
    print(text)

def text_readlines2():
    try:
        f = open("/temp/live.txt", "rt", encoding="utf8")
        rows = f.readlines()

        for I,row in enumerate(rows,1):

            print(f"{I} : {row}", end="")

    except  FileNotFoundError:
        print("파일 없")
    finally:
        f.close()

def text_readlines():
    try:#절대좌표로 입력할거면 역슬레시 두개 표준은 /로 쓰는데 윈도우에서 쓸떈 \니까 잘 구분에서 쓰쎔
        f = open("/temp/live.txt", "rt", encoding="utf8")
        rows = f.readlines()
        for row in rows:
            print(row, end ='')
    except FileNotFoundError:
        print("파일이 존재하지 않습니다")
    finally:
        f.close()



def Seek(): # 이친구는 맘대로 인코딩 디코딩하면서 못씀 입력한 칸수만큼 띄어서 읽기를 시작하게 해줌
    try:
        f = open("/temp/live2.txt", "rt")
        f.seek(12,0)
        text = f.read()
    except FileNotFoundError:
        print("파일이 존재하지 않습니다")
    finally:
        f.close()

    print(text)

##append

def text_append(): # 예는 인코딩 해도 괜찮음
    try:
        with open('temp/live1.txt', "at", encoding="utf8") as f:
            text = f.write("""살고싶다고 말해"""
            )
    except Exception as e:
        print(e)



############### with ~s 얘 를사용하면 with블록을 나갈때 자동으로 close를 사용해줌
def with_open():
    try:
        with open('test.txt', 'r') as file:
            text = file.read()
            print(text)
    except Exception as e:
        print(e)#원인을 몰라도 이렇게하면 원인을 알려줌 에러창에서


def main():
    text_write() #파일을 찾거나 생성되는 위치를 워킹 디렉토리라고 함 WORKING DIRECTORY
    text_read()
    text_readline()
    text_readlines2()
    Seek()
    text_append()
    text_read()

main()
#아래 터미널에서 입력하는거
#경로를 안쓰고 python 14_1_FIO.py 만 입력했을때는 상대경로라고 부름
#python \workspace\01_python\14chapter\14_1_FIO.py 이렇게 싹 기술해서 경로 입력하는걸 절대 경로라고 부름
#dir 현재 디렉토리의 내용을 출력해주는 것
#mkdir 폴더명 디렉토리를 만들어라(make directory) dir로 확인해볼수있음
#copy 워킹디렉토리의파일명 복사할디렉토리\파일명
#상대경로와 절대경로의 차이점 절대경로는 \로 시작함
#type 텍스트 파일의 파일을 출력하는 명령어
#.은 현재디렉토리 ..은 부모디렉터리(상위)