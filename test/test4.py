from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QSlider
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setGeometry(50, 50, 200, 30)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setTickInterval(5)  # 设置滑块的刻度间隔为5
        self.slider.setSingleStep(1)  # 设置滑块在键盘或鼠标滚轮操作时的步长

        self.label = QLabel(self)
        self.label.setGeometry(50, 100, 200, 30)

        self.slider.valueChanged.connect(self.slider_value_changed)

    def slider_value_changed(self, value):
        self.label.setText(f"Slider value: {value}")

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
