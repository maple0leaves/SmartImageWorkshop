from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QMovie
import sys

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        label = QLabel(self)
        layout.addWidget(label)

        # 创建 QMovie 对象并加载 GIF 图片
        movie = QMovie('../1.gif')
        label.setMovie(movie)

        # 设置 QMovie 循环播放
        movie.setCacheMode(QMovie.CacheAll)
        movie.setSpeed(100)
        movie.start()

        self.setLayout(layout)

        # self.setGeometry(100, 100, 300, 300)
        self.setWindowTitle('GIF Animation')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    example = Example()
    sys.exit(app.exec_())
