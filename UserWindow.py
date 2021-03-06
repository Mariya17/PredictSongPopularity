
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserWindow(object):
    def setupUi(self, UserWindow):
        UserWindow.setObjectName("UserWindow")
        UserWindow.resize(700, 609)
        UserWindow.setStyleSheet("background-color: rgb(76, 153, 229);\n""")
        self.centralwidget = QtWidgets.QWidget(UserWindow)
        self.centralwidget.setGeometry(QtCore.QRect(-10, 0, 701, 621))
        self.centralwidget.setObjectName("centralwidget")
        self.btn_BrowseASong = QtWidgets.QPushButton(self.centralwidget)
        self.btn_BrowseASong.setGeometry(QtCore.QRect(570, 60, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.btn_BrowseASong.setFont(font)
        self.btn_BrowseASong.setStyleSheet("background-color: rgb(190, 178, 255);\n"
                                         "border-style: outset;\n"
                                         "border-width: 2px;\n"
                                         "border-radius: 10px;\n"
                                         "border-color: beige;\n"
                                         "font: bold 14px;\n"
                                         "min-width: 5em;\n"
                                         "padding: 6px;\n"
                                         "")
        self.btn_BrowseASong.setObjectName("btn_BrowseASong")
        self.btn_predict = QtWidgets.QPushButton(self.centralwidget)
        self.btn_predict.setGeometry(QtCore.QRect(490, 130, 186, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.btn_predict.setFont(font)
        self.btn_predict.setStyleSheet("background-color: rgb(190, 178, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"min-width: 10em;\n"
"padding: 6px;\n"
"")
        self.btn_predict.setObjectName("btn_predict")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 200, 701, 391))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("microphoneBackground.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(540, 530, 118, 41))
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
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(170, 70, 391, 31))
        self.plainTextEdit.setAutoFillBackground(False)
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setDisabled(True)
        self.plainTextEdit.setPlainText("Please select a song file")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 121, 21))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
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

        UserWindow.setWindowTitle('User Main Window')
        UserWindow.setWindowIcon(QtGui.QIcon('icon.png'))
        self.btn_BrowseASong.setText(_translate("UserWindow", "Browse"))
        self.btn_predict.setText(_translate("UserWindow", "Predict"))
        self.btn_back.setText(_translate("UserWindow", "Back"))
        self.label_2.setText(_translate("UserWindow", "Load A Song"))
