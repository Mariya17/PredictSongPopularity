# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UserWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserWindow(object):
    def setupUi(self, UserWindow):
        UserWindow.setObjectName("UserWindow")
        UserWindow.resize(700, 609)
        UserWindow.setStyleSheet("background-color: rgb(76, 153, 229);\n"
"")
        self.centralwidget = QtWidgets.QWidget(UserWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 701, 621))
        self.centralwidget.setObjectName("centralwidget")
        self.loadASong = QtWidgets.QPushButton(self.centralwidget)
        self.loadASong.setGeometry(QtCore.QRect(50, 80, 186, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.loadASong.setFont(font)
        self.loadASong.setStyleSheet("background-color: rgb(190, 178, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"")
        self.loadASong.setObjectName("loadASong")
        self.predict = QtWidgets.QPushButton(self.centralwidget)
        self.predict.setGeometry(QtCore.QRect(410, 80, 186, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.predict.setFont(font)
        self.predict.setStyleSheet("background-color: rgb(190, 178, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"")
        self.predict.setObjectName("predict")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 200, 701, 391))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../microphoneBackground.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(568, 530, 118, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.back.setFont(font)
        self.back.setStyleSheet("background-color: rgb(75, 151, 225);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"min-width: 6em;\n"
"padding: 6px;\n"
"")
        self.back.setObjectName("back")
        self.menubar = QtWidgets.QMenuBar(UserWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(UserWindow)
        self.statusbar.setGeometry(QtCore.QRect(0, 0, 3, 18))
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(UserWindow)
        QtCore.QMetaObject.connectSlotsByName(UserWindow)

    def retranslateUi(self, UserWindow):
        _translate = QtCore.QCoreApplication.translate
        UserWindow.setWindowTitle(_translate("UserWindow", "MainWindow"))
        self.loadASong.setText(_translate("UserWindow", "Load A Song"))
        self.predict.setText(_translate("UserWindow", "Predict"))
        self.back.setText(_translate("UserWindow", "Back"))
