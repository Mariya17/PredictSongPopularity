from PredictSongPopularity import PREDICT_RES
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PredictedResultsWindow(object):
    def setupUi(self, PredictedResultsWindow):
        PredictedResultsWindow.setObjectName("PredictedResultsWindow")
        PredictedResultsWindow.setEnabled(True)
        PredictedResultsWindow.resize(700, 609)
        PredictedResultsWindow.setStyleSheet("background-color: rgb(76, 153, 229);\n"
"")
        self.centralwidget = QtWidgets.QWidget(PredictedResultsWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 701, 621))
        self.centralwidget.setObjectName("centralwidget")
        self.lb1 = QtWidgets.QLabel(self.centralwidget)
        self.lb1.setGeometry(QtCore.QRect(130, 50, 461, 51))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(36)
        self.lb1.setFont(font)
        self.lb1.setObjectName("lb1")
        self.learnitg_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.learnitg_label_2.setGeometry(QtCore.QRect(50, 120, 611, 51))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(23)
        self.learnitg_label_2.setFont(font)
        self.learnitg_label_2.setStyleSheet("background-color: transparent;")
        self.learnitg_label_2.setObjectName("learnitg_label_2")
        self.lb_to = QtWidgets.QLabel(self.centralwidget)
        self.lb_to.setGeometry(QtCore.QRect(320, 290, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(34)
        self.lb_to.setFont(font)
        self.lb_to.setStyleSheet("background-color: transparent;")
        self.lb_to.setObjectName("lb_to")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 130, 501, 511))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("abdolah.png"))
        self.label.setObjectName("label")
        self.pt_from = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pt_from.setGeometry(QtCore.QRect(190, 280, 141, 71))
        font = QtGui.QFont()
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.pt_from.setFont(font)
        self.pt_from.setStyleSheet("background-color: transparent;\n"
"")
        self.pt_from.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pt_from.setUndoRedoEnabled(True)
        self.pt_from.setLineWrapMode(QtWidgets.QPlainTextEdit.WidgetWidth)
        self.pt_from.setObjectName("pt_from")
        self.pt_to = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pt_to.setGeometry(QtCore.QRect(380, 280, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(34)
        font.setBold(True)
        font.setWeight(75)
        self.pt_to.setFont(font)
        self.pt_to.setStyleSheet("background-color: transparent;")
        self.pt_to.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.pt_to.setObjectName("pt_to")

        self.label.raise_()
        self.lb1.raise_()
        self.learnitg_label_2.raise_()
        self.lb_to.raise_()
        self.pt_from.raise_()
        self.pt_to.raise_()

        self.menubar = QtWidgets.QMenuBar(PredictedResultsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(PredictedResultsWindow)
        self.statusbar.setGeometry(QtCore.QRect(0, 0, 3, 18))
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(PredictedResultsWindow)
        QtCore.QMetaObject.connectSlotsByName(PredictedResultsWindow)

    def retranslateUi(self, PredictedResultsWindow):
        _translate = QtCore.QCoreApplication.translate
        PredictedResultsWindow.setWindowTitle('Results Window')
        PredictedResultsWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        self.lb1.setText(_translate("PredictedResultsWindow", "PREDICTION RESULTS"))
        self.learnitg_label_2.setText(_translate("PredictedResultsWindow", "Your song probability of success is between:"))
        self.lb_to.setText(_translate("PredictedResultsWindow", "to"))
        self.pt_from.setPlainText(_translate("PredictedResultsWindow", str(PREDICT_RES * 20)+'%'))
        self.pt_to.setPlainText(_translate("PredictedResultsWindow", str((PREDICT_RES * 20)+19)+'%'))

