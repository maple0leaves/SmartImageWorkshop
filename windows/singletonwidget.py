import  sys

from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import  QWidget ,QGridLayout,QApplication
from PyQt5.QtCore import Qt
from tools.MyLabel import MyQLabel

class singletonwidget(QWidget):
    def __init__(self):
        super().__init__()
        # self.widget's layout
        self.gridlayout = QGridLayout()
        self.setLayout(self.gridlayout)
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

        self.setUI()
    def setUI(self):
        self.gridlayout.addWidget(self.originlabel,0,0,1,1)
        self.gridlayout.addWidget(self.newlabel,0,1,1,1)
        self.gridlayout.addLayout(self.gridlayout2,1,0,1,2)

        self.gridlayout2.addWidget(self.uplabel,0,0,1,1)
        self.gridlayout2.addWidget(self.processlabel,0,1,1,1)
        self.gridlayout2.addWidget(self.downloadlabel,0,2,1,1)


if __name__=='__main__':
    app =QApplication(sys.argv)
    stw= singletonwidget()
    stw.show()
    sys.exit(app.exec_())