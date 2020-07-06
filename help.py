import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMainWindow
from help_ui import *


class help_hh(QMainWindow, Ui_help_hh):
    def __init__(self, parent=None):
        # 设置界面
        super(help_hh, self).__init__(parent)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.setupUi(self)
        bg = QtGui.QPixmap('./img/main.png')
        self.bgcolor.setPixmap(bg)
        self.m_flag = None
        self.m_Position = None

        self.close_3.clicked.connect(self.ButtonCloseSlot)  # 关闭界面
        self.min_.clicked.connect(self.ButtonMinSlot)  # 最小化界面

    # 最小化界面
    def ButtonMinSlot(self):
        self.showMinimized()

    # 关闭界面
    def ButtonCloseSlot(self):
        self.close()

    # 鼠标移动控制
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

   
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    hh = help_hh()
    hh.show()
    sys.exit(app.exec_())