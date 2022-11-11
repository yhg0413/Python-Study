#동일한 데이터파일을 연속적으로 저장하는 것을 배열이라고함

#시퀀스 데이터로부터 배열 생성

#arr_obj = np.array(seq_data)
#시퀀스 데이터(리스트,튜플 등)를 배열로 변경
#배열의 속성
#dtype : 배열 요소의 데이터 타입
#shape : 배열의 모양(차원)을 튜플로 표현
#reshape(m,n)
#배열의 차원 조정, m x n 형태로 변경 , *데이터의 개수가 맞아야함
#1차원 배열을 백터라 부르고 2차원을 행열 3차원 이상은 N차원 배열 이라고 부름

#범위를 지정해 배열 생성
#arr_o
import numpy as np

data1 = [0,1,2,3,4]
a1 = np.array(data1)
print(a1)

data2 = [0.1,5,4,12,0.5]
a2 = np.array(data2)
print(a2)
print(a1.dtype)
print(a2.dtype)

print(np.array([0.5,2,0.01,8]))
print(np.array([[1,2,3],[4,5,6],[7,8,9]]))

