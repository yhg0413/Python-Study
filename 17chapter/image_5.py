from PIL import Image

def center_crop(im):
    crop_size = min(im.size)

    left = (im.size[0] - crop_size) // 2
    top = (im.size[1] - crop_size) // 2
    right = (im.size[0] + crop_size) // 2
    bottom = (im.size[1] + crop_size) // 2

    return im.crop((left, top, right, bottom))#crop는 매개변수를 튜플로받음

im = Image.open('phy.PNG')
cropImage = center_crop(im)
cropImage.save('python_crop_c.PNG')
cropImage.show()