import sys
from PyQt6.QtWidgets import QLineEdit, QMessageBox, QInputDialog
from Air_db.sign_db import *
from Air_db.ticket_db import *
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
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
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

        self.ui.pushButton_exit.clicked.connect(self.to_sign)
        self.ui.pushButton_add.clicked.connect(self.addTickets)
        self.ui.pushButton_del.clicked.connect(self.delTicket)
        self.ui.pushButton_date.clicked.connect(self.change_date)
        self.ui.pushButton_cost.clicked.connect(self.change_price)

        self.ticket_db = TicketSet()

        self.value = []
        self.loadTickets()

    '''Функция выхода в окно входа'''

    def to_sign(self):
        adminWindow.close()
        signwindow.show()

    def addTickets(self):
        self.ticket_db.ticket_add()
        self.ui.listWidget.clear()
        self.loadTickets()

    def loadTickets(self):
        self.value = self.ticket_db.ticket_show()
        self.ui.listWidget.addItems(
            [str(*[f"Номер рейса: {i[1]} | Откуда: {i[2]} | Куда: {i[3]} | Время вылета: {i[4]}"
                   f" | Дата вылета: {i[5]} | Цена: {i[6]} ₽ | Количество {i[7]}"]) for i in self.value])

    def delTicket(self):
        currentIndex = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(currentIndex)
        if item is None:
            return

        question = QMessageBox.question(self, "Удаление билета", "Хотите удалить билет: " + '\n' + item.text() + '?')

        if question == QMessageBox.StandardButton.Yes:
            item = self.ui.listWidget.takeItem(currentIndex)
            self.ticket_db.ticket_del(item.text().split())

    def change_date(self):
        currentIndex = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(currentIndex)

        if item is not None:
            text, ok = QInputDialog.getText(self, "Изменить дату рейса", "Введите дату:")
            if text and ok is not None:
                self.ticket_db.data_change(item.text().split('|'), text)

        self.ui.listWidget.clear()
        self.loadTickets()

    def change_price(self):
        currentIndex = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(currentIndex)

        if item is not None:
            price, ok = QInputDialog.getInt(self, "Изменить цену рейса", "Введите цену:")
            if price and ok is not None:
                self.ticket_db.cost_change(item.text().split('|'), price)

        self.ui.listWidget.clear()
        self.loadTickets()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    signwindow = EnterWindow()  # Создание экземпляра окна входа
    adminWindow = AdminWindow()  # Создание экземпляра окна админа
    signwindow.show()
    sys.exit(app.exec())
