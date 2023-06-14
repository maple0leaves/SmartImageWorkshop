import  sys
import cv2
from PyQt5.QtGui import QCursor, QPixmap, QIcon, QImage, QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QFrame, QFileDialog, QSlider, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt

from tools.ImgAdapter import ImgAdapter
from tools.ImgConverter import ImgConverter
from tools.MyLabel import MyQLabel


'''maybe I set img size do not use label size but use Qwidget size ,Qwidget size is clearly'''


class adaptwidget(QWidget):
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
        #origin img path
        self.name=None
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


        self.processlabel = MyQLabel('开始处理')
        self.processlabel.setFont(self.font)
        self.processlabel.setStyleSheet('QLabel:hover{background-color:#e5f3ff}')
        self.processlabel.setFrameShape(QFrame.Box)
        self.processlabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.processlabel.setAlignment(Qt.AlignCenter)
        #when click processlabel run self.processimg to process img
        self.processlabel.connect_customized(self.processimg)

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

        self.gridlayout2.addWidget(self.processlabel,0,1,1,1)
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
            self.name = filename
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


    def processimg(self):
        if self.pixmap is None:
            QMessageBox.information(self, '提示', '请先上传图片',
                                    QMessageBox.Yes )
        else:
            img = cv2.imread(self.name)
            img = self.hisEqulColor2(img)
            q_image = ImgConverter.cvimg_to_qtimg(img)
            self.newimg = QPixmap.fromImage(q_image)
            pixmap = ImgAdapter.adapteSize(self.newimg,self.newlabel.width(),self.newlabel.height())
            self.newlabel.setPixmap(pixmap)

    def hisEqulColor2(self,img):
        ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
        channels = cv2.split(ycrcb)

        # 以下代码详细注释见官网：
        # https://docs.opencv.org/4.1.0/d5/daf/tutorial_py_histogram_equalization.html
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        clahe.apply(channels[0], channels[0])

        cv2.merge(channels, ycrcb)
        cv2.cvtColor(ycrcb, cv2.COLOR_YCR_CB2BGR,img)
        return img


if __name__=='__main__':
    app =QApplication(sys.argv)
    stw= adaptwidget()
    stw.show()
    sys.exit(app.exec_())