from AdministratorWindow import Ui_AdministratorWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
class AdministratorController(QtWidgets.QMainWindow, Ui_AdministratorWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.btn_loadDataBase.clicked.connect(self.loadDataBase)

    def loadDataBase(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.csv)", options=options)
        if fileName:
            print(fileName)