import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(0) # 设置控件之间的间距为 0 像素
        grid.setContentsMargins(50, 50, 50, 50) # 设置控件之间的间距为 10 像素

        btn1 = QPushButton('Button 1')
        btn2 = QPushButton('Button 2')
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWidget()
    sys.exit(app.exec_())