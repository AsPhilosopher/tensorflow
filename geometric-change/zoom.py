import cv2
import numpy as np

img = cv2.imread('../img/test.jpg', 1)
imgInfo = img.shape
print(imgInfo)
height = imgInfo[0]
width = imgInfo[1]
mode = imgInfo[2]
# 1 放大 缩小 2 等比例 非等比例
dstHeight = int(height * 0.5)
dstWidth = int(width * 0.5)
# 最近临域插值 双线性插值 像素关系重采样 立方插值
dst = cv2.resize(img, (dstWidth, dstHeight))
cv2.imshow('image', dst)
# cv2.waitKey(0)

# 1.最近临域插值 2.双线性插值
# 1.按比例计算，取整
# 2.
img = cv2.imread('../img/test.jpg', 1)
height = imgInfo[0]
width = imgInfo[1]
desHeight = int(height / 2)
desWidth = int(width / 2)
dstImage = np.zeros((dstHeight, dstWidth, 3), np.uint8)  # 0-255
for i in range(0, desHeight):  # 行
    for j in range(0, desWidth):  # 列
        iNew = int(i * (height * 1.0) / desHeight)
        jNew = int(j * (width * 1.0) / dstWidth)
        dstImage[i, j] = img[iNew, jNew]
cv2.imshow('dst', dstImage)
# cv2.waitKey(0)

img = cv2.imread('../img/test.jpg', 1)
matScale = np.float32([[0.5, 0, 0], [0, 0.5, 0]])
dst = cv2.warpAffine(img, matScale, (int(width / 2), int(height / 2)))
cv2.imshow('dst2', dst)
cv2.waitKey(0)
