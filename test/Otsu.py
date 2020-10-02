# -*- coding:utf-8 -*-
#本程序用于大津算法的实现
import cv2  #导入opencv模块
import os
import matplotlib.pyplot as plt
IMG = 'pic3.jpg'


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

plt.hist(gray.ravel(), 256, [0, 256])
plt.axvline(retval, color='red')
plt.show()
cv2.waitKey()
