import cv2

img = cv2.imread("../img/test.jpg", 1)  # 1是彩色 0是灰色
cv2.imshow('showName', img)
cv2.waitKey(0)
