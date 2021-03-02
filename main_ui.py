from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1150, 850)
        icon = QtGui.QIcon()  # 创建一个对象
        icon.addPixmap(QtGui.QPixmap("img/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off) #设置图标路径
        MainWindow.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.openfile = QtWidgets.QPushButton(self.centralwidget)
        self.openfile.setGeometry(QtCore.QRect(35, 260, 100, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(60)
        self.openfile.setFont(font)
        self.openfile.setObjectName("openfile")

        self.text = QtWidgets.QLineEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(35, 310, 100, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(60)
        self.text.setFont(font)
        self.text.setObjectName("text")

        self.dete = QtWidgets.QPushButton(self.centralwidget)
        self.dete.setGeometry(QtCore.QRect(35, 360, 100, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(60)
        self.dete.setFont(font)
        self.dete.setObjectName("dete")

        self.open = QtWidgets.QPushButton(self.centralwidget)
        self.open.setGeometry(QtCore.QRect(35, 410, 100, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(60)
        self.open.setFont(font)
        self.open.setObjectName("open")

        self.close_ = QtWidgets.QPushButton(self.centralwidget)
        self.close_.setGeometry(QtCore.QRect(35, 460, 100, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(60)
        self.close_.setFont(font)
        self.close_.setObjectName("close_")

        self.close_2 = QtWidgets.QPushButton(self.centralwidget)
        self.close_2.setGeometry(QtCore.QRect(35, 610, 100, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(60)
        self.close_2.setFont(font)
        self.close_2.setObjectName("close_2")

        self.close_3 = QtWidgets.QPushButton(self.centralwidget)
        self.close_3.setGeometry(QtCore.QRect(115, 30, 20, 20))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(60)
        self.close_3.setFont(font)
        self.close_3.setObjectName("close_3")

        self.max_ = QtWidgets.QPushButton(self.centralwidget)
        self.max_.setGeometry(QtCore.QRect(75, 30, 20, 20))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(60)
        self.max_.setFont(font)
        self.max_.setObjectName("max_")

        self.min_ = QtWidgets.QPushButton(self.centralwidget)
        self.min_.setGeometry(QtCore.QRect(35, 30, 20, 20))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(60)
        self.min_.setFont(font)
        self.min_.setObjectName("min_")

        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(35, 660, 100, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(60)
        self.logout.setFont(font)
        self.logout.setObjectName("logout")

        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(35, 710, 100, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(60)
        self.help.setFont(font)
        self.help.setObjectName("help")

        self.train = QtWidgets.QPushButton(self.centralwidget)
        self.train.setGeometry(QtCore.QRect(35, 510, 100, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(60)
        self.train.setFont(font)
        self.train.setObjectName("train")

        self.re = QtWidgets.QPushButton(self.centralwidget)
        self.re.setGeometry(QtCore.QRect(35, 560, 100, 30))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(60)
        self.re.setFont(font)
        self.re.setObjectName("tn")

        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(500, 30, 330, 80))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(29)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(60)
        self.header.setFont(font)
        self.header.setObjectName("header")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 195, 940, 630))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(60)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(35, 100, 100, 120))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.boder = QtWidgets.QLabel(self.centralwidget)
        self.boder.setGeometry(QtCore.QRect(195, 90, 900, 700))
        self.boder.setObjectName("boder")

        self.bgcolor = QtWidgets.QLabel(self.centralwidget)
        self.bgcolor.setGeometry(QtCore.QRect(0, 0, 1150, 850))
        self.bgcolor.setText("")
        self.bgcolor.setObjectName("bgcolor")

        self.countdown = QtWidgets.QLabel(self.centralwidget)
        self.countdown.setGeometry(QtCore.QRect(480, 120, 370, 60))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(60)
        self.countdown.setFont(font)
        self.countdown.setAlignment(QtCore.Qt.AlignCenter)
        self.countdown.setObjectName("countdown")

        self.bgcolor.raise_()
        self.boder.raise_()
        self.open.raise_()
        self.close_.raise_()
        self.close_2.raise_()
        self.close_3.raise_()
        self.max_.raise_()
        self.min_.raise_()
        self.dete.raise_()
        self.text.raise_()
        self.re.raise_()
        self.train.raise_()
        self.label.raise_()
        self.header.raise_()
        self.logout.raise_()
        self.countdown.raise_()
        self.label_2.raise_()
        self.openfile.raise_()
        self.help.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "人脸识别系统"))
        self.open.setText(_translate("MainWindow", "开始采集"))
        self.close_.setText(_translate("MainWindow", "结束采集"))
        self.dete.setText(_translate("MainWindow", "确定姓名"))
        self.label.setText(_translate("MainWindow", "人脸采集/识别区域"))
        self.logout.setText(_translate("MainWindow", "注销登录"))
        self.train.setText(_translate("MainWindow", "模型训练"))
        self.re.setText(_translate("MainWindow", "人脸识别"))
        self.close_2.setText(_translate("MainWindow", "结束识别"))
        self.close_3.setText(_translate("MainWindow", ""))
        self.min_.setText(_translate("MainWindow", ""))
        self.max_.setText(_translate("MainWindow", ""))
        self.countdown.setText(_translate("MainWindow", "采集/识别等待中"))
        self.openfile.setText(_translate("MainWindow", "打开文件"))
        self.help.setText(_translate("MainWindow", "帮助中心"))

        self.countdown.setStyleSheet("border-color:white;border:2px;color:white;")
        self.open.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}"
            "QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}")
        self.train.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}"
            "QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}")
        self.re.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}"
            "QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}")
        self.close_.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}"
            "QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}")
        self.close_2.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}"
            "QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}")
        self.close_3.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.min_.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.max_.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.dete.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}"
            "QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}")
        self.help.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}"
            "QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}")
        self.openfile.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}"
            "QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}")
        self.logout.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}"
            "QPushButton{border:2px groove gray;border-radius:10px;padding:2px 4px;}")
        self.text.setStyleSheet(
            "border-color:black;border:4px;color:black;border-radius:10px;padding:2px 4px;"
            "background-color:rgb(250,250,250)")
        self.label.setStyleSheet("border-color:white;border:2px;""color:white;")
