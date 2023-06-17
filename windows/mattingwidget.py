import  sys
import cv2
import numpy as np
from PyQt5.QtGui import QCursor, QPixmap, QIcon, QImage, QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QFrame, QFileDialog, QSlider, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt

from tools.ImgAdapter import ImgAdapter
from tools.ImgConverter import ImgConverter
from tools.MyLabel import MyQLabel
from MODnet.start import run

'''maybe I set img size do not use label size but use Qwidget size ,Qwidget size is clearly'''


class mattingwidget(QWidget):
    '''
    this class use to process filter img
    '''
    def __init__(self):
        super().__init__()
        self.setWindowTitle("智能图像工坊")
        self.setWindowIcon(QIcon('./images/logo.png'))
        self.setStyleSheet('QWidget{background-color:white;}')
        #origin img
        self.pixmap=None
        #origin path
        self.filename =None
        #new img
        self.newimg = None

        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.screenheight = self.screenRect.height()
        self.screenwidth = self.screenRect.width()
        self.height = int(self.screenheight * 0.7)
        self.width = int(self.screenwidth * 0.7)
        #设置大小
        self.resize(self.width, self.height)
        #originlabel、newlabel在默认状态下的height、width
        self.oh =self.height*0.9
        self.ow = self.width*0.5
        # self.widget's layout
        self.gridlayout = QGridLayout()
        self.setLayout(self.gridlayout)
        #字体大小
        self.font = QFont()
        self.font.setPointSize(16)

        self.originlabel = MyQLabel('原图')
        self.originlabel.setFont(self.font)
        self.originlabel.setFrameShape(QFrame.Box)
        self.originlabel.setAlignment(Qt.AlignCenter)
        self.originlabel.setMinimumSize(int(self.width*0.5),int(self.height*0.9))
        self.originlabel.setMaximumSize(int(self.screenwidth*0.5),int(self.screenheight*0.9))

        self.newlabel = MyQLabel('新图片')
        self.newlabel.setFont(self.font)
        self.newlabel.setAlignment(Qt.AlignCenter)
        self.newlabel.setFrameShape(QFrame.Box)
        self.newlabel.setMinimumSize(int(self.width*0.5),int(self.height*0.9))
        self.newlabel.setMaximumSize(int(self.screenwidth*0.5),int(self.screenheight*0.9))
        # put 3 Label layout
        self.gridlayout2 =QGridLayout()
        self.uplabel = MyQLabel('上传图片')
        self.uplabel.setFont(self.font)
        self.uplabel.setStyleSheet('QLabel:hover{background-color:#e5f3ff}')
        self.uplabel.setMinimumSize(int(self.width*0.33),int(self.height*0.1))
        self.uplabel.setMaximumSize(int(self.screenwidth*0.33),int(self.screenheight*0.1))
        self.uplabel.setFrameShape(QFrame.Box)
        self.uplabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.uplabel.setAlignment(Qt.AlignCenter)


        self.label_red = MyQLabel('白色背景')
        self.label_red.setFont(self.font)
        self.label_red.setStyleSheet('QLabel:hover{background-color:#e5f3ff}')
        self.label_red.setFrameShape(QFrame.Box)
        self.label_red.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_red.setAlignment(Qt.AlignCenter)
        self.label_red.connect_customized(lambda :self.processimg(1))

        self.label_blue = MyQLabel('绿色背景')
        self.label_blue.setFont(self.font)
        self.label_blue.setStyleSheet('QLabel:hover{background-color:#e5f3ff}')
        self.label_blue.setFrameShape(QFrame.Box)
        self.label_blue.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_blue.setAlignment(Qt.AlignCenter)
        self.label_blue.connect_customized(lambda :self.processimg(2))

        self.label_white = MyQLabel('自定义背景')
        self.label_white.setFont(self.font)
        self.label_white.setStyleSheet('QLabel:hover{background-color:#e5f3ff}')
        self.label_white.setFrameShape(QFrame.Box)
        self.label_white.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_white.setAlignment(Qt.AlignCenter)
        self.label_white.connect_customized(lambda :self.processimg(3))


        self.sliderlayout = QGridLayout(self)
        # self.sliderlayout.setMinimumSize(int(self.width * 0.33), int(self.height * 0.1))
        # self.sliderlayout.setMaximumSize(int(self.screenwidth * 0.33), int(self.screenheight * 0.1))
        self.sliderlayout.addWidget(self.label_red,0,0,1,1)
        self.sliderlayout.addWidget(self.label_blue,0,1,1,1)
        self.sliderlayout.addWidget(self.label_white,0,2,1,1)
        #when slider valueChanged ,connect elf.update_labels


        self.downloadlabel = MyQLabel('保存图片')
        self.downloadlabel.setFont(self.font)
        self.downloadlabel.setStyleSheet('QLabel:hover{background-color:#e5f3ff}')
        self.downloadlabel.setMinimumSize(int(self.width * 0.33), int(self.height * 0.1))
        self.downloadlabel.setMaximumSize(int(self.screenwidth * 0.33), int(self.screenheight * 0.1))

        self.downloadlabel.setFrameShape(QFrame.Box)
        self.downloadlabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.downloadlabel.setAlignment(Qt.AlignCenter)

        self.setUI()

    def setUI(self):
        self.gridlayout.setRowStretch(0,7)
        self.gridlayout.setRowStretch(1,1)
        self.gridlayout.setColumnStretch(0,1)
        self.gridlayout.setColumnStretch(1,1)
        self.gridlayout.addWidget(self.originlabel,0,0,1,1)
        self.gridlayout.addWidget(self.newlabel,0,1,1,1)
        self.gridlayout.addLayout(self.gridlayout2,1,0,1,2)

        self.gridlayout2.addWidget(self.uplabel,0,0,1,1)
        self.gridlayout2.addLayout(self.sliderlayout, 0, 1, 1, 1)

        self.gridlayout2.addWidget(self.downloadlabel,0,2,1,1)

        self.uplabel.connect_customized(self.open_image)
        self.downloadlabel.connect_customized(self.save_image)

    def open_image(self):

        if self.isMaximized():
            oheight = self.screenheight * 0.9
            owidth = self.screenwidth * 0.49
        else:
            oheight = self.height*0.9
            owidth = self.width*0.5
        print("是否最大化",self.isMaximized())
        #if i write in setUI() or __init__(),I can not get true size
        #so I get size in this func, I can not think better way to solve now

        filename, _ = QFileDialog.getOpenFileName(None, "Open Image", ".", "Images (*.png *.jpg *.bmp)")
        if filename:
            self.filename = filename
            self.pixmap = QPixmap(filename)
            pixmap=ImgAdapter.adapteSize(self.pixmap,owidth,oheight)
            self.originlabel.setPixmap(pixmap)

    def save_image(self):
        if self.newimg is None:
            QMessageBox.information(self, '提示', '请先处理图片',
                                    QMessageBox.Yes )
        else:
            file_name, _ = QFileDialog.getSaveFileName(None, "Save Image", ".", "Images (*.png *.jpg *.bmp)")
            if file_name:
                self.newimg.save(file_name)

    '''changeEvent方法可以捕捉其他窗口状态的改变，例如窗口最大化，窗口还原
    窗口最小化、窗口关闭等'''
    def changeEvent(self, event):
        if event.type() == event.WindowStateChange:
            if self.isMinimized():
              pass
            elif self.isMaximized():
                if self.pixmap is not None:
                    oheight = self.originlabel.height()
                    owidth = self.originlabel.width()
                    pixmap = ImgAdapter.adapteSize(self.pixmap,owidth,oheight)
                    self.originlabel.setPixmap(pixmap)
                if self.newimg is not None:
                    oheight = self.newlabel.height()
                    owidth = self.newlabel.width()
                    pixmap = ImgAdapter.adapteSize(self.newimg, owidth, oheight)
                    self.newlabel.setPixmap(pixmap)
            else:
                if self.pixmap is not None:
                    oheight = self.oh
                    owidth = self.ow
                    pixmap = ImgAdapter.adapteSize(self.pixmap,owidth,oheight)
                    self.originlabel.setPixmap(pixmap)
                if self.newimg is not None:
                    oheight = self.oh
                    owidth = self.ow
                    pixmap = ImgAdapter.adapteSize(self.newimg,owidth,oheight)
                    self.newlabel.setPixmap(pixmap)
        event.accept()



    def processimg(self,index):
        if self.pixmap is None:
            QMessageBox.information(self, '提示', '请先上传图片',
                                    QMessageBox.Yes )
        else:
            if index==1:
                img = run(self.filename, './images/white.png')
                img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
                q_image = ImgConverter.cvimg_to_qtimg(img)
                self.newimg = QPixmap.fromImage(q_image)
                pixmap = ImgAdapter.adapteSize(self.newimg, self.newlabel.width(), self.newlabel.height())
                self.newlabel.setPixmap(pixmap)
            elif index==2:
                img = run(self.filename, './images/green.png')
                img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
                q_image = ImgConverter.cvimg_to_qtimg(img)
                self.newimg = QPixmap.fromImage(q_image)
                pixmap = ImgAdapter.adapteSize(self.newimg, self.newlabel.width(), self.newlabel.height())
                self.newlabel.setPixmap(pixmap)
            elif index==3:
                filename, _ = QFileDialog.getOpenFileName(None, "Open Image", ".", "Images (*.png *.jpg *.bmp)")
                if filename:
                    img = run(self.filename, filename)
                    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
                    q_image = ImgConverter.cvimg_to_qtimg(img)
                    self.newimg = QPixmap.fromImage(q_image)
                    pixmap = ImgAdapter.adapteSize(self.newimg, self.newlabel.width(), self.newlabel.height())
                    self.newlabel.setPixmap(pixmap)

    def changebackground(self,img, color):
        new_img = cv2.resize(img, None, fx=0.5, fy=0.5)
        rows, cols, channels = new_img.shape

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
                    new_img[i, j] = color  # (0, 0, 255)替换为红底   (255, 255, 255)替换为白底

        return new_img

if __name__=='__main__':
    app =QApplication(sys.argv)
    stw= mattingwidget()
    stw.show()
    sys.exit(app.exec_())