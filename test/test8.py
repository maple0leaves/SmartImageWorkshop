import cv2
import numpy as np

red = (0, 0, 255)
blue = (243, 191, 0)
white = (255, 255, 255)
img = cv2.imread('../1.jpg', 1)

new_img = cv2.resize(img, None, fx=0.5, fy=0.5)
rows, cols, channels = new_img.shape
print(rows, cols, channels)
# 显示图像
cv2.imshow('new_img', new_img)

# 将图片转换为灰度图片
gray_img = cv2.cvtColor(new_img, cv2.COLOR_BGR2HSV)

# 图片二值化处理
low_value = np.array([90, 70, 70])
high_value = np.array([110, 255, 255])
binary_img = cv2.inRange(gray_img, low_value, high_value)

# 腐蚀膨胀
erode = cv2.erode(binary_img, None, iterations=1)
dilate = cv2.dilate(erode, None, iterations=1)
# cv2.imshow('dilate', dilate)

# 遍历替换
for i in range(rows):
    for j in range(cols):
        if dilate[i, j] == 255:
            # 此处替换颜色，为BGR通道
            new_img[i, j] = red   # (0, 0, 255)替换为红底   (255, 255, 255)替换为白底



cv2.imshow('red_bg_img', new_img)
# 窗口等待命令  0表示无限等待
cv2.waitKey(0)
cv2.destroyAllWindows()
# import cv2
# import numpy as np
#
#
# # 读取照片
# image = cv2.imread('../1.jpg')
# # image = cv2.imread('img_1.png')
# # 修改尺寸
# image = cv2.resize(image, None, fx=0.5, fy=0.5)
# # 图片转换为二值化图
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# print(hsv)
# # 图片的二值化黑白处理
# lower_blue = np.array([90, 70, 70])
# upper_blue = np.array([110, 255, 255])
# heibai = cv2.inRange(hsv, lower_blue, upper_blue)
# # 闭运算
# k = np.ones((5, 5), np.uint8)
# r = cv2.morphologyEx(heibai, cv2.MORPH_CLOSE, k)
# # 颜色替换
# imageNew = np.copy(image)
# rows, cols, channels = image.shape
# for i in range(rows):
#     for j in range(cols):
#         if r[i, j] == 255:  # 像素点为255表示的是白色，我们就是要将白色处的像素点，替换为红色
#             imageNew[i, j] = (0, 0, 255)  # 此处替换颜色，为BGR通道，不是RGB通道
# # 显示
# cv2.imshow('image', image)
# cv2.imshow('hsv', hsv)
# cv2.imshow('heibai', heibai)
# cv2.imshow('r', r)
# cv2.imshow('imageNew', imageNew)
# # 无限等待
# cv2.waitKey(0)
# # 销毁内存
# cv2.destroyAllWindows()