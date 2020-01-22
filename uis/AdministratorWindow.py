# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdministratorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdministratorWindow(object):
    def setupUi(self, AdministratorWindow):
        AdministratorWindow.setObjectName("AdministratorWindow")
        AdministratorWindow.resize(700, 609)
        AdministratorWindow.setStyleSheet("background-color: rgb(76, 153, 229);\n"
"")
        self.centralwidget = QtWidgets.QWidget(AdministratorWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, -10, 701, 621))
        self.centralwidget.setObjectName("centralwidget")
        self.btn_loadDataBase = QtWidgets.QPushButton(self.centralwidget)
        self.btn_loadDataBase.setGeometry(QtCore.QRect(540, 60, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.btn_loadDataBase.setFont(font)
        self.btn_loadDataBase.setStyleSheet("background-color: rgb(190, 178, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"")
        self.btn_loadDataBase.setObjectName("btn_loadDataBase")
        self.btn_testing = QtWidgets.QPushButton(self.centralwidget)
        self.btn_testing.setGeometry(QtCore.QRect(460, 140, 186, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.btn_testing.setFont(font)
        self.btn_testing.setStyleSheet("background-color: rgb(190, 178, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"")
        self.btn_testing.setObjectName("btn_testing")
        self.btn_learning = QtWidgets.QPushButton(self.centralwidget)
        self.btn_learning.setGeometry(QtCore.QRect(30, 140, 186, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.btn_learning.setFont(font)
        self.btn_learning.setStyleSheet("background-color: rgb(190, 178, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"")
        self.btn_learning.setObjectName("btn_learning")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 200, 701, 391))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../microphoneBackground.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(550, 530, 118, 41))
        self.btn_back.setMaximumSize(QtCore.QSize(16777213, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("background-color: rgb(75, 151, 225);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"min-width: 6em;\n"
"padding: 6px;\n"
"")
        self.btn_back.setObjectName("btn_back")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pt_dbpath = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pt_dbpath.setGeometry(QtCore.QRect(170, 70, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pt_dbpath.setFont(font)
        self.pt_dbpath.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pt_dbpath.setObjectName("pt_dbpath")
        self.menubar = QtWidgets.QMenuBar(AdministratorWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(AdministratorWindow)
        self.statusbar.setGeometry(QtCore.QRect(0, 0, 3, 18))
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(AdministratorWindow)
        QtCore.QMetaObject.connectSlotsByName(AdministratorWindow)

    def retranslateUi(self, AdministratorWindow):
        _translate = QtCore.QCoreApplication.translate
        AdministratorWindow.setWindowTitle(_translate("AdministratorWindow", "MainWindow"))
        self.btn_loadDataBase.setText(_translate("AdministratorWindow", "Browse"))
        self.btn_testing.setText(_translate("AdministratorWindow", "Testing"))
        self.btn_learning.setText(_translate("AdministratorWindow", "Learning"))
        self.btn_back.setText(_translate("AdministratorWindow", "Back"))
        self.label_2.setText(_translate("AdministratorWindow", "Load Data Base"))
