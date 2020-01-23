from UserWindow import Ui_UserWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from PredictedResultsController import PredictedResultsController
import PredictSongPopularity
import os

class UserController(QtWidgets.QMainWindow, Ui_UserWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.predictedResults = PredictedResultsController()

        self.perdictSongFileName = "empty"
        self.btn_BrowseASong.clicked.connect(self.browseASong)
        self.btn_predict.clicked.connect(self.predictSong)


    def browseASong(self):
        _translate = QtCore.QCoreApplication.translate

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.perdictSongFileName, _ = QFileDialog.getOpenFileName(self.clearMask(), "QFileDialog.getOpenFileName()", "",
                                                  "Song Files (*.csv);;All Files (*)", options=options)
        if not self.perdictSongFileName:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("No file selected. Please browse a song file")
            error_dialog.exec()
            self.plainTextEdit.clear()
            self.plainTextEdit.setPlainText("Please browse a song file ")
        elif self.perdictSongFileName != "empty":
            listOfPerdictSongFileName = self.perdictSongFileName.split(".")
            endOfselfpredictSongFileName = listOfPerdictSongFileName[len(listOfPerdictSongFileName) - 1]
            if endOfselfpredictSongFileName != "csv":
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage("Error: you browsed a '{0}' format file. Please load a 'csv' format file"
                                         .format(endOfselfpredictSongFileName))
                error_dialog.exec()
                self.plainTextEdit.clear()
                self.plainTextEdit.setPlainText("Please browse again a song file ")
            else:
                self.plainTextEdit.clear()
                self.plainTextEdit.setPlainText(self.perdictSongFileName)
    def setPredictionEstimation(self, res):
        if res == 4:
            self.predictedResults.pt_from.setPlainText('99%')
            self.predictedResults.pt_to.setPlainText('80%')
        elif res == 3:
            self.predictedResults.pt_from.setPlainText('79%')
            self.predictedResults.pt_to.setPlainText('60%')
        elif res == 2:
            self.predictedResults.pt_from.setPlainText('59%')
            self.predictedResults.pt_to.setPlainText('40%')
        elif res == 1:
            self.predictedResults.pt_from.setPlainText('39%')
            self.predictedResults.pt_to.setPlainText('20%')
        else:
            self.predictedResults.pt_from.setPlainText('19%')
            self.predictedResults.pt_to.setPlainText('0%')
        self.predictedResults.pt_from.setEnabled(False)
        self.predictedResults.pt_to.setEnabled(False)

    def predictSong(self):
        if self.perdictSongFileName == "empty":
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("Please load a song")
            error_dialog.exec()
        else:
            if os.path.isfile('./DAG_File.csv'):
                print("predicting")
                predict = PredictSongPopularity.PredictSongPopularity()
                res = predict.predictSingle(self.perdictSongFileName)
                self.setPredictionEstimation(res)

                self.predictedResults.show()
            else:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage("There is no predicting model. Please contact your administrator")
                error_dialog.exec()





