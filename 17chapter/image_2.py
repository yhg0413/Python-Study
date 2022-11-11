#색상 변경

from PIL import Image

#이미지 열기

#convert : "L" (grau), "RGB", "RGBA", "CMYK"
#객체로 반환한 함수나 class에서 객체에서 바로 메소드로 다시 이용하는것
# = im.convert("L")랑 같음
im = Image.open('phy.PNG').convert("L") #메서드 체이닝

im.show()

