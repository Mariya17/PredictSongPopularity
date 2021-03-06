from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import os
from Const import Files

from AdministratorWindow import Ui_AdministratorWindow
import Measurements
from PredictSongPopularity import PredictSongPopularity

progressValue = 100

class AdministratorController(QtWidgets.QMainWindow, Ui_AdministratorWindow):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.learningFlaf = False
        self.newFileFlag = False
        self.predictor = PredictSongPopularity()

        self.k2InputFileName = "empty"
        self.btn_loadDataBase.clicked.connect(self.loadDataBase)
        self.btn_loadK2Input.clicked.connect(self.browseK2Input)
        self.btn_learning.clicked.connect(self.learning)
        self.btn_testing.clicked.connect(self.testing)
        self.btn_statistics.clicked.connect(self.showGraph)

        self.graphFile = Files.GRAPH

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
            if fileSize < 10000:
                QtWidgets.QMessageBox.information(self.clearMask(), "Data Error",
                                                  "The data base is too small or empty.\nTry another one.")
            else:
                self.newFileFlag = True
        else:
            QtWidgets.QMessageBox.information(self.clearMask(), "Data Error",
                                        "No file selected. Please select a Data Base")
            return

    def disable_all_buttons(self, val):
        self.btn_learning.setDisabled(val)
        self.btn_back.setDisabled(val)
        self.btn_loadDataBase.setDisabled(val)
        self.btn_learning.setDisabled(val)
        self.btn_testing.setDisabled(val)
        self.btn_loadK2Input.setDisabled(val)
        self.btn_statistics.setDisabled(val)


    def learning(self):
        if not self.newFileFlag:
            QtWidgets.QMessageBox.information(self.clearMask(), "Info Message",
                                              "Please select a Data Base for learning.")
            return
        if self.k2InputFileName == "empty":
            QtWidgets.QMessageBox.information(self.clearMask(), "Info Message",
                                              "Please select a K2 Input before learning.")
            return
        self.lb_learnitg.show()
        self.progressBar.setValue(0)
        self.progressBar.show()
        self.disable_all_buttons(True)

        choice = QtWidgets.QMessageBox.question(self.clearMask(), 'Message',
                                                "Learning may take a lot of time.\n"
                                                "Start Learning?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            self.predictor.preprocessing()
            log_str = 'Data Preprocessing Completed\nStarted K2 Algorithm\n'
            self.tl_outputBox.setText(log_str)
            self.progressBar.setValue(10)
            k2_str = self.predictor.performK2()
            if k2_str != '':
                QtWidgets.QMessageBox.information(self.clearMask(), "Info Message",
                                                  k2_str)
                self.disable_all_buttons(False)
                return
            log_str += 'K2 Algorithm Completed\nStarted Bayesian Learning Prossess\n'
            self.tl_outputBox.setText(log_str)
            self.progressBar.setValue(25)
            self.predictor.bayesianLearning()
            log_str += 'Completed Bayesian Learning Prossess\n'
            self.tl_outputBox.setText(log_str)
            self.progressBar.setValue(100)

            self.learningFlaf = True
            self.progressBar.hide()
            self.lb_completed.show()
        else:
            self.lb_learnitg.hide()
            self.progressBar.hide()
        self.disable_all_buttons(False)

    def testing(self):
        if not self.learningFlaf:
            QtWidgets.QMessageBox.information(self.clearMask(), "Info Message",
                                    "Please complete Learning before Testing")
            return
        self.lb_learnitg.hide()
        self.lb_completed.hide()

        self.lb_testing.show()
        self.progressBar.setValue(0)
        self.progressBar.show()

        self.tl_outputBox.setText('')
        self.disable_all_buttons(True)
        choice = QtWidgets.QMessageBox.question(self.clearMask(), 'Message',
                                                "Testining may take a lot of time.\n"
                                                "Start Testining?",
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:

            ############## Testing #######################
            self.progressBar.setValue(3)
            log_str = 'Started Bayesian Testing\n'
            self.tl_outputBox.setText(log_str)
            self.predictor.bayesianTesting()
            log_str += 'Completed Testing\n'
            self.tl_outputBox.setText(log_str)
            self.progressBar.setValue(90)
            mseStr = self.predictor.mseMeasure()
            log_str += mseStr
            mseList = mseStr.split(' ')
            mseStr = mseList[len(mseList) - 1]
            mseList = mseStr.split('\n')
            mseStr = mseList[0]
            self.tl_outputBox.setText(log_str)
            self.progressBar.setValue(95)
            errorRateStr = self.predictor.errorInPresents()
            log_str += errorRateStr
            errorRateList = errorRateStr.split(' ')
            errorRateStr = errorRateList[len(errorRateList)-1]
            errorRateList = errorRateStr.split('%')
            errorRateStr = errorRateList[0]
            self.tl_outputBox.setText(log_str)
            self.progressBar.setValue(100)
            self.progressBar.hide()
            self.lb_completed.show()
            Measurements.addToGraphFile(mseStr, errorRateStr)
        else:
            self.lb_testing.hide()
            self.progressBar.hide()
        self.disable_all_buttons(False)

    def browseK2Input(self):
        _translate = QtCore.QCoreApplication.translate

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.k2InputFileName, _ = QFileDialog.getOpenFileName(self.clearMask(), "QFileDialog.getOpenFileName()", "",

                                                                  "DB Files (*.csv)", options=options)
        if not self.k2InputFileName:
            QtWidgets.QMessageBox.information(self.clearMask(), "Info Message",
                                              "No file selected. Please select a K2 Input")
            return
        elif self.k2InputFileName != "empty":
            listOfK2InputFileName = self.k2InputFileName.split(".")
            endOfK2InputFileName = listOfK2InputFileName[len(listOfK2InputFileName) - 1]
            if endOfK2InputFileName != "csv":
                QtWidgets.QMessageBox.information(self.clearMask(), "Error Message",
                                                  "Error: you selected a '{0}' format file. Please select a 'csv' format file"
                                         .format(endOfK2InputFileName))
                return
            else:
                self.pt_k2path.clear()
                self.pt_k2path.setPlainText(self.k2InputFileName)
                self.predictor.ordered_list_file = self.k2InputFileName

    def showGraph(self):
        Measurements.createGraph()

