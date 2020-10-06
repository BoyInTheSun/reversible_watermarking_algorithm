#!/usr/bin/python3.6

import cv2
import os
import sys
import numpy as np

# 调整栈大小
sys.setrecursionlimit(1000000000)
IMG = os.path.join('test', 'image', 'pic1.jpg')
SPEED = 1000  # 显示速度，最慢为1，最快无穷
ZOOM = 2  # 显示缩放倍数，1为原始大小
IS_SHOW = True

binary_temp = None
step = 0
count = dict()
move_x = [-1, -1, 0, 1, 1, 1, 0, -1]
move_y = [0, -1, -1, -1, 0, 1, 1, 1]


def show_step(time):
    global binary_temp
    x = len(binary_temp[0])
    y = len(binary_temp)
    # 新建RGB的numpy数组
    new = np.full((y, x, 3), 255).astype('uint8')
    a = {0: [0, 0, 0], 1: [255, 255, 255], 2: [255, 0, 0], -2: [0, 0, 255]}
    for i in range(len(binary_temp)):
        for j in range(len(binary_temp[i])):
            new[i, j] = a[binary_temp[i, j]]
    new = cv2.resize(new, (x * ZOOM, y * ZOOM), interpolation=cv2.INTER_AREA)
    cv2.namedWindow("show_step")  # 创建一个窗口
    cv2.imshow('show_step', new)
    cv2.waitKey(time)

# 重写该函数，递归次数过多导致栈溢出！
'''
# binary_temp为带边框的二值图，m, n为横纵坐标，now为当前位移，first为false代表该点为起点
def border_following(m, n, start_m, start_n, now, is_first):
    global is_done
    global binary_temp
    global count
    global step
    global step_each
    step += 1
    step_each += 1
    if IS_SHOW and step % SPEED == 0:
        show_step(1)
    for i in range(now, now + 8):
        # 顺时针找到第一个非零点
        if binary_temp[n + move_y[i % 8], m + move_x[i % 8]] != 0:
            now = i % 8
            # 右侧为0标记为-2，否则标记为2
            if binary_temp[n, m + 1] == 0:
                binary_temp[n, m] = -2
            else:
                binary_temp[n, m] = 2
            break
    # 周围全是零点，标记-2
    else:
        # 中心点为1，标记为-2
        if binary_temp[n, m] == 1:
            binary_temp[n, m] = -2
        # 中心点位0，向右寻找1，到最右则下一行
        elif binary_temp[n, m] == 0:
            # 向右侧找到下一个起点，如右侧没有从下一行开始找
            while True:
                # 如果遇到2，跳到下一个-2
                if binary_temp[n, m] == 2:
                    while True:
                        m += 1
                        # 到最右跳出
                        if m == len(binary_temp[0]) - 1:
                            break
                        # 遇到-2跳出
                        if binary_temp[n, m] == -2:
                            break
                # 向右侧
                if m < len(binary_temp[n]) - 1:
                    m += 1
                # 到最右则下一行
                else:
                    m = 1
                    n += 1
                if n == len(binary_temp) - 1:
                    return
                if binary_temp[n, m] == 1:
                    border_following(m, n, m, n, 0, True)
                    if is_done:
                        return
    if is_first:
        # print(m, n, is_done)
        is_first = False
    # 开始新的一轮
    elif n == start_n and m == start_m:
        # 向右侧找到下一个起点，如右侧没有从下一行开始找
        while True:
            # 如果遇到2，跳到下一个-2
            if binary_temp[n, m] == 2:
                while True:
                    m += 1
                    # 到最右跳出
                    if m == len(binary_temp[0]) - 2:
                        break
                    # 遇到-2跳出
                    if binary_temp[n, m] == -2:
                        break
            # 向右侧
            if m < len(binary_temp[n]) - 1:
                m += 1
            # 到最右则下一行
            else:
                m = 1
                n += 1
            if n == len(binary_temp) - 1:
                count[len(count)] = step_each
                is_done = True
                return
            if binary_temp[n, m] == 1:
                count[len(count)] = step_each
                step_each = 0
                border_following(m, n, m, n, 0, True)
                if is_done:
                    return
    for i in range(now - 1, now - 9, -1):
        # 逆时针找到第一个非零点作为下个中心
        temp = binary_temp[n + move_y[i % 8], m + move_x[i % 8]]
        if temp != 0:
            border_following(m + move_x[i % 8], n + move_y[i % 8], start_m, start_n, (i + 4) % 8, is_first)
            if is_done:
                return
            break
'''

