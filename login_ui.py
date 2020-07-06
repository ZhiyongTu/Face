from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.setFixedSize(1150, 850)
        icon = QtGui.QIcon()  # 创建一个对象
        icon.addPixmap(QtGui.QPixmap("img/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)  # 设置图标路径
        login.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(login)
        self.centralwidget.setObjectName("centralwidget")

        self.enter = QtWidgets.QPushButton(self.centralwidget)
        self.enter.setGeometry(QtCore.QRect(550, 550, 100, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.enter.setFont(font)
        self.enter.setObjectName("enter")

        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(670, 550, 100, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")

        # 加logo
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(800, 20, 451, 81))
        self.logo.setObjectName("logo")

        self.face = QtWidgets.QPushButton(self.centralwidget)
        self.face.setGeometry(QtCore.QRect(790, 550, 100, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.face.setFont(font)
        self.face.setObjectName("face")

        self.close_3 = QtWidgets.QPushButton(self.centralwidget)
        self.close_3.setGeometry(QtCore.QRect(165, 50, 20, 20))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.close_3.setFont(font)
        self.close_3.setObjectName("close_3")

        self.max_ = QtWidgets.QPushButton(self.centralwidget)
        self.max_.setGeometry(QtCore.QRect(125, 50, 20, 20))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.max_.setFont(font)
        self.max_.setObjectName("max_")

        self.min_ = QtWidgets.QPushButton(self.centralwidget)
        self.min_.setGeometry(QtCore.QRect(85, 50, 20, 20))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        self.min_.setFont(font)
        self.min_.setObjectName("min_")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(550, 220, 451, 81))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(550, 370, 80, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(550, 450, 80, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.account = QtWidgets.QLineEdit(self.centralwidget)
        self.account.setGeometry(QtCore.QRect(630, 370, 260, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(15)
        self.account.setFont(font)
        self.account.setText("")
        self.account.setObjectName("account")

        self.label_4 = QtWidgets.QPushButton(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(900, 370, 105, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.word = QtWidgets.QLineEdit(self.centralwidget)
        self.word.setGeometry(QtCore.QRect(630, 450, 260, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(15)
        self.word.setFont(font)
        self.word.setObjectName("word")

        self.label_5 = QtWidgets.QPushButton(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(900, 450, 105, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(630, 500, 200, 20))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")

        self.prompt = QtWidgets.QLabel(self.centralwidget)
        self.prompt.setGeometry(QtCore.QRect(650, 610, 231, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.prompt.setFont(font)
        self.prompt.setText("")
        self.prompt.setObjectName("prompt")
        self.logoo = QtWidgets.QLabel(self.centralwidget)
        self.logoo.setGeometry(QtCore.QRect(0, 0, 3000, 2000))
        self.logoo.setText("")
        self.logoo.setObjectName("logoo")
        self.logoo.raise_()
        self.enter.raise_()
        self.exit.raise_()
        self.face.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.checkBox.raise_()
        self.account.raise_()
        self.word.raise_()
        self.prompt.raise_()

        self.close_3.raise_()
        self.max_.raise_()
        self.min_.raise_()
        self.logo.raise_()

        login.setCentralWidget(self.centralwidget)
        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "登录界面"))
        self.enter.setText(_translate("login", "登录"))
        self.exit.setText(_translate("login", "退出"))
        self.face.setText(_translate("login", "人脸登录"))
        self.label.setText(_translate("login", "人脸识别系统登录"))
        pixmap = QtGui.QPixmap("./img/logo.png")
        self.logo.setPixmap(pixmap)
        self.label_2.setText(_translate("login", "账号："))
        self.label_3.setText(_translate("login", "密码："))
        self.label_4.setText(_translate("login", "注册账号"))
        self.label_5.setText(_translate("login", "找回密码"))
        self.checkBox.setText(_translate("login", "记住用户名和密码"))
        self.label.setStyleSheet("color:white;")
        self.label_2.setStyleSheet("color:white;")
        self.label_3.setStyleSheet("color:white;")
        self.checkBox.setStyleSheet("color:white;")
        self.prompt.setStyleSheet("color:white;")

        self.account.setStyleSheet(
            "border-color:black;border:4px;color:groove gray;border-radius:10px;padding:2px 4px;"
            "background-color:rgb(250,250,250)")
        self.word.setStyleSheet(
            "border-color:black;border:4px;color:groove gray;border-radius:10px;padding:2px 4px;"
            "background-color:rgb(250,250,250)")

        self.label_4.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}"
            "QPushButton{color:white;border-radius:10px;padding:2px 4px;}")
        self.label_5.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}"
            "QPushButton{color:white;border-radius:10px;padding:2px 4px;}")

        self.enter.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}"
            "QPushButton{color:white;border:2px groove gray;border-radius:10px;padding:2px 4px;}")
        self.exit.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}"
            "QPushButton{color:white;border:2px groove gray;border-radius:10px;padding:2px 4px;}")
        self.face.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}"
            "QPushButton{color:white;border:2px groove gray;border-radius:10px;padding:2px 4px;}")

        self.close_3.setText(_translate("MainWindow", ""))
        self.min_.setText(_translate("MainWindow", ""))
        self.max_.setText(_translate("MainWindow", ""))

        self.close_3.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.min_.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.max_.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')