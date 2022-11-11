#이미지 <--> numpy배열

from PIL import Image
import numpy as np
#픽셀 단위 작업할때 필요함
#이미지 객체의 색상정보만 변환시켜주는 함수 차원을 가지고 데이터를 관리함
# Image --> numpy array
im = Image.open('phy.PNG')# im2arr.shape:height x width x channel
im2arr = np.array(im)
print(im2arr.shape) #3차원 데이터로 관리함

#numpy array --> Image
arr2im = Image.fromarray(im2arr)

