import sys
from PyQt6.QtWidgets import QLineEdit
from Air_db.sign_db import *
from py_interfaces.sign_ui import Ui_Enter
from py_interfaces.admin_main_ui import Ui_AdminWindowMain


class EnterWindow(QtWidgets.QMainWindow, Ui_Enter):
    '''Инициализация класса входа'''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Enter()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.auth)
        self.ui.pushButton_2.clicked.connect(self.reg)
        self.radio_button = [self.ui.radioButton, self.ui.radioButton_2, self.ui.radioButton_3]
        self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2]
        self.ui.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)

        self.sign_db = CheckThread()
        self.sign_db.mysignal.connect(self.signal_handler)

    '''функция проверки есть ли символы в полях логина и пароля'''
    def check_input(funct):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)

        return wrapper

    '''Возвращает сигнал(окно) после авторизации и регистрации'''
    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    '''функция авторизации'''
    @check_input
    def auth(self):
        login = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        answer = self.sign_db.thr_login(login, password)
        if answer == 'Админ':
            signwindow.close()
            adminWindow.show()
        elif answer == 'Кассир':
            print("Кассир")
        elif answer == 'Клиент':
            print("Клиент")

    '''функция регистрации'''
    @check_input
    def reg(self):
        login = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        data = [i.text() for i in self.radio_button if i.isChecked()]
        data.append(login)
        data.append(password)
        self.sign_db.thr_registration(data)


class AdminWindow(QtWidgets.QMainWindow):
    '''Инициализация класса вдмина'''
    def __init__(self):
        super().__init__()
        self.ui = Ui_AdminWindowMain()
        self.ui.setupUi(self)

        self.ui.pushButton_add.clicked.connect(self.to_sign)

    '''Функция выхода в окно входа'''
    def to_sign(self):
        adminWindow.close()
        signwindow.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    signwindow = EnterWindow()  # Создание экземпляра окна входа
    adminWindow = AdminWindow()  # Создание экземпляра окна админа
    signwindow.show()
    sys.exit(app.exec())
