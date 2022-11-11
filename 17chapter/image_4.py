from PIL import Image


im = Image.open("phy.PNG")
cropImage = im.crop((0,0,300,300)) #(좌,상,우,하)(시작좌표와 끝좌표로 사각형그려서 그 사각형으로 그림)
cropImage.save("python-crop.PNG")
cropImage.show()