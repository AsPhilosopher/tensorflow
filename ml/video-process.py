import cv2

'''
cap = cv2.VideoCapture('../mp4/1.mp4')
isOpened = cap.isOpened()
print(isOpened)
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(fps, width, height)
i = 0
while isOpened:
    if i == 10:
        break
    else:
        i += 1
    (flag, frame) = cap.read()
    fileName = '../img/ml/image' + str(i) + '.jpg'
    print(fileName)
    if flag:
        cv2.imwrite(fileName, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
'''

img = cv2.imread('../img/ml/image1.jpg')
imgInfo = img.shape
size = (imgInfo[1], imgInfo[0])
print(size)
# -1表示选择一个支持的解码器 第三个参数是帧数
videoWrite = cv2.VideoWriter('../mp4/test.mp4', -1, 5, size)
for i in range(1, 11):
    fileName = '../img/ml/image' + str(i) + '.jpg'
    img = cv2.imread(fileName)
    videoWrite.write(img)  # 写入方法
