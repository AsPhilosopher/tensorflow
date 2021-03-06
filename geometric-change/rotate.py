import cv2
import numpy as np

img = cv2.imread('../img/test.jpg', 1)
cv2.imshow('src', img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
# 中心点 旋转角度 缩放
matRotate = cv2.getRotationMatrix2D((height * 0.5, width * 0.5), 45, 0.5)
dst = cv2.warpAffine(img, matRotate, (height, width))
cv2.imshow('dst', dst)
cv2.waitKey(0)
