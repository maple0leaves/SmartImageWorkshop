import  sys

from PyQt5.QtGui import QCursor, QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QFrame, QFileDialog
from PyQt5.QtCore import Qt
from tools.MyLabel import MyQLabel

class singletonwidget(QWidget):
    def __init__(self):
        super().__init__()
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.screenheight = self.screenRect.height()
        self.screenwidth = self.screenRect.width()
        self.height = int(self.screenheight * 0.7)
        self.width = int(self.screenwidth * 0.7)
        #设置大小
        self.resize(self.width, self.height)
        # self.widget's layout
        self.gridlayout = QGridLayout()
        self.setLayout(self.gridlayout)
        # put 3 Label layout
        self.gridlayout2 =QGridLayout()

        self.originlabel = MyQLabel('原图')
        self.originlabel.setFrameShape(QFrame.Box)
        self.originlabel.setAlignment(Qt.AlignCenter)

        self.newlabel = MyQLabel('新图片')
        self.newlabel.setAlignment(Qt.AlignCenter)
        self.newlabel.setFrameShape(QFrame.Box)

        self.uplabel = MyQLabel('上传图片')
        self.uplabel.setFrameShape(QFrame.Box)
        self.uplabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.uplabel.setAlignment(Qt.AlignCenter)

        self.processlabel = MyQLabel('开始处理')
        self.processlabel.setFrameShape(QFrame.Box)
        self.processlabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.processlabel.setAlignment(Qt.AlignCenter)

        self.downloadlabel = MyQLabel('保存图片')
        self.downloadlabel.setFrameShape(QFrame.Box)
        self.downloadlabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.downloadlabel.setAlignment(Qt.AlignCenter)

        self.setUI()
    def setUI(self):
        self.gridlayout.setRowStretch(0,7)
        self.gridlayout.setRowStretch(1,1)
        self.gridlayout.addWidget(self.originlabel,0,0,1,1)
        self.gridlayout.addWidget(self.newlabel,0,1,1,1)
        self.gridlayout.addLayout(self.gridlayout2,1,0,1,2)

        self.gridlayout2.addWidget(self.uplabel,0,0,1,1)
        self.gridlayout2.addWidget(self.processlabel,0,1,1,1)
        self.gridlayout2.addWidget(self.downloadlabel,0,2,1,1)

        self.uplabel.connect_customized(self.open_image)
        self.downloadlabel.connect_customized(self.save_image)

    def open_image(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Image", ".", "Images (*.png *.jpg *.bmp)")
        if filename:
            self.pixmap = QPixmap(filename)
            self.originlabel.setPixmap(self.pixmap)
    def save_image(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Image", ".", "Images (*.png *.jpg *.bmp)")
        if file_name:
            # pixmap = QPixmap('image.jpg')  # 假设要保存的图片名为 image.jpg
            self.pixmap.save(file_name)
if __name__=='__main__':
    app =QApplication(sys.argv)
    stw= singletonwidget()
    stw.show()
    sys.exit(app.exec_())