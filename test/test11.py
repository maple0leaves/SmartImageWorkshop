import numpy as np
import cv2 as cv

# 彩色图像进行自适应直方图均衡化，代码同上的地方不再添加注释
def hisEqulColor2(img):
    ycrcb = cv.cvtColor(img, cv.COLOR_BGR2YCR_CB)
    channels = cv.split(ycrcb)

    # 以下代码详细注释见官网：
    # https://docs.opencv.org/4.1.0/d5/daf/tutorial_py_histogram_equalization.html
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    clahe.apply(channels[0], channels[0])

    cv.merge(channels, ycrcb)
    cv.cvtColor(ycrcb, cv.COLOR_YCR_CB2BGR, img)
    return img

img = cv.imread('cat1.png')
img2 = img.copy()
res2 = hisEqulColor2(img2)

res = np.hstack((img, res2))
cv.imwrite('res1.jpg', res)