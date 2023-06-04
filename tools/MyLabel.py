from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel
'''
@author 221 
由于QLabel没有clicked()信号，所以定义自己的Label，写信号函数
'''
class MyQLabel(QLabel):
    # 自定义信号, 注意信号必须为类属性 QtCore 核心
    button_clicked_signal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(MyQLabel, self).__init__(parent)

    def mouseReleaseEvent(self, QMouseEvent):
        self.button_clicked_signal.emit()

    # 可在外部与槽函数连接
    def connect_customized(self, func):
        self.button_clicked_signal.connect(func)

