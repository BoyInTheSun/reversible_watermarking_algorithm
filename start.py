import border_following
import capacity_calculating
import cv2
import os
IMG = os.path.join('test', 'image', 'pic1.jpg')
input_image_path = 'test/image/Lena.jpg'

img = cv2.imread(IMG)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_output = img_gray.copy()
imgs_border = border_following.main(img_gray, min_step=20)
for i in range(len(imgs_border)):
    '''
    cv2.namedWindow(str(i))  # 创建一个窗口
    cv2.imshow(str(i), imgs_border[i])
    cv2.waitKey(0)
    '''
    temp = capacity_calculating.finding_max_and_min(img_gray, imgs_border[i], input_image_path)
    for m in range(len(temp)):
        for n in range(len(temp[i])):
            if imgs_border[i][m, n]

