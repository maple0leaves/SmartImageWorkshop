import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from mainwindows import Ui_MainWindow



if __name__ == "__main__":
    App = QApplication(sys.argv)    # 创建QApplication对象，作为GUI主程序入口
    aw = Ui_MainWindow()    # 创建主窗体对象，实例化Ui_MainWindow
    w = QMainWindow()      # 实例化QMainWindow类
                            #传入MainWindow 然后对这个Maindow进行设置
    aw.setupUi(w)         # 主窗体对象调用setupUi方法，对QMainWindow对象进行设置
    w.show()               # 显示主窗体
    # App.exit()
    sys.exit(App.exec_())   # 循环中等待退出程序