import os
from PredictedResultsWindow import Ui_PredictedResultsWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from Const import Files



class PredictedResultsController(QtWidgets.QMainWindow, Ui_PredictedResultsWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
