import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from tools.MyLabel import MyQLabel
from tools.common_helper import CommonHelper


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(0) # 设置控件之间的间距为 0 像素
        grid.setContentsMargins(50, 50, 50, 50) # 设置控件之间的间距为 10 像素

        self.stylefile = '../style.qss'
        self.qssstyle = CommonHelper.readQSS(self.stylefile)
        #要使用QSS中ID选择器需要setObjectName(),这个ObjectName不是对象名
        btn1 = MyQLabel('点击事件')
        #ID选择器通过ObjectName来实现的，再说一次，这个ObjectName是要自己设置的
        #不是对象名不是对象名！！！！！不是对象名！！！！
        btn1.setObjectName("btn1")
        btn1.setStyleSheet(self.qssstyle)
        btn1.connect_customized(self.fun)

        btn2 = QPushButton('Button 2')
        btn2.setStyleSheet(self.qssstyle)
        btn3 = QPushButton('Button 3')
        btn4 = QPushButton('Button 4')
        btn5 = QPushButton('Button 5')

        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(btn3, 1, 0)
        grid.addWidget(btn4, 1, 1)
        grid.addWidget(btn5, 2, 0, 1, 2)

        self.setLayout(grid)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('QGridLayout')
        self.show()
    def fun(self):
        print("__________")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    sys.exit(app.exec_())