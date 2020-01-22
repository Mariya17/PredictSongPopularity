import os
from AdministratorWindow import Ui_AdministratorWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PredictSongPopularity import PredictSongPopularity

progressValue = 100

class AdministratorController(QtWidgets.QMainWindow, Ui_AdministratorWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.learningFlaf = False
        self.newFileFlag = False
        self.predictor = PredictSongPopularity()

        self.btn_loadDataBase.clicked.connect(self.loadDataBase)
        self.btn_learning.clicked.connect(self.learning)
        self.btn_testing.clicked.connect(self.testing)

    def loadDataBase(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self.clearMask(), "QFileDialog.getOpenFileName()", "",
                                                  "Python Files (*.csv)", options=options)
        if fileName:
            self.pt_dbpath.setPlainText(fileName)
            print(fileName)
            self.predictor.db_file_name = fileName
            self.pt_dbpath.setDisabled(True)
            fileSize = os.path.getsize(fileName)
            if fileSize < 100:
                QtWidgets.QMessageBox.information(self.clearMask(), "QMessageBox.information()",
                                                  "The data base is too small or empty.\nTry another one.")
            else:
                self.newFileFlag = True

    def learning(self):
        if not self.newFileFlag:
            QtWidgets.QMessageBox.information(self.clearMask(), "QMessageBox.information()",
                                              "Please load a Data Base for learning.")
            return
        self.lb_learnitg.show()
        self.progressBar.setValue(progressValue)
        self.progressBar.show()
        self.btn_learning.setDisabled(True)
        self.btn_back.setDisabled(True)
        self.btn_loadDataBase.setDisabled(True)
        self.btn_learning.setDisabled(True)
        self.btn_testing.setDisabled(True)

        choice = QtWidgets.QMessageBox.question(self.clearMask(), 'Message',
                                                "Learning may take a lot of time.\n"
                                                "Start Learning?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            # self.predictor.predict()
            self.learningFlaf = True
            self.progressBar.hide()
            self.lb_completed.show()
        else:
            self.lb_learnitg.hide()
            self.progressBar.hide()
        self.btn_learning.setDisabled(False)
        self.btn_back.setDisabled(False)
        self.btn_loadDataBase.setDisabled(False)
        self.btn_learning.setDisabled(False)
        self.btn_testing.setDisabled(False)


    def testing(self):
        if not self.learningFlaf:
            QtWidgets.QMessageBox.information(self.clearMask(), "QMessageBox.information()",
                                    "Please complete Learning before Testing")
            return
        self.lb_learnitg.hide()
        self.lb_completed.hide()

        self.lb_testing.show()
        self.progressBar.setValue(progressValue)
        self.progressBar.show()

        self.btn_learning.setDisabled(True)
        self.btn_back.setDisabled(True)
        self.btn_loadDataBase.setDisabled(True)
        self.btn_learning.setDisabled(True)
        self.btn_testing.setDisabled(True)

        choice = QtWidgets.QMessageBox.question(self.clearMask(), 'Message',
                                                "Testining may take a lot of time.\n"
                                                "Start Testining?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:

            ############## Testing #######################
            # self.predictor.predict()
            self.progressBar.hide()
            self.lb_completed.show()
        else:
            self.lb_testing.hide()
            self.progressBar.hide()
        self.btn_learning.setDisabled(False)
        self.btn_back.setDisabled(False)
        self.btn_loadDataBase.setDisabled(False)
        self.btn_learning.setDisabled(False)
        self.btn_testing.setDisabled(False)




