# Form implementation generated from reading ui file 'C:\Users\Stanislawski\Desktop\МРПС\Programm\interfaces\admin_add_ticket.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIntValidator


class Ui_admin_add_ticket(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(864, 481)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 871, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit_from = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_from.setGeometry(QtCore.QRect(150, 40, 591, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_from.setFont(font)
        self.lineEdit_from.setStyleSheet("")
        self.lineEdit_from.setText("")
        self.lineEdit_from.setObjectName("lineEdit_from")
        self.lineEdit_where = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_where.setGeometry(QtCore.QRect(150, 100, 591, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_where.setFont(font)
        self.lineEdit_where.setObjectName("lineEdit_where")
        self.lineEdit_number = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_number.setGeometry(QtCore.QRect(150, 160, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_number.setFont(font)
        self.lineEdit_number.setMaxLength(999999999)
        self.lineEdit_number.setObjectName("lineEdit_number")
        self.lineEdit_number.setValidator(QIntValidator())
        self.lineEdit_time = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_time.setGeometry(QtCore.QRect(450, 160, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_time.setFont(font)
        self.lineEdit_time.setObjectName("lineEdit_time")
        self.lineEdit_date = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_date.setGeometry(QtCore.QRect(150, 220, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_date.setFont(font)
        self.lineEdit_date.setObjectName("lineEdit_date")
        self.lineEdit_quantity = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_quantity.setGeometry(QtCore.QRect(450, 220, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_quantity.setFont(font)
        self.lineEdit_quantity.setObjectName("lineEdit_quantity")
        self.lineEdit_quantity.setValidator(QIntValidator())
        self.lineEdit_price = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_price.setGeometry(QtCore.QRect(150, 290, 591, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_price.setFont(font)
        self.lineEdit_price.setMaxLength(999999999)
        self.lineEdit_price.setObjectName("lineEdit_price")
        self.lineEdit_price.setValidator(QIntValidator())
        self.pushButton_return_to_adminmain = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_return_to_adminmain.setGeometry(QtCore.QRect(150, 370, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_return_to_adminmain.setFont(font)
        self.pushButton_return_to_adminmain.setObjectName("pushButton_return_to_adminmain")
        self.pushButton_add_ticket = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_add_ticket.setGeometry(QtCore.QRect(450, 370, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_add_ticket.setFont(font)
        self.pushButton_add_ticket.setObjectName("pushButton_add_ticket")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 864, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавление рейса администратором"))
        self.label.setText(_translate("MainWindow", "Введите данные о новом билете:"))
        self.lineEdit_from.setPlaceholderText(_translate("MainWindow", "Откуда..."))
        self.lineEdit_where.setPlaceholderText(_translate("MainWindow", "Куда..."))
        self.lineEdit_number.setPlaceholderText(_translate("MainWindow", "Номер рейса..."))
        self.lineEdit_time.setPlaceholderText(_translate("MainWindow", "Время вылета..."))
        self.lineEdit_date.setPlaceholderText(_translate("MainWindow", "Дата вылета..."))
        self.lineEdit_quantity.setPlaceholderText(_translate("MainWindow", "Количество билетов..."))
        self.lineEdit_price.setPlaceholderText(_translate("MainWindow", "Цена..."))
        self.pushButton_return_to_adminmain.setText(_translate("MainWindow", "Вернуться в меню"))
        self.pushButton_add_ticket.setText(_translate("MainWindow", "Добавить билет"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_admin_add_ticket()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
