
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
        self.label.setPixmap(QtGui.QPixmap("microphoneBackground.png"))
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
        self.pt_dbpath.setPlainText("Please browse a Data Base")
        self.pt_dbpath.setDisabled(True)
        self.lb_learnitg = QtWidgets.QLabel(self.centralwidget)
        self.lb_learnitg.setGeometry(QtCore.QRect(230, 220, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.lb_learnitg.setFont(font)
        self.lb_learnitg.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lb_learnitg.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lb_learnitg.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.lb_learnitg.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lb_learnitg.setLineWidth(0)
        self.lb_learnitg.setObjectName("lb_learnitg")
        self.lb_learnitg.hide()

        self.tl_outputBox = QtWidgets.QLabel(self.centralwidget)
        self.tl_outputBox.setGeometry(QtCore.QRect(40, 340, 451, 201))
        self.tl_outputBox.setStyleSheet("background-color: transparent;")
        self.tl_outputBox.setObjectName("tl_outputBox")

        self.lb_testing = QtWidgets.QLabel(self.centralwidget)
        self.lb_testing.setGeometry(QtCore.QRect(230, 220, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.lb_testing.setFont(font)
        self.lb_testing.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lb_testing.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lb_testing.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.lb_testing.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lb_testing.setLineWidth(0)
        self.lb_testing.setObjectName("lb_testing")
        self.lb_testing.hide()

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(110, 290, 351, 23))
        font = QtGui.QFont()
        font.setFamily("Arial Rounded MT Bold")
        font.setPointSize(24)
        self.progressBar.setFont(font)
        self.progressBar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.progressBar.setStyleSheet("color: rgb(255, 255, 255);")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.hide()
		
        self.lb_completed = QtWidgets.QLabel(self.centralwidget)
        self.lb_completed.setEnabled(False)
        self.lb_completed.setGeometry(QtCore.QRect(200, 320, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Bauhaus 93")
        font.setPointSize(36)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.lb_completed.setFont(font)
        self.lb_completed.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lb_completed.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.lb_completed.setAutoFillBackground(False)
        self.lb_completed.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: transparent;")
        self.lb_completed.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lb_completed.setLineWidth(0)
        self.lb_completed.setObjectName("lb_completed")
        self.lb_completed.hide()

        self.btn_loadK2Input = QtWidgets.QPushButton(self.centralwidget)
        self.btn_loadK2Input.setGeometry(QtCore.QRect(540, 90, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setKerning(True)
        self.btn_loadK2Input.setFont(font)
        self.btn_loadK2Input.setStyleSheet("background-color: rgb(190, 178, 255);\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"min-width: 5em;\n"
"padding: 6px;\n"
"")
        self.btn_loadK2Input.setObjectName("btn_loadK2Input")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pt_k2path = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pt_k2path.setGeometry(QtCore.QRect(170, 100, 361, 31))
        self.pt_k2path.setPlainText("Please browse a K2 Input")
        self.pt_k2path.setDisabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pt_k2path.setFont(font)
        self.pt_k2path.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pt_k2path.setObjectName("pt_k2path")


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
        self.btn_loadDataBase.setText(_translate("AdministratorWindow", "Browse"))
        self.btn_testing.setText(_translate("AdministratorWindow", "Testing"))
        self.btn_learning.setText(_translate("AdministratorWindow", "Learning"))
        self.btn_back.setText(_translate("AdministratorWindow", "Back"))
        self.label_2.setText(_translate("AdministratorWindow", "Load Data Base"))
        self.lb_learnitg.setText(_translate("AdministratorWindow", "Learning"))
        self.lb_testing.setText(_translate("AdministratorWindow", "Testing"))
        self.lb_completed.setText(_translate("AdministratorWindow", "Completed"))
