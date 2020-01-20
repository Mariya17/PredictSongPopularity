
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdministratorWindow(object):

    def setupUi(self, AdministratorWindow):
        AdministratorWindow.setObjectName("AdministratorWindow")
        AdministratorWindow.resize(700, 609)
        AdministratorWindow.setStyleSheet("background-color: rgb(76, 153, 229);\n"
"")
        self.centralwidget = QtWidgets.QWidget(AdministratorWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 0, 701, 621))
        self.centralwidget.setObjectName("centralwidget")
        self.loadDataBase = QtWidgets.QPushButton(self.centralwidget)
        self.loadDataBase.setGeometry(QtCore.QRect(60, 50, 186, 41))

        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.loadDataBase.setFont(font)
        self.loadDataBase.setStyleSheet("background-color: rgb(190, 178, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"")
        self.loadDataBase.setObjectName("loadDataBase")
        self.updateDataBase = QtWidgets.QPushButton(self.centralwidget)
        self.updateDataBase.setGeometry(QtCore.QRect(60, 110, 186, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.updateDataBase.setFont(font)
        self.updateDataBase.setStyleSheet("background-color: rgb(190, 178, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"")
        self.updateDataBase.setObjectName("updateDataBase")
        self.testing = QtWidgets.QPushButton(self.centralwidget)
        self.testing.setGeometry(QtCore.QRect(410, 110, 186, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.testing.setFont(font)
        self.testing.setStyleSheet("background-color: rgb(190, 178, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"")
        self.testing.setObjectName("testing")
        self.learning = QtWidgets.QPushButton(self.centralwidget)
        self.learning.setGeometry(QtCore.QRect(410, 50, 186, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.learning.setFont(font)
        self.learning.setStyleSheet("background-color: rgb(190, 178, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"")
        self.learning.setObjectName("learning")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 200, 701, 391))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("microphoneBackground.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
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

        AdministratorWindow.setWindowTitle('Administrator Main Window')
        AdministratorWindow.setWindowIcon(QtGui.QIcon('icon.png'))

        self.loadDataBase.setText(_translate("AdministratorWindow", "Load Data Base"))
        self.updateDataBase.setText(_translate("AdministratorWindow", "Update Data Base"))
        self.testing.setText(_translate("AdministratorWindow", "Testing"))
        self.learning.setText(_translate("AdministratorWindow", "Learning"))
