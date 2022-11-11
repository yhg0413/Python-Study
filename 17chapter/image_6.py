#이미지 회전 및 Resize

from PIL import Image
im = Image.open("phy.PNG")

#크기를 600x600 으로

img2 = im.resize((600,600)) #가로세로무시하고 사이즈 맞춤
img2.save('python-600.PNG')
img2.show()


#90도 회전
img3 = im.rotate(90)
img3.save("python-rotate.PNG")
img3.show()