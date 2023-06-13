import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap, QPainter, QPen, QImage, QColor, QPainterPath
from PyQt5.QtCore import Qt, QRect


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.label = QLabel(self)
        self.layout.addWidget(self.label)

        self.button = QPushButton("Apply Mosaic", self)
        self.button.clicked.connect(self.applyMosaic)
        self.layout.addWidget(self.button)

        self.image = QPixmap("img_2.png")
        self.label.setPixmap(self.image)
        self.label.setFixedSize(self.image.size())

        self.origin = None
        self.current_rect = QRect()
        self.drawing = False

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.image)

        painter.setPen(QPen(Qt.red, 2, Qt.SolidLine))
        if self.drawing:
            painter.drawRect(self.current_rect)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.origin = event.pos()
            self.current_rect.setTopLeft(self.origin)
            self.current_rect.setBottomRight(self.origin)
            self.drawing = True

    def mouseMoveEvent(self, event):
        if self.drawing:
            self.current_rect.setBottomRight(event.pos())
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False
            self.update()

    def applyMosaic(self):
        if self.current_rect.isValid():
            x = self.current_rect.x()
            y = self.current_rect.y()
            width = self.current_rect.width()
            height = self.current_rect.height()

            mosaic_image = self.image.toImage()
            mosaic_image = self.applyMosaicEffect(mosaic_image, x, y, width, height)

            self.image = QPixmap.fromImage(mosaic_image)
            self.label.setPixmap(self.image)

    def applyMosaicEffect(self, image, x, y, width, height):
        mosaic_image = image.copy(x, y, width, height)

        for i in range(x, x + width):
            for j in range(y, y + height):
                mosaic_color = image.pixelColor(i, j)
                for x in range(i, i + 10):
                    for y in range(j, j + 10):
                        mosaic_image.setPixelColor(x, y, mosaic_color)

        return mosaic_image


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
