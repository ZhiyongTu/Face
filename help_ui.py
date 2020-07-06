from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_help_hh(object):
    def setupUi(self, help_hh):
        help_hh.setObjectName("help_hh")
        help_hh.setFixedSize(1150, 850)
        icon = QtGui.QIcon()  # 创建一个对象
        icon.addPixmap(QtGui.QPixmap("img/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)  # 设置图标路径
        help_hh.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setFamily("仿宋")
        help_hh.setFont(font)
        self.setWindowOpacity(0.9)
        self.centralwidget = QtWidgets.QWidget(help_hh)
        self.centralwidget.setObjectName("centralwidget")

        self.help = QtWidgets.QLabel(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(320, 220, 700, 800))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(22)
        self.help.setFont(font)
        self.help.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.help.setObjectName("help")

        self.close_3 = QtWidgets.QPushButton(self.centralwidget)
        self.close_3.setGeometry(QtCore.QRect(115, 30, 20, 20))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.close_3.setFont(font)
        self.close_3.setObjectName("close_3")

        self.max_ = QtWidgets.QPushButton(self.centralwidget)
        self.max_.setGeometry(QtCore.QRect(75, 30, 20, 20))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.max_.setFont(font)
        self.max_.setObjectName("max_")

        self.min_ = QtWidgets.QPushButton(self.centralwidget)
        self.min_.setGeometry(QtCore.QRect(35, 30, 20, 20))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.min_.setFont(font)
        self.min_.setObjectName("min_")

        # 加logo
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(800, 20, 451, 81))
        self.logo.setObjectName("logo")

        self.bgcolor = QtWidgets.QLabel(self.centralwidget)
        self.bgcolor.setGeometry(QtCore.QRect(0, 0, 1150, 850))
        self.bgcolor.setText("")
        self.bgcolor.setObjectName("bgcolor")

        font = QtGui.QFont()
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)

        self.bgcolor.raise_()
        self.help.raise_()

        self.close_3.raise_()
        self.max_.raise_()
        self.min_.raise_()

        self.logo.raise_()

        help_hh.setCentralWidget(self.centralwidget)

        self.retranslateUi(help_hh)
        QtCore.QMetaObject.connectSlotsByName(help_hh)
        
    def retranslateUi(self, help_hh):
        _translate = QtCore.QCoreApplication.translate
        help_hh.setWindowTitle(_translate("help_hh", "帮助"))
        pixmap = QtGui.QPixmap("./img/logo.png")
        self.logo.setPixmap(pixmap)
        self.help.setText(_translate("help_hh", "人脸识别界面\n\n"
                                                "1.打开文件：请先打开用户文件夹：user_info\n"
                                                "2.确定姓名：生成对应学号的人脸存储文件夹\n"
                                                "3.开始采集：打开摄像头，自动检测和裁剪人脸图片\n，并保存至对应文件夹\n"
                                                "4.结束采集：关闭摄像头\n"
                                                "5.模型训练：将采集的人脸数据导入CNN中训练模型\n得到face.model和contrast_table文件\n"
                                                "6.人脸识别：打开摄像头，自动检测和识别人脸\n"
                                                "7.结束识别：关闭摄像头\n"
                                                "8.注销登录：注销并返回登录界面\n\n"
                                                "登录界面\n\n"
                                                "1.登录：密码登录系统\n"
                                                "2.退出：退出系统\n"
                                                "3.人脸登录：通过人脸识别登录系统"))

        self.close_3.setText(_translate("MainWindow", ""))
        self.min_.setText(_translate("MainWindow", ""))
        self.max_.setText(_translate("MainWindow", ""))

        self.help.setStyleSheet("border-color:white;border:2px;color:white;")
        self.close_3.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.min_.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.max_.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
