#이미지 필터링

from PIL import Image, ImageFilter

im = Image.open('phy.PNG')
blurImage = im.filter(ImageFilter.BLUR)

blurImage.save('python-blur.PNG')
blurImage.show()