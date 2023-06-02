import cv2
import numpy as np

img = cv2.imread(r'001.png', 1)
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
            new_img[i, j] = (0, 0, 255)   # (0, 0, 255)替换为红底   (255, 255, 255)替换为白底

cv2.imshow('red_bg_img', new_img)
# 窗口等待命令  0表示无限等待
cv2.waitKey(0)
cv2.destroyAllWindows()
