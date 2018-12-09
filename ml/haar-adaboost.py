# haar 特征 = 像素经过运算得到的结果(具体值 向量 矩阵 多维)
# 如何运用特征区分目标？ 如阈值判决等
# 如何得到阈值判决？机器学习
# 1 特征 2 判决 3 得到判决
# haar有一系列模板 滑动 缩放 运算量大
# 举例 1080*720 10*10
# 计算量=14模板 * 20缩放 * (1080/2*720/2) * (100点+-) = 50-100亿
# 实时处理 15祯 (50-100)*15 = 1000亿次
# 积分图
# haar + Adaboost face
# Adaboost分类器将错误样本不断加强
# 训练终止条件：1 for count 2 p(误差概率)
# haar> T1 and haar>T2 2个强分类器15-20
# 强分类器进行判决 弱分类器计算强分类器特征(由若干Node节点)
# Adaboost 训练：
# 1.初始化数据权值分布
# 苹果 苹果 苹果 香蕉
# 0.1 0.1 0.1 0.1
# 2 遍历判决阈值 p
# minP=t 最小误差概率
# G1(x) 计算一个权重
# 权值分布 update
# 满足终止条件 结束训练


import cv2

# 1load xml 2load jpg 3haar gray 4detect 5draw
face_xml = cv2.CascadeClassifier('../xml/haarcascade_frontalface_default.xml')
eye_xml = cv2.CascadeClassifier('../xml/haarcascade_eye.xml')
# img = cv2.imread('../img/face.jpg')
img = cv2.imread('../img/beautiful_girl.jpg')
cv2.imshow('src', img)
# haar gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 缩放系数:1.3 人脸[目标]最小不能小于多少像素 5
faces = face_xml.detectMultiScale(gray, 1.3, 5)
print('face=', len(faces))
# draw
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_face = gray[y:y + h, x: x + w]
    roi_color = img[y:y + h, x:x + w]
    eyes = eye_xml.detectMultiScale(roi_face)
    print('eye=', len(eyes))
    for (e_x, e_y, e_w, e_h) in eyes:
        cv2.rectangle(roi_color, (e_x, e_y), (e_x + e_w, e_y + e_h), (255, 0, 0), 2)
cv2.imshow('dst', img)
cv2.waitKey(0)
