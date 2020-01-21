from LearningWindow import Ui_LearningWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class LearningController(QtWidgets.QMainWindow, Ui_LearningWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)