from UserWindow import Ui_UserWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import PredictSongPopularity
import os

class UserController(QtWidgets.QMainWindow, Ui_UserWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.perdictSongFileName = "empty"
        self.btn_BrowseASong.clicked.connect(self.browseASong)
        self.btn_predict.clicked.connect(self.predictSong)

    def browseASong(self):
        _translate = QtCore.QCoreApplication.translate

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.perdictSongFileName, _ = QFileDialog.getOpenFileName(self.clearMask(), "QFileDialog.getOpenFileName()", "",
                                                  "Song Files (*.csv)", options=options)
        if not self.perdictSongFileName:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("No file selected. Please select a song file")
            error_dialog.exec()
            self.plainTextEdit.clear()
            self.plainTextEdit.setPlainText("Please select a song file ")
        elif self.perdictSongFileName != "empty":
            listOfPerdictSongFileName = self.perdictSongFileName.split(".")
            endOfselfpredictSongFileName = listOfPerdictSongFileName[len(listOfPerdictSongFileName) - 1]
            if endOfselfpredictSongFileName != "csv":
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage("Error: you selected a '{0}' format file. selecta 'csv' format file"
                                         .format(endOfselfpredictSongFileName))
                error_dialog.exec()
                self.plainTextEdit.clear()
                self.plainTextEdit.setPlainText("Please select again a song file ")
            else:
                self.plainTextEdit.clear()
                self.plainTextEdit.setPlainText(self.perdictSongFileName)

    def predictSong(self):
        if self.perdictSongFileName == "empty":
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("Please selecta song")
            error_dialog.exec()
        else:
            if os.path.isfile('./DAG_File.csv'):
                print("predicting")
                predict = PredictSongPopularity.PredictSongPopularity()
                predict.predictSingle(self.perdictSongFileName)
            else:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage("There is no predicting model. Please contact your administrator")
                error_dialog.exec()





