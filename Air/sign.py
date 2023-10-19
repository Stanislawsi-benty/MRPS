import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from py_interfaces.sign_ui import Ui_EnterWindow
from py_interfaces.admin_ui import Ui_AdminWindow
from py_interfaces.cashier_ui import Ui_CashierWindow
from py_interfaces.client_ui import Ui_ClientWindow
from Air_db.sign_db import check_user, sign_up

app = QtWidgets.QApplication(sys.argv)

EnterWindow = QtWidgets.QMainWindow()
ui = Ui_EnterWindow()
ui.setupUi(EnterWindow)
EnterWindow.show()

data_in = []
data_up = []
switch = False


def enter():
    global data_in, switch, AdminWindow, CashierWindow, ClientWindow
    password = ui.textEdit.toPlainText()
    login = ui.textEdit_2.toPlainText()

    data_in.append(password)
    data_in.append(login)

    switch = check_user(data_in)

    if switch == 'Админ':
        AdminWindow = QtWidgets.QMainWindow()
        ui_admin = Ui_AdminWindow()
        ui_admin.setupUi(AdminWindow)
        EnterWindow.close()
        AdminWindow.show()

        def return_to_main():
            AdminWindow.close()
            EnterWindow.show()

        ui_admin.pushButton.clicked.connect(return_to_main)

    elif switch == 'Кассир':
        CashierWindow = QtWidgets.QMainWindow()
        ui_cashier = Ui_CashierWindow()
        ui_cashier.setupUi(CashierWindow)
        EnterWindow.close()
        CashierWindow.show()

        def return_to_main():
            CashierWindow.close()
            EnterWindow.show()

        ui_cashier.pushButton.clicked.connect(return_to_main)

    elif switch == 'Клиент':
        ClientWindow = QtWidgets.QMainWindow()
        ui_client = Ui_ClientWindow()
        ui_client.setupUi(ClientWindow)
        EnterWindow.close()
        ClientWindow.show()

        def return_to_main():
            ClientWindow.close()
            EnterWindow.show()

        ui_client.pushButton.clicked.connect(return_to_main)

    elif switch is False:
        ui.textBrowser.setText("Неверный логин или пароль")


def registration():
    global data_up
    password = ui.textEdit.toPlainText()
    login = ui.textEdit_2.toPlainText()
    rb1, rb2, rb3 = ui.radioButton.isChecked(), ui.radioButton_2.isChecked(), ui.radioButton_3.isChecked()

    data_up.append(password)
    data_up.append(login)

    if rb1:
        data_up.append('Кассир')
    if rb2:
        data_up.append('Клиент')
    if rb3:
        data_up.append('Админ')

    ui.textBrowser.setText("Вы зарегистрированы, войдите снова")
    sign_up(data_up)


ui.pushButton.clicked.connect(enter)
ui.pushButton_2.clicked.connect(registration)

sys.exit(app.exec())
