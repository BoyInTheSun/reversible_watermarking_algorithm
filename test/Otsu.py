# -*- coding:utf-8 -*-
#本程序用于大津算法的实现
import cv2  #导入opencv模块
import os
import matplotlib.pyplot as plt
IMG = 'pic4.jpg'


img = cv2.imread(os.path.join("image", IMG))  # 导入图片，图片放在程序所在目录
cv2.namedWindow("imagshow")  # 创建一个窗口
cv2.imshow('imagshow', img)  # 显示原始图片

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转换为灰度图
cv2.namedWindow("gray")  # 创建一个窗口
cv2.imshow('gray', gray)  # 显示原始图片
retval, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)  # 使用大津算法进行图像二值化
cv2.namedWindow("dst")  # 创建一个窗口
cv2.imshow("dst", dst)
print('阈值是：', retval)

# 计算有无零点
count = dict()
count_zero = list()
for i in range(0, 256):
    count[i] = 0
for row in gray:
    for col in row:
        count[col] += 1
for i in count:
    if count[i] == 0:
        count_zero.append(i)
if len(count_zero) == 0:
    print('无零点')
else:
    print('有零点: 其灰度为', count_zero)


# 添加边框
dst1 = cv2.copyMakeBorder(dst, 1, 1, 1, 1, cv2.BORDER_CONSTANT, None, [0, 0, 0])
cv2.namedWindow("dst1")  # 创建一个窗口
cv2.imshow("dst1", dst1)
# 输出到csv文件
f = open('temp.csv', 'w')
for row in dst1:
    for col in row:
        f.write(str(0 if col == 0 else 1))
        f.write(',')
    f.write('\n')
f.close()
# 保存到bmp
cv2.imwrite('temp.bmp', dst1)
print(img)

plt.hist(gray.ravel(), 256, [0, 256])
plt.axvline(retval, color='red')
plt.show()
cv2.waitKey()
