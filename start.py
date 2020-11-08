import border_following
import cv2
import os
IMG = os.path.join('test', 'image', 'pic1.jpg')


img = cv2.imread(IMG)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgs_border = border_following.main(img_gray, min_step=20)
for i in range(len(imgs_border)):
    cv2.namedWindow(str(i))  # 创建一个窗口
    cv2.imshow(str(i), imgs_border[i])
    cv2.waitKey(0)
