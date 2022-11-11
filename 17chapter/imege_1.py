#  PIL
# ○ 파이썬 이미지 처리 라이브러리
# ○ pip install pillow
#  아나콘다에 기본 탑재되어 있음
    #패키지명    클래스 대문자로 시작함
from PIL import Image

#이미지 열기
            #이 오픈이 스태틱 메서드 (인스턴트 안만들고 실행함)
            #팩터리 함수라고 부름 만들어서 줌 factory(객체의 생성과정을 단순화해서 만들어줌)
im = Image.open('phy.PNG')

#이미이 크기 출력
print(im.size)

#이미지 JPG로 저장

im.save('python.png')

#이미지 화면 출력
im.show()# 윈도우즈의 그림보여주는 프로그램으로 틀어주는 것