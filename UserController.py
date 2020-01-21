from UserWindow import Ui_UserWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class UserController(QtWidgets.QMainWindow, Ui_UserWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.btn_loadASong.clicked.connect(self.loadASong)

    def loadASong(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Song Files (*.csv)", options=options)
        if fileName:
            print(fileName)