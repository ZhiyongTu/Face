import sys
import os
import json
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QLineEdit
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import QTimer
from main_ui import *
from login_ui import *
from help import *
import Face_recognition


# 登录界面
class Login(QMainWindow, Ui_login):
    switch_main = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        # 设置界面
        super(Login, self).__init__(parent)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.setupUi(self)

        pic = QtGui.QPixmap('./img/login.png')
        self.logoo.setPixmap(pic)

        # 按键设置
        self.close_3.clicked.connect(self.ButtonCloseSlot)  # 关闭界面
        self.min_.clicked.connect(self.ButtonMinSlot)  # 最小化界面

        self.enter.clicked.connect(self.enter_d)  # 登录
        self.exit.clicked.connect(self.exit_d)  # 退出
        self.face.clicked.connect(self.face_d)  # 人脸登录

        # 输入设置
        self.account.setPlaceholderText("账号")  # 账号输入框
        self.word.setEchoMode(QLineEdit.Password)  # 密码输入框
        self.word.setPlaceholderText("密码")  # 密码输入框

        # 初始化参数
        self.num = 0

    # 最小化界面
    def ButtonMinSlot(self):
        self.showMinimized()

    # 关闭界面
    def ButtonCloseSlot(self):
        self.close()

    # 登录
    def enter_d(self):
        def load_file(file_path):
            pat = []
            with open(file_path, "r+") as f:
                for i in f.readlines():
                    pat.append(i.replace("\n", ''))
            return pat

        user = load_file("./login_info/账号.txt")
        password = load_file("./login_info/密码.txt")
        self.id_password = dict(zip(user, password))

        if self.account.text() not in self.id_password.keys():
            self.prompt.setText("账号或密码输入错误")
        else:
            if self.id_password[self.account.text()] == self.word.text():
                # 账号密码验证成功，进入主界面，并关闭登录窗口
                self.timer = QTimer()
                self.timer.start()
                self.timer.setInterval(100)
                self.timer.timeout.connect(self.show_action)
            else:
                self.prompt.setText("账号或密码输入错误")

    # 退出
    def exit_d(self):
        self.timer = QTimer()
        self.timer.start()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.show_close)

    # 人脸登录
    def face_d(self):
        get_name = Face_recognition.main()  # 返回识别的人名
        if get_name == "unknown":
            self.prompt.setText("人脸识别登录失败")
            reply = QMessageBox.information(self, '提示', '人脸识别失败', QMessageBox.Close)
        else:
            reply = QMessageBox.information(self, '提示', "欢迎您：" + get_name, QMessageBox.Ok)
            # 人脸验证成功，进入主界面，并关闭登录窗口
            self.timer = QTimer()
            self.timer.start()
            self.timer.setInterval(100)
            self.timer.timeout.connect(self.show_action)

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

    # 成功登录提示
    def show_action(self):
        if self.num == 36:
            self.switch_main.emit()
            self.close()
        elif self.num == 0:
            self.prompt.setText("登录成功,加载中·")
        elif self.num == 12:
            self.prompt.setText("登录成功,加载中··")
        elif self.num == 24:
            self.prompt.setText("登录成功,加载中···")
        self.num = self.num + 1

    # 退出提示
    def show_close(self):
        if self.num == 36:
            self.close()
        elif self.num == 0:
            self.prompt.setText(str(3 - (self.num // 12)) + "s后退出·")
        elif self.num == 12:
            self.prompt.setText(str(3 - (self.num // 12)) + "s后退出··")
        elif self.num == 24:
            self.prompt.setText(str(3 - (self.num // 12)) + "s后退出···")
        self.num = self.num + 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = Login()
    myWin.show()
    sys.exit(app.exec_())
