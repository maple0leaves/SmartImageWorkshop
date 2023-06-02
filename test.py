# _*_coding:utf-8_*_
# author:leo
# date:
# email:alplf123@163.com

from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QWidget, QVBoxLayout, QFrame, QGridLayout, QSizePolicy
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, \
    QGridLayout, QVBoxLayout, QHBoxLayout


'''
布局中嵌套布局是有效的，但是位置的问题还需要解决
widget ->gridlayout->widget->gridlayout
'''
class Example(QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self._initUI()
    def _initUI(self):
        #控件随窗口改变而改变
        # 可以通过继承 QMainWindow 来实现
        self.resize(400, 400)
        #建立顶层控件
        self.centeralwidget = QWidget(self)
        self.centergridLayout =  QGridLayout()
        self.centeralwidget.setLayout(self.centergridLayout)

        self.titlewidget  = QTextEdit()
        self.buttonwidget = QWidget()

        self.centergridLayout.addWidget(self.titlewidget,0,0,1,1)
        #要修改行列大小占比，一般使用setsetRowStretch,和setColumnStretch
        #在一定情况下也可以修改占据多少行
        self.centergridLayout.setRowStretch(0,1)
        self.centergridLayout.addWidget(self.buttonwidget,1,0,1,1)
        self.centergridLayout.setRowStretch(1,1)

        self.buttongrid = QGridLayout()
        self.buttonwidget.setLayout(self.buttongrid)
        self.button =  QPushButton("button")
        #让pushbutton在gridlayout中可以随布局变化而调整大小
        self.button.setSizePolicy (QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.button1 =  QPushButton("button1")
        self.button1.setSizePolicy (QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button2 =  QPushButton("button1")
        self.button2.setSizePolicy (QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.buttongrid.addWidget(self.button,0,0)
        self.buttongrid.addWidget(self.button1,1,0)
        self.buttongrid.addWidget(self.button2,2,0)


        #
        # self.vbox = QVBoxLayout(self.centeralwidget)
        # edit = QTextEdit()
        # self.vbox.addWidget(edit)
        #通过设置中心控件，将子控件填充布局
        #如果有多个控件最好在加一层widget这样最好布局，控制
        self.setCentralWidget(self.centeralwidget)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())