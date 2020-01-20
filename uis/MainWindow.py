# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from AdministratorGui import Ui_AdministratorWindow

class Ui_MainWindow(object):
    def openAdminWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_AdministratorWindow()
        self.ui.seupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 609)
        MainWindow.setStyleSheet("background-color: rgb(76, 153, 229);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.userBT = QtWidgets.QPushButton(self.centralwidget)
        self.userBT.setGeometry(QtCore.QRect(60, 50, 186, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.userBT.setFont(font)
        self.userBT.setStyleSheet("background-color: rgb(190, 178, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"")
        self.userBT.setObjectName("userBT")
        self.AdministratorBT = QtWidgets.QPushButton(self.centralwidget)
        self.AdministratorBT.setGeometry(QtCore.QRect(410, 50, 186, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.AdministratorBT.setFont(font)
        self.AdministratorBT.setStyleSheet("background-color: rgb(190, 178, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"")
        self.AdministratorBT.setObjectName("AdministratorBT")

        self.AdministratorBT.clicked.connect(self.openAdminWindow())

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 180, 701, 391))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../microphoneBackground.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.userBT.setText(_translate("MainWindow", "User"))
        self.AdministratorBT.setText(_translate("MainWindow", "Administrator"))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())