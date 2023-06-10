import  sys

from PyQt5.QtGui import QCursor, QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QFrame, QFileDialog, QSlider, QVBoxLayout
from PyQt5.QtCore import Qt
from tools.MyLabel import MyQLabel

'''have a small ui bug not fix ,in  short time I have no idea to solve it 
specifically when click maxsize for window then return ,img size can not full label
 it not a main bug ,just small ,and I see it uncomfortable.
'''
'''maybe I set img size do not use label size but use Qwidget size ,Qwidget size is clearly'''
def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper

@singleton
class singletonwidget(QWidget):
    '''
    this class use to process filter img
    '''
    def __init__(self,name='亮度'):
        super().__init__()
        self.setWindowTitle("智能图象处理")
        self.setWindowIcon(QIcon('../images/logo.png'))
        self.setStyleSheet('QWidget{background-color:white;}')
        self.labelname = name
        self.pixmap=None
        #暂存originlabel、newlabel的height、width
        self.oh = None
        self.ow = None
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.screenheight = self.screenRect.height()
        self.screenwidth = self.screenRect.width()
        self.height = int(self.screenheight * 0.7)
        self.width = int(self.screenwidth * 0.7)
        #设置大小
        self.resize(self.width, self.height)
        # self.widget's layout
        self.gridlayout = QGridLayout()
        self.setLayout(self.gridlayout)
        # put 3 Label layout
        self.gridlayout2 =QGridLayout()

        self.originlabel = MyQLabel('原图')
        self.originlabel.setFrameShape(QFrame.Box)
        self.originlabel.setAlignment(Qt.AlignCenter)

        self.newlabel = MyQLabel('新图片')
        self.newlabel.setAlignment(Qt.AlignCenter)
        self.newlabel.setFrameShape(QFrame.Box)

        self.uplabel = MyQLabel('上传图片')
        self.uplabel.setStyleSheet('QLabel:hover{background-color:#e5f3ff}')
        self.uplabel.setMinimumSize(int(self.width*0.33),int(self.height*0.1))
        self.uplabel.setMaximumSize(int(self.screenwidth*0.33),int(self.screenheight*0.1))
        self.uplabel.setFrameShape(QFrame.Box)
        self.uplabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.uplabel.setAlignment(Qt.AlignCenter)

        if self.labelname=='亮度':
            self.label_min = MyQLabel('-50')
            self.label_max = MyQLabel('50')
            self.label_max.setAlignment(Qt.AlignRight)
            ##########
            self.slider = QSlider(Qt.Horizontal)
            self.slider.setMinimumSize(int(self.width * 0.33), int(self.height * 0.1))
            self.slider.setMaximumSize(int(self.screenwidth * 0.33), int(self.screenheight * 0.1))
            self.slider.setOrientation(Qt.Horizontal)
            self.slider.setTickPosition(QSlider.TicksBothSides)
            self.slider.setTickInterval(10)
            self.slider.setRange(-50, 50)

            self.sliderlayout = QGridLayout(self)
            self.sliderlayout.addWidget(self.slider,0,0,1,2)
            self.sliderlayout.addWidget(self.label_min,1,0,1,1)
            self.sliderlayout.addWidget(self.label_max,1,1,1,1)
            #when slider valueChanged ,connect elf.update_labels
            self.slider.valueChanged.connect(self.update_labels)
        else:
            self.processlabel = MyQLabel(self.labelname+'处理')
            self.processlabel.setStyleSheet('QLabel:hover{background-color:#e5f3ff}')
            self.processlabel.setFrameShape(QFrame.Box)
            self.processlabel.setCursor(QCursor(Qt.PointingHandCursor))
            self.processlabel.setAlignment(Qt.AlignCenter)

        self.downloadlabel = MyQLabel('保存图片')
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
        self.gridlayout.addWidget(self.originlabel,0,0,1,1)
        self.gridlayout.addWidget(self.newlabel,0,1,1,1)
        self.gridlayout.addLayout(self.gridlayout2,1,0,1,2)

        self.gridlayout2.addWidget(self.uplabel,0,0,1,1)
        if self.labelname=='亮度':
            self.gridlayout2.addLayout(self.sliderlayout, 0, 1, 1, 1)
        else:
            self.gridlayout2.addWidget(self.processlabel,0,1,1,1)
        self.gridlayout2.addWidget(self.downloadlabel,0,2,1,1)

        self.uplabel.connect_customized(self.open_image)
        self.downloadlabel.connect_customized(self.save_image)

    def open_image(self):
        oheight = self.originlabel.height()
        owidth = self.originlabel.width()
        #if i write in setUI() or __init__(),I can not get true size
        #so I get size in this func, I can not think better way to solve now
        self.oh =oheight
        self.ow = owidth
        filename, _ = QFileDialog.getOpenFileName(None, "Open Image", ".", "Images (*.png *.jpg *.bmp)")
        if filename:
            self.pixmap = QPixmap(filename)
            pixmap = self.pixmap
            if oheight>=owidth:
                pixmap = pixmap.scaledToWidth(owidth)
                if pixmap.height()>= oheight:
                   pixmap = pixmap.scaledToHeight(oheight)
            else:
                pixmap = pixmap.scaledToHeight(oheight)
                if pixmap.width()>=owidth:
                    pixmap =pixmap.scaledToWidth(owidth)
            self.originlabel.setPixmap(pixmap)

    def save_image(self):
        file_name, _ = QFileDialog.getSaveFileName(None, "Save Image", ".", "Images (*.png *.jpg *.bmp)")
        if file_name:
            # pixmap = QPixmap('image.jpg')  # 假设要保存的图片名为 image.jpg
            self.pixmap.save(file_name)

    '''changeEvent方法可以捕捉其他窗口状态的改变，例如窗口最大化，窗口还原
    窗口最小化、窗口关闭等'''
    def changeEvent(self, event):
        if event.type() == event.WindowStateChange:
            pixmap = self.pixmap
            if self.isMinimized():
              pass
            elif self.isMaximized(): #因为这里包含两种情况，最大化和还原，所以放在else中
                if pixmap is not None:
                    oheight = self.originlabel.height()
                    owidth = self.originlabel.width()
                    if oheight >= owidth:
                        pixmap = pixmap.scaledToWidth(owidth)
                        if pixmap.height() >= oheight:
                            pixmap = pixmap.scaledToHeight(oheight)
                    else:
                        pixmap = pixmap.scaledToHeight(oheight)
                        if pixmap.width() >= owidth:
                            pixmap = pixmap.scaledToWidth(owidth)
                    self.originlabel.setPixmap(pixmap)
            else:
                if pixmap is not None:
                    oheight = self.oh
                    owidth = self.ow
                    if oheight >= owidth:
                        pixmap = pixmap.scaledToWidth(owidth)
                        if pixmap.height() >= oheight:
                           pixmap = pixmap.scaledToHeight(oheight)
                    else:
                        pixmap = pixmap.scaledToHeight(oheight)
                        if pixmap.width() >= owidth:
                            pixmap = pixmap.scaledToWidth(owidth)
                    self.originlabel.setPixmap(pixmap)
        event.accept()
    def update_labels(self):
        print('____________')
        self.label_min.setText(str(self.slider.minimum()))
        self.label_max.setText(str(self.slider.maximum()))

if __name__=='__main__':
    app =QApplication(sys.argv)
    stw= singletonwidget()
    stw.show()
    sys.exit(app.exec_())