from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton
import sys

from AdministratorWindow import Ui_AdministratorWindow
from UserWindow import Ui_UserWindow
from MainWindow import Ui_MainWindow
from LearningWindow import Ui_LearningWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

class AdministratorWindow(QtWidgets.QMainWindow, Ui_AdministratorWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

class UserWindow(QtWidgets.QMainWindow, Ui_UserWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

class LearningWindow(QtWidgets.QMainWindow, Ui_LearningWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)


def changeWindow(w1, w2):
    w1.hide()
    w2.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    user = UserWindow()
    administrator = AdministratorWindow()
    learning = LearningWindow()

    main.btn_user.clicked.connect(lambda: changeWindow(main, user))
    user.btn_back.clicked.connect(lambda: changeWindow(user, main))
    main.btn_administrator.clicked.connect(lambda: changeWindow(main, administrator))
    administrator.btn_learning.clicked.connect(lambda: changeWindow(administrator, learning))
    administrator.btn_back.clicked.connect(lambda: changeWindow(administrator, main))

    main.show()
    sys.exit(app.exec_())