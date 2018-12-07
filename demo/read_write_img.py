import cv2

# 文件的读取 封装格式解析 数据解码 数据加载
# jpg/png[压缩编码] 文件头 文件数据
# img = cv2.imread("../img/test.jpg", 1)  # 1是彩色 0是灰色
# cv2.imshow('showName', img)  # 单位毫秒

# img = cv2.imread("../img/test.jpg", 1)
# cv2.imwrite('../img/copy_test.jpg', img)
# cv2.waitKey(0)

# img = cv2.imread("../img/test.jpg", 1)
# cv2.imwrite('../img/compress_test.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 0])  # 有损压缩 0-100

# jpg有损压缩 png无损压缩还可以设置透明度，数字越小压缩比越低
# img = cv2.imread("../img/test.jpg", 1)
# cv2.imwrite('../img/compress_test.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 0])  # 0-9

# 像素 RGB 颜色深度-->8bit 0-255 三种颜色 256的三次方
# w h 640 * 480（单位：像素）
# 1.14M = 720*547*3*8/8
# RGB alpha（透明度信息）
# RGB bgr
img = cv2.imread("../img/test.jpg", 1)
(b, g, r) = img[100, 100]  # bgr
print(b, g, r)
for i in range(1, 100):
    img[10 + i, 100] = (255, 0, 0)
cv2.imshow('pixel', img)
cv2.waitKey(0)
