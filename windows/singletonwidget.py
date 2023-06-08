import  sys

from PyQt5.QtGui import QCursor, QIcon
from PyQt5.QtWidgets import  QWidget ,QGridLayout,QApplication
from PyQt5.QtCore import Qt
from tools.MyLabel import MyQLabel

class singletonwidget(QWidget):
    def __init__(self):
        super().__init__()
        self.widget = QWidget()
        # self.widget's layout
        self.gridlayout = QGridLayout()
        # put 3 Label layout
        self.gridlayout2 =QGridLayout()
        self.originlabel = MyQLabel('原图')
        self.newlabel = MyQLabel('新图片')
        self.uplabel = MyQLabel('上传图片')
        self.uplabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.uplabel.setAlignment(Qt.AlignCenter)
        self.processlabel = MyQLabel('开始处理')
        self.processlabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.processlabel.setAlignment(Qt.AlignCenter)
        self.downloadlabel = MyQLabel('保存图片')
        self.downloadlabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.downloadlabel.setAlignment(Qt.AlignCenter)
    def setUI(self):
