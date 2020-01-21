from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton
import sys

from AdministratorController import AdministratorController
from UserController import UserController
from MainWindow import Ui_MainWindow


class MainController(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

def changeWindow(w1, w2):
    w1.hide()
    w2.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainController()
    user = UserController()
    administrator = AdministratorController()


    main.btn_user.clicked.connect(lambda: changeWindow(main, user))
    user.btn_back.clicked.connect(lambda: changeWindow(user, main))
    main.btn_administrator.clicked.connect(lambda: changeWindow(main, administrator))


    administrator.btn_back.clicked.connect(lambda: changeWindow(administrator, main))


    main.show()
    sys.exit(app.exec_())