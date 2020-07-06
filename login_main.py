import sys
import os
import json
import cv2
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QLineEdit
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import QTimer
from main_ui import *
from login_ui import *
from help import *
import Face_train
import Face_recognition


# 登录界面
class Login(QMainWindow, Ui_login):
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
            self.hide()  # 隐藏窗口
            self.shop = MyWindow()
            self.shop.show()  # 打开主窗口
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


# 主界面
class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.init_ui()

    def init_ui(self):
        # 设置主界面UI
        self.setupUi(self)
        # self.setWindowOpacity(0.9)  # 设置窗口透明度
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        bg = QtGui.QPixmap('./img/main.png')
        self.bgcolor.setPixmap(bg)
        self.bgcolor.setStyleSheet("background-color:#000000;")

        # 设置显示窗口
        self.label_2.setStyleSheet("border:1px solid black;")  # 显示人脸照片
        self.label.setStyleSheet("border:1px solid white;")  # 采集/识别人脸主窗口

        # 设置按键响应
        self.close_3.clicked.connect(self.ButtonCloseSlot)  # 关闭界面
        self.min_.clicked.connect(self.ButtonMinSlot)  # 最小化界面
        self.openfile.clicked.connect(self.open_file)  # 打开人脸采集名单
        self.dete.clicked.connect(self.create_file)  # 确定人脸信息，创建对应人脸文件夹
        self.open.clicked.connect(self.open_cap)  # 开始采集人脸
        self.close_.clicked.connect(self.close_cap)  # 结束采集人脸
        self.train.clicked.connect(self.train_d)  # 模型训练
        self.re.clicked.connect(self.recognition)  # 开始人脸识别
        self.close_2.clicked.connect(self.close_re)  # 结束人脸识别
        self.logout.clicked.connect(self.logout_d)  # 注销登录
        self.help.clicked.connect(self.help_d)  # 帮助中心

        # 参数初始化
        self.count = 0  # 初始化采集/识别限制数量
        self.index = 0  # 初始化索引
        self.num = 1  # 初始化采集人脸数量

    # 最小化界面
    def ButtonMinSlot(self):
        self.showMinimized()

    # 关闭界面
    def ButtonCloseSlot(self):
        self.close()

    # 打开人脸采集名单
    def open_file(self):
        self.absolute_path = QFileDialog.getExistingDirectory(self, "选取文件夹", "/")

        image_path = self.absolute_path + '/image/'
        for root, dirs, files in os.walk(image_path):
            for photo_file in files:
                photo_path = image_path + photo_file
                image = cv2.imread(photo_path)
                image = cv2.resize(image, (100, 120))
                cv2.imwrite(photo_path, image)
        info = self.absolute_path + '/information.xls'
        self.class_info = pd.read_excel(info, header=None, names=['name', 'id'])
        self.class_dict = dict(zip(self.class_info.id.astype('str'), self.class_info.name))
        self.text.setText(self.class_info.name[self.index])
        photo = QtGui.QPixmap(self.absolute_path + '/image/' + str(self.class_info.id[self.index]) + '.jpg')
        self.label_2.setPixmap(photo)

    # 确定人脸信息，创建对应人脸文件夹
    def create_file(self):
        self.root_file = os.path.split(os.path.realpath(__file__))[0] + \
                         "\\data" + '\\' + str(self.class_info.id[self.index]) + '\\'
        if os.path.exists(self.root_file):
            os.remove(self.root_file)
        os.makedirs(self.root_file)
        self.index = self.index + 1

    # 开始采集人脸
    def open_cap(self):
        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.timer.start()
        self.timer.setInterval(100)
        self.countdown.setText("开始采集")
        self.timer.timeout.connect(self.show_image)

    def show_image(self):
        # 使用OpenCV人脸识别分类器
        classfier = cv2.CascadeClassifier("need/haarcascade_frontalface_default.xml")
        # 人脸检测边框的颜色，RGB格式
        color = (255, 255, 255)
        while self.cap.isOpened():
            flag, self.image = self.cap.read()  # 读取一帧数据
            if not flag:
                break
            grey = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)  # 将当前桢图像转换成灰度图像
            # 人脸检测
            faceRects = classfier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))

            if self.num > 59:
                if self.num % 6 == 0 and self.count != 200:
                    image_num = self.num // 6 - 9
                    file_path = self.root_file + '{:03}.jpg'.format(image_num)
                    if len(faceRects) > 0:  # 大于0则检测到人脸
                        for faceRect in faceRects:  # 单独框出每一张人脸
                            x, y, w, h = faceRect

                            # 将当前帧保存为图片
                            image = self.image[y - 10: y + h + 10, x - 10: x + w + 10]
                            cv2.imwrite(file_path, image)

                            # 画出矩形框
                            cv2.rectangle(self.image, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 1)

                            # 显示当前捕捉人脸图片数目
                            # font = cv2.FONT_HERSHEY_SIMPLEX
                            # cv2.putText(self.image, 'num:%d' % (image_num), (x + 30, y + 30), font, 1, color, 1)
                            self.countdown.setText('已采集人脸图像数量:%d' % image_num)

                    self.count = self.count + 1
            else:
                self.countdown.setText(str(5 - (self.num // 12)))
            self.num = self.num + 1

            # 显示图像
            show = cv2.resize(self.image, (940, 835))
            show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
            showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap.fromImage(showImage))

            c = cv2.waitKey(10)
            if c & 0xFF == ord('q'):
                break

    # 结束采集人脸
    def close_cap(self):
        self.num = 1
        self.timer.stop()
        self.cap.release()
        self.label.clear()
        self.label.setText("人脸采集及识别区域")
        self.countdown.setText("采集/识别等待中")
        self.text.setText("")
        self.text.setText(self.class_info.name[self.index])
        photo = QtGui.QPixmap(self.absolute_path + '/image/' + str(self.class_info.id[self.index]) + '.jpg')
        self.label_2.setPixmap(photo)
        # 释放摄像头并销毁所有窗口
        self.cap.release()

    # 模型训练
    def train_d(self):
        self.countdown.setText("模型训练中")
        QMessageBox.information(self, '提示', '正在训练数据', QMessageBox.Ok)
        Face_train.main()
        QMessageBox.information(self, '提示', '训练完毕', QMessageBox.Ok)
        self.countdown.setText("模型训练完毕")

    # 开始人脸识别
    def recognition(self):
        # 读取人脸身份信息
        with open('./need/contrast_table', 'r') as f:
            self.contrast_table = json.loads(f.read())
        self.model = Face_train.Model()
        self.model.load_model(file_path='./model/model')

        self.countdown.setText("开始识别")
        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.timer.start()
        self.timer.setInterval(10)
        self.timer.timeout.connect(self.re_image)

    def re_image(self):
        while self.cap.isOpened():
            flag, self.image = self.cap.read()  # 读取一帧数据

            if flag is True:
                # 将当前桢图像转换成灰度图像
                grey = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            else:
                break

            # 使用人脸识别分类器
            classifier = cv2.CascadeClassifier("need/haarcascade_frontalface_default.xml")
            # 人脸检测边框的颜色，RGB格式
            color = (255, 255, 255)

            # 人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
            faceRects = classifier.detectMultiScale(grey, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
            if self.num > 59:
                if self.num % 2 == 0 and self.count != 1000:
                    if len(faceRects) > 0:  # 大于0则检测到人脸
                        for faceRect in faceRects:  # 单独框出每一张人脸
                            x, y, w, h = faceRect

                            # 截取脸部图像提交给模型识别这是谁
                            image = self.image[y - 10: y + h + 10, x - 10: x + w + 10]
                            probability, name_number = self.model.face_predict(image)
                            print(name_number)
                            name = self.contrast_table[str(name_number)]
                            print('name_number:', name_number)

                            # 画出矩形框
                            cv2.rectangle(self.image, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 1)

                            # 文字提示身份
                            # cv2.putText(self.image, name, (x + 30, y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 1)
                            if probability > 0.7:
                                self.countdown.setText('识别结果为:' + name)
                            else:
                                self.countdown.setText('识别结果为:' + 'unknown')

                    self.count = self.count + 1
            else:
                self.countdown.setText(str(5 - (self.num // 12)))
            self.num = self.num + 1

            # 显示图像
            self.show = cv2.resize(self.image, (940, 835))
            self.show = cv2.cvtColor(self.show, cv2.COLOR_BGR2RGB)
            showImage = QtGui.QImage(self.show.data, self.show.shape[1], self.show.shape[0], QtGui.QImage.Format_RGB888)
            self.label.setPixmap(QtGui.QPixmap.fromImage(showImage))

            c = cv2.waitKey(10)
            if c & 0xFF == ord('q'):
                break

    # 结束人脸识别
    def close_re(self):
        self.timer.stop()
        self.label.clear()
        self.label.setText("人脸采集及识别区域")
        self.countdown.setText("采集/识别等待中")
        cv2.destroyAllWindows()
        # 释放摄像头并销毁所有窗口
        self.cap.release()

    # 注销登录
    def logout_d(self):
        self.hide()  # 隐藏窗口
        self.logout = Login()
        self.logout.show()  # 打开登录窗口

    # 帮助中心
    def help_d(self):
        self.shop = help_hh()
        self.shop.show()

    # 鼠标控制
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
    app = QApplication(sys.argv)
    myWin = Login()
    myWin.show()
    sys.exit(app.exec_())
