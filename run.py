from PyQt5.QtWidgets import *
from login import *
from main import *

class Controller:
    def __init__(self):
        pass

    def show_login(self):
        self.login = Login()
        self.login.switch_main.connect(self.show_main)
        self.login.show()

    def show_main(self):
        self.main = MyWindow()
        self.main.switch_login.connect(self.show_login)
        self.main.show()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())