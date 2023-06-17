from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QMovie, QPainter, QPaintEvent
import sys

class AnimatedWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.movie = QMovie('../testimgs/1.gif')
        self.movie.frameChanged.connect(self.update)  # 连接帧变化信号到 update 方法
        self.movie.start()

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        current_frame = self.movie.currentPixmap()
        painter.drawPixmap(0, 0, current_frame)

    def resizeEvent(self, event):
        self.movie.setScaledSize(self.size())  # 调整 QMovie 的大小与 QWidget 相同

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = AnimatedWidget()
    widget.setWindowTitle('Animated Widget')
    widget.setGeometry(100, 100, 300, 200)
    widget.show()
    sys.exit(app.exec_())
