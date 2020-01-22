from UserWindow import Ui_UserWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
import PredictSongPopularity

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
                                                  "All Files (*);;Song Files (*.csv)", options=options)
        if self.perdictSongFileName != "empty":
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

    def predictSong(self):
        if self.perdictSongFileName == "empty":
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage("Please load a song")
            error_dialog.exec()
        else:
            print("predicting")
            predict = PredictSongPopularity.PredictSongPopularity()
            predict.predictSingle(self.perdictSongFileName)





