from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
import sys

class morewidget(QWidget):
    def __init__(self):
        super().__init__()
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.screenheight = self.screenRect.height()
        self.screenwidth = self.screenRect.width()
        self.height = int(self.screenheight * 0.5)
        self.width = int(self.screenwidth * 0.5)
        # 设置大小
        self.resize(self.width, self.height)
        self.setWindowTitle("智能图像工坊")
        self.setWindowIcon(QIcon('./images/logo.png'))
        self.setStyleSheet('QWidget{background-color:white;}')
        self.font = QFont()
        self.font.setPointSize(16)
        self.initUI()

    def initUI(self):
        # 创建 QLabel 组件
        label = QLabel(self)
        label.setFont(self.font)
        label.resize(self.width, self.height)
        label.setWordWrap(True)
        # 读取文本文件内容
        with open('./text.txt', 'r',encoding='UTF-8') as file:
            text = file.read()

        # 设置文本内容到 QLabel 中
        label.setText(text)
        # self.show()

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     example = morewidget()
#     sys.exit(app.exec_())
