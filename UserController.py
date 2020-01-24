from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import os
from UserWindow import Ui_UserWindow
import PredictSongPopularity
from PredictedResultsController import PredictedResultsController

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
                                                  "Song Files (*.csv)", options=options)
        if not self.perdictSongFileName:
            QtWidgets.QMessageBox.information(self.clearMask(), "Info Message",
                                              "No file selected. Please select a song file")
            return
        elif self.perdictSongFileName != "empty":
            listOfPerdictSongFileName = self.perdictSongFileName.split(".")
            endOfselfpredictSongFileName = listOfPerdictSongFileName[len(listOfPerdictSongFileName) - 1]
            if endOfselfpredictSongFileName != "csv":
                QtWidgets.QMessageBox.information(self.clearMask(), "Error Message",
                                                  "Error: you selected a '{0}' format file. select a 'csv' format file"
                                         .format(endOfselfpredictSongFileName))
                return
            else:
                self.plainTextEdit.clear()
                self.plainTextEdit.setPlainText(self.perdictSongFileName)

    def setPredictionEstimation(self, res):
        from_val = ''
        to_val = ''
        if res == 5:
            from_val = '99%'
            to_val = '85%'
        elif res == 4:
            from_val = '84%'
            to_val = '68%'
        elif res == 3:
            from_val = '67%'
            to_val = '51%'
        elif res == 2:
            from_val = '50%'
            to_val = '34%'
        elif res == 1:
            from_val = '33%'
            to_val = '17%'
        else:
            from_val = '16%'
            to_val = '0%'

        self.predictedResults.pt_from.setPlainText(from_val)
        self.predictedResults.pt_to.setPlainText(to_val)
        self.predictedResults.pt_from.setEnabled(False)
        self.predictedResults.pt_to.setEnabled(False)


    def predictSong(self):
        if self.perdictSongFileName == "empty":
            QtWidgets.QMessageBox.information(self.clearMask(), "Info Message",
                                              "Please select a song")
        else:
            if os.path.isfile('./DAG_File.csv'):
                print("predicting")
                predict = PredictSongPopularity.PredictSongPopularity()
                res = predict.predictSingle(self.perdictSongFileName)
                self.setPredictionEstimation(res)

                self.predictedResults.show()
            else:
                QtWidgets.QMessageBox.information(self.clearMask(), "Info Message",
                                                  "There is no predicting model. Please contact your administrator")





