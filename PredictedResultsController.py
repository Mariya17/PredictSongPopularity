from PyQt5 import QtWidgets

from PredictedResultsWindow import Ui_PredictedResultsWindow



class PredictedResultsController(QtWidgets.QMainWindow, Ui_PredictedResultsWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
