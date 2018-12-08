import cv2
import numpy as np

img = cv2.imread('../img/test.jpg', 1)
# cv2.imshow('src', img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
####
matShift = np.float32([[1, 0, 100], [0, 1, 200]])  # 2*3
dst = cv2.warpAffine(img, matShift, (height, width))  # 移位 矩阵运算
# cv2.imshow('dst', dst)
# cv2.waitKey(0)

'''
[1, 0, 100], [0, 1, 200] 2*2 2*1
[[1,0],[0,1]] 2*2 A
[[100], [200]] 2*1 B
xy C
A*C+B = [[x+100], [y+200]]
'''
img = cv2.imread('../img/test.jpg', 1)
cv2.imshow('src', img)
imgInfo = img.shape
dst = np.zeros(imgInfo, np.uint8)
# print(dst)
height = imgInfo[0]
width = imgInfo[1]
for i in range(0, height):
    for j in range(0, width - 100):
        dst[i, j+100] = img[i, j]
cv2.imshow('image', dst)
cv2.waitKey(0)
