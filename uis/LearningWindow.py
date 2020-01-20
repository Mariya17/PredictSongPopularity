# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LearningWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LearningWindow(object):
    def setupUi(self, LearningWindow):
        LearningWindow.setObjectName("LearningWindow")
        LearningWindow.setEnabled(True)
        LearningWindow.resize(700, 609)
        LearningWindow.setStyleSheet("background-color: rgb(76, 153, 229);\n"
"")
        self.centralwidget = QtWidgets.QWidget(LearningWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 701, 621))
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 200, 701, 391))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../microphoneBackground.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.learnitg_label = QtWidgets.QLabel(self.centralwidget)
        self.learnitg_label.setGeometry(QtCore.QRect(240, 50, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(36)
        self.learnitg_label.setFont(font)
        self.learnitg_label.setObjectName("learnitg_label")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(150, 130, 351, 23))
        self.progressBar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.menubar = QtWidgets.QMenuBar(LearningWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(LearningWindow)
        self.statusbar.setGeometry(QtCore.QRect(0, 0, 3, 18))
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(LearningWindow)
        QtCore.QMetaObject.connectSlotsByName(LearningWindow)

    def retranslateUi(self, LearningWindow):
        _translate = QtCore.QCoreApplication.translate
        LearningWindow.setWindowTitle(_translate("LearningWindow", "MainWindow"))
        self.learnitg_label.setText(_translate("LearningWindow", "Learning"))
