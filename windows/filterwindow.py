import  sys

from PyQt5.QtGui import QCursor, QIcon
from PyQt5.QtWidgets import  QWidget ,QGridLayout,QApplication
from PyQt5.QtCore import Qt
from tools.MyLabel import MyQLabel


class filterwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.grid = QGridLayout()
        #blackwhitelabel
        self.bwLabel = MyQLabel('黑白')
        #contrarycolorlabel
        self.cclabel = MyQLabel('反色')
        #dermabrasionlabel
        self.delabel = MyQLabel('磨皮')
        #changelightlabel
        self.cllabel = MyQLabel('亮度变化')

        self.initUI()


    def initUI(self):
        #获取显示器分辨率 depend on indicator size set window size
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.screenheight = self.screenRect.height()
        self.screenwidth = self.screenRect.width()
        self.height = int(self.screenheight * 0.7)
        self.width = int(self.screenwidth * 0.7)
        # 设置大小
        self.resize(self.width, self.height)
        self.setWindowTitle("智能图象处理")
        self.setWindowIcon(QIcon('../images/logo.png'))
        self.setStyleSheet('QWidget{background-color:white;}')

        #word set center ,mouse touch label be hand
        self.bwLabel.setAlignment(Qt.AlignCenter)
        self.bwLabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.bwLabel.setStyleSheet('MyQLabel{background-color:#f0f0f0;}')
        self.cclabel.setAlignment(Qt.AlignCenter)
        self.cclabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.delabel.setAlignment(Qt.AlignCenter)
        self.delabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.cllabel.setAlignment(Qt.AlignCenter)
        self.cllabel.setCursor(QCursor(Qt.PointingHandCursor))

        self.grid.setColumnStretch(0,1)
        self.grid.setColumnStretch(1,3)
        self.grid.setColumnStretch(2,3)
        self.grid.setColumnStretch(3,3)
        self.grid.addWidget(self.bwLabel,0,0)
        self.grid.addWidget(self.cclabel,1,0)
        self.grid.addWidget(self.delabel,2,0)
        self.grid.addWidget(self.cllabel,3,0)
        self.bwwidget()
        # label = MyQLabel("saojioa")
        # label2 = MyQLabel("saojioa")
        # label.setAlignment(Qt.AlignCenter)
        #
        # self.grid.addWidget(label,4,1)
        # self.grid.addWidget(label2,5,1)

        self.setLayout(self.grid)

    def bwwidget(self):
        self.wid = QWidget()
        self.grid.addWidget(self.wid,0,1,6,3)
        self.widgridlayout = QGridLayout()



if __name__ =='__main__':
    app = QApplication(sys.argv)
    fw = filterwindow()
    fw.show()
    sys.exit(app.exec_())