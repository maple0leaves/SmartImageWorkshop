import  sys

from PyQt5.QtGui import QCursor, QIcon, QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QFrame
from PyQt5.QtCore import Qt
from tools.MyLabel import MyQLabel
from windows.filterwidget import filterwidget


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
        self.height = int(self.screenheight * 0.6)
        self.width = int(self.screenwidth * 0.2)
        # 设置大小
        self.resize(self.width, self.height)
        self.setWindowTitle("智能图像工坊")
        self.setWindowIcon(QIcon('./images/logo.png'))
        self.setStyleSheet('QWidget{background-color:white;}')
        self.font = QFont()
        self.font.setPointSize(16)
        #word set center ,mouse touch label be hand
        self.bwLabel.setAlignment(Qt.AlignCenter)
        self.bwLabel.setFont(self.font)
        self.bwLabel.setFrameShape(QFrame.Box)
        self.bwLabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.bwLabel.setStyleSheet('MyQLabel:hover{background-color:#e5f3ff;}')
        self.bwLabel.connect_customized(lambda:self.labelclick('黑白'))

        self.cclabel.setAlignment(Qt.AlignCenter)
        self.cclabel.setFont(self.font)
        self.cclabel.setFrameShape(QFrame.Box)
        self.cclabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.cclabel.setStyleSheet('MyQLabel:hover{background-color:#e5f3ff;}')
        self.cclabel.connect_customized(lambda:self.labelclick('反色'))


        self.delabel.setAlignment(Qt.AlignCenter)
        self.delabel.setFont(self.font)
        self.delabel.setFrameShape(QFrame.Box)
        self.delabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.delabel.setStyleSheet('MyQLabel:hover{background-color:#e5f3ff;}')
        self.delabel.connect_customized(lambda:self.labelclick('磨皮'))


        self.cllabel.setAlignment(Qt.AlignCenter)
        self.cllabel.setFont(self.font)
        self.cllabel.setFrameShape(QFrame.Box)
        self.cllabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.cllabel.setStyleSheet('MyQLabel:hover{background-color:#e5f3ff;}')
        self.cllabel.connect_customized(lambda:self.labelclick('亮度'))


        self.grid.addWidget(self.bwLabel,0,0)
        self.grid.addWidget(self.cclabel,1,0)
        self.grid.addWidget(self.delabel,2,0)
        self.grid.addWidget(self.cllabel,3,0)

        self.setLayout(self.grid)
    def labelclick(self,name):
        self.sw = filterwidget(name)
        self.sw.show()

# if __name__ =='__main__':
#     app = QApplication(sys.argv)
#     fw = filterwindow()
#     fw.show()
#     sys.exit(app.exec_())