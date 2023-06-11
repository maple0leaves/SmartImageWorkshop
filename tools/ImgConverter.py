import cv2
import numpy as np
from PyQt5.QtGui import QImage, QPixmap


class ImgConverter:
    @staticmethod
    def opencv_to_qpixmap(opencv_image):
        # 获取OpenCV图像的尺寸和通道数
        height, width, channel = opencv_image.shape
        # 计算每行的字节数
        bytes_per_line = channel * width
        # 创建一个QImage对象，将OpenCV图像数据转换为适用于QPixmap的格式
        q_image = QImage(opencv_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        # 创建并返回QPixmap对象
        pixmap = QPixmap.fromImage(q_image)
        return pixmap

    @staticmethod
    def qpixmap_to_opencv(qpixmap_image):
        # 获取QPixmap图像的QImage对象
        qimage = qpixmap_image.toImage()
        # 获取图像的宽度和高度
        width = qimage.width()
        height = qimage.height()
        # 获取图像的字节缓冲区
        buffer = qimage.constBits()
        # 重塑缓冲区的形状，将其转换为NumPy数组
        buffer.reshape(qimage.height(), qimage.width(), 3)
        # 创建并返回OpenCV图像
        opencv_image = np.array(buffer).reshape(height, width, 3).copy()
        return opencv_image

    @staticmethod
    def qpixmap_to_cvimg(qpixmap):
        qimg = qpixmap.toImage()
        temp_shape = (qimg.height(), qimg.bytesPerLine() * 8 // qimg.depth())
        temp_shape += (4,)
        ptr = qimg.bits()
        ptr.setsize(qimg.byteCount())
        cvimg = np.array(ptr, dtype=np.uint8).reshape(temp_shape)
        cvimg = cvimg[..., :3]

        return cvimg

    @staticmethod
    def cvimg_to_qtimg(cvimg):
        height, width, depth = cvimg.shape
        cvimg = cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB)
        cvimg = QImage(cvimg.data, width, height, width * depth, QImage.Format_RGB888)

        return cvimg
    @staticmethod
    def graycvimg_to_qtimg(img_gray):
        height, width = img_gray.shape
        bytes_per_line = width
        q_image = QImage(img_gray.data, width, height, bytes_per_line, QImage.Format_Grayscale8)

        return q_image