def find_center(m, n):
    while True:
        # 如果遇到2，跳到右侧的-2
        if binary_temp[n, m] == 2:
            while True:
                m += 1
                # 到最右跳出
                if m == len(binary_temp[0]) - 1:
                    break
                # 遇到-2跳出
                if binary_temp[n, m] == -2:
                    break
        # 向右寻找
        if m < len(binary_temp[0]) - 1:
            m += 1
        # 到最右后向下
        else:
            m = 1
            n += 1
        # 结束
        if n == len(binary_temp) - 1:
            return None, None
        # 返回1点坐标
        if binary_temp[n, m] == 1:
            return m, n

def border_following(m, n):
    global binary_temp
    global count
    global step
    step_each = 0
    now = 0
    # 找中心
    if binary_temp[n, m] == 0:
        m, n = find_center(m, n)
        # 结束
        if m is None and n is None:
            return
    start_m = m
    start_n = n
    while True:
        step += 1
        step_each += 1
        # 显示当前进度
        if IS_SHOW and step % SPEED == 0:
            show_step(1)

        # 顺时针找到第一个非零点
        for i in range(now, now + 8):
            if binary_temp[n + move_y[i % 8], m + move_x[i % 8]] != 0:
                # 右侧为0标记为-2
                if binary_temp[n, m + 1] == 0:
                    binary_temp[n, m] = -2
                # 否则标记为2
                else:
                    binary_temp[n, m] = 2
                now = i % 8
                break
        # 周围全是零点，标记-2，进行下一轮标记
        else:
            binary_temp[n, m] = -2
            count[len(count)] = step_each
            m, n = find_center(m, n)
            # 结束
            if m is None and n is None:
                return
            border_following(m, n)
            return

        for i in range(now - 1, now - 9, -1):
            # 逆时针找到第一个非零点作为下个中心
            if binary_temp[n + move_y[i % 8], m + move_x[i % 8]] != 0:
                now = (i + 4) % 8
                n += move_y[i % 8]
                m += move_x[i % 8]
                break
        # 回到起点时进行下一轮
        if n == start_n and m == start_m:
            count[len(count)] = step_each
            m, n = find_center(m, n)
            # 结束
            if m is None and n is None:
                return
            border_following(m, n)
            return


img = cv2.imread(IMG)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshold, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
for i in range(len(binary)):
    for j in range(len(binary[i])):
        if binary[i, j] == 255:
            binary[i, j] = 1
binary_with_border = cv2.copyMakeBorder(binary, 1, 1, 1, 1, cv2.BORDER_CONSTANT, None, [0, 0, 0])
binary_with_border = binary_with_border.astype(np.int8)
# 输出到csv文件
f = open('binary_with_border.csv', 'w')
for row in binary_with_border:
    for col in row:
        f.write(str(col))
        f.write(',')
    f.write('\n')
f.close()
binary_temp = binary_with_border

# 递归标记边界
# border_following(1, 1, 1, 1, 0, True)
border_following(1, 1)
# 裁剪掉之前添加的最外一圈
binary_temp = binary_temp[1: -1, 1: -1]
# print(after_border_following)
# 输出到csv文件
f = open('after_border_following.csv', 'w')
for row in binary_temp:
    for col in row:
        f.write(str(col))
        f.write(',')
    f.write('\n')
f.close()
print('标记了{}个像素，共{}轮'.format(step, len(count)))
print('其中 ', count)
show_step(0)



# cv2.imwrite('temp.bmp', binary_with_border)  # 输出图片
# cv2.imshow("binary_with_border", binary_with_border)
# cv2.waitKey()
