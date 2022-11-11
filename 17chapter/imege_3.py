from PIL import Image


im = Image.open('phy.PNG')

#Thumbnail 이미지 생성
size = 64,64
im.thumbnail(size) #어디에도 대입하지 않았기에 im안의 값이 바뀌어버림

im.save('python-thumb.PNG')
im.show()

print(im.size)#변환된 사이즈