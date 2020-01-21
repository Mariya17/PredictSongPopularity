from AdministratorWindow import Ui_AdministratorWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PredictSongPopularity import PredictSongPopularity
from LearningController import LearningController

class AdministratorController(QtWidgets.QMainWindow, Ui_AdministratorWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.learningFlaf = False
        self.predictor = PredictSongPopularity()

        self.btn_loadDataBase.clicked.connect(self.loadDataBase)
        # self.btn_learning.clicked.connect(self.learning)

    def loadDataBase(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self.clearMask(), "QFileDialog.getOpenFileName()", "",
                                                  "Python Files (*.csv)", options=options)
        if fileName:
            self.pt_dbpath.setPlainText(fileName)
            print(fileName)
            self.predictor.db_file_name = fileName

    # def learning(self):
    #
    #     self.predictor.predict()

    def changeWindow(self, w2):
        self.hide()
        w2.show()