from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit
from PyQt6.QtCore import pyqtSlot, Qt
from PyQt6 import QtCore, QtGui, QtWidgets



class Ui_vozv_tic(object):
    def setupUi(self, vozv_tic):
        vozv_tic.setObjectName("vozv_tic")
        vozv_tic.resize(633, 301)
        self.centralwidget = QtWidgets.QWidget(vozv_tic)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 170, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 170, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setPlaceholderText("2 1432")

        self.lineEdit.setGeometry(QtCore.QRect(290, 60, 251, 41))
        self.lineEdit.setObjectName("lineEdit")
        vozv_tic.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(vozv_tic)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 633, 26))
        self.menubar.setObjectName("menubar")
        vozv_tic.setMenuBar(self.menubar)

        self.retranslateUi(vozv_tic)
        QtCore.QMetaObject.connectSlotsByName(vozv_tic)


    def retranslateUi(self, vozv_tic):
        _translate = QtCore.QCoreApplication.translate
        vozv_tic.setWindowTitle(_translate("vozv_tic", "MainWindow"))
        self.label.setText(_translate("vozv_tic", "Введите номер билета:"))
        self.pushButton.setText(_translate("vozv_tic", "Возврат"))
        self.pushButton_2.setText(_translate("vozv_tic", "Вернуться в меню"))

