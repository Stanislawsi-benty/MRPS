# Form implementation generated from reading ui file 'C:\Users\Stanislawski\Desktop\МРПС\Programm\interfaces\Return_ticket.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIntValidator


class Ui_Return_ticket_window(object):
    def setupUi(self, Return_ticket_window):
        Return_ticket_window.setObjectName("Return_ticket_window")
        Return_ticket_window.resize(791, 426)
        self.centralwidget = QtWidgets.QWidget(parent=Return_ticket_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 781, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit_surname = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_surname.setGeometry(QtCore.QRect(90, 70, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_surname.setFont(font)
        self.lineEdit_surname.setText("")
        self.lineEdit_surname.setObjectName("lineEdit_Surname")
        self.lineEdit_name = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(90, 130, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setText("")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_patronymic = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_patronymic.setGeometry(QtCore.QRect(90, 190, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_patronymic.setFont(font)
        self.lineEdit_patronymic.setText("")
        self.lineEdit_patronymic.setObjectName("lineEdit_patronymic")
        self.lineEdit_flying_number = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_flying_number.setGeometry(QtCore.QRect(400, 70, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_flying_number.setFont(font)
        self.lineEdit_flying_number.setText("")
        self.lineEdit_flying_number.setObjectName("lineEdit_flying_number")
        self.lineEdit_flying_number.setValidator(QIntValidator())
        self.lineEdit_from = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_from.setGeometry(QtCore.QRect(400, 130, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_from.setFont(font)
        self.lineEdit_from.setText("")
        self.lineEdit_from.setObjectName("lineEdit_from")
        self.lineEdit_date = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_date.setGeometry(QtCore.QRect(400, 190, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_date.setFont(font)
        self.lineEdit_date.setText("")
        self.lineEdit_date.setObjectName("lineEdit_date")
        self.pushButton_back = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_back.setGeometry(QtCore.QRect(160, 310, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_back.setFont(font)
        self.pushButton_back.setObjectName("pushButton_back")
        self.pushButton_return_ticket = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_return_ticket.setGeometry(QtCore.QRect(400, 310, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_return_ticket.setFont(font)
        self.pushButton_return_ticket.setObjectName("pushButton_return_ticket")
        Return_ticket_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Return_ticket_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 791, 21))
        self.menubar.setObjectName("menubar")
        Return_ticket_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Return_ticket_window)
        self.statusbar.setObjectName("statusbar")
        Return_ticket_window.setStatusBar(self.statusbar)

        self.retranslateUi(Return_ticket_window)
        QtCore.QMetaObject.connectSlotsByName(Return_ticket_window)

    def retranslateUi(self, Return_ticket_window):
        _translate = QtCore.QCoreApplication.translate
        Return_ticket_window.setWindowTitle(_translate("Return_ticket_window", "Возврат билета"))
        self.label.setText(_translate("Return_ticket_window", "Введите данные для возврата билета:"))
        self.lineEdit_surname.setPlaceholderText(_translate("Return_ticket_window", "Фамилия..."))
        self.lineEdit_name.setPlaceholderText(_translate("Return_ticket_window", "Имя..."))
        self.lineEdit_patronymic.setPlaceholderText(_translate("Return_ticket_window", "Отчество..."))
        self.lineEdit_flying_number.setPlaceholderText(_translate("Return_ticket_window", "Номер рейса..."))
        self.lineEdit_from.setPlaceholderText(_translate("Return_ticket_window", "Откуда..."))
        self.lineEdit_date.setPlaceholderText(_translate("Return_ticket_window", "Дата вылета..."))
        self.pushButton_back.setText(_translate("Return_ticket_window", "Назад"))
        self.pushButton_return_ticket.setText(_translate("Return_ticket_window", "Вернуть билет"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Return_ticket_window = QtWidgets.QMainWindow()
    ui = Ui_Return_ticket_window()
    ui.setupUi(Return_ticket_window)
    Return_ticket_window.show()
    sys.exit(app.exec())
