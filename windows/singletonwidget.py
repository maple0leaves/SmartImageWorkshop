import  sys

from PyQt5.QtGui import QCursor, QIcon
from PyQt5.QtWidgets import  QWidget ,QGridLayout,QApplication
from PyQt5.QtCore import Qt
from tools.MyLabel import MyQLabel

class singletonwidget(QWidget):
    def __init__(self):
        super().__init__()
