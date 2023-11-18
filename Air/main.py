import sys
from typing import Callable
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QLineEdit, QMessageBox, QInputDialog
from Air_db.sign_db import *
from Air_db.ticket_db import *
from py_interfaces.sign_ui import Ui_Form
from py_interfaces.admin_main_ui import Ui_AdminWindowMain
from py_interfaces.admin_add_ticket_ui import Ui_admin_add_ticket
from py_interfaces.client_main_ui import Ui_mainWindow
from py_interfaces.buy_ticket_ui import Ui_buy_tic
from py_interfaces.return_ticket_ui import Ui_Return_ticket_window
from py_interfaces.cashier_main_ui import Ui_CashierMainWindow


class EnterWindow(QtWidgets.QMainWindow, Ui_Form):
    """Инициализация класса входа"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.auth)
        self.ui.pushButton_2.clicked.connect(self.reg)
        self.radio_button = [self.ui.radioButton, self.ui.radioButton_2, self.ui.radioButton_3]
        self.radio_group = QtWidgets.QButtonGroup(self)
        self.radio_group.addButton(self.ui.radioButton)
        self.radio_group.addButton(self.ui.radioButton_2)
        self.radio_group.addButton(self.ui.radioButton_3)
        self.base_line_edit = [self.ui.lineEdit, self.ui.lineEdit_2]
        self.ui.lineEdit_2.setEchoMode(QLineEdit.EchoMode.Password)

        self.sign_db = CheckThread()
        self.sign_db.my_signal.connect(self.signal_handler)

    '''Функция очистки полей в окне входа и радио кнопок'''
    def cleaning_sign(self, actor):
        for i in self.base_line_edit:
            i.clear()

        self.radio_group.setExclusive(False)
        if actor == "Админ":
            self.ui.radioButton.setChecked(False)
        if actor == "Кассир":
            self.ui.radioButton_2.setChecked(False)
        if actor == "Клиент":
            self.ui.radioButton_3.setChecked(False)
        self.radio_group.setExclusive(True)

    '''Функция проверки есть ли символы в полях логина и пароля'''
    def check_input(funct: Callable):
        def wrapper(self):
            for line_edit in self.base_line_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)

        return wrapper

    '''Возвращает сигнал(окно) после авторизации и регистрации'''
    def signal_handler(self, value_sign):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value_sign)

    '''Функция авторизации'''
    @check_input
    def auth(self):
        login = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        answer_db = self.sign_db.thr_login(login, password)

        if answer_db == 'Админ':
            sign_window.close()
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            admin_window_main.show()
        elif answer_db == 'Кассир':
            sign_window.close()
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            cashier_window_main.show()
        elif answer_db == 'Клиент':
            sign_window.close()
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            user_window_main.show()

    '''Функция регистрации'''
    @check_input
    def reg(self):
        login = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        data = [i.text() for i in self.radio_button if i.isChecked()]
        if data:
            data.append(login)
            data.append(password)
            self.sign_db.thr_registration(data)
        else:
            return
        self.cleaning_sign(data[0])


class AdminWindow(QtWidgets.QMainWindow):
    """Инициализация класса админа"""
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

    '''Загрузка рейсов в список'''
    def loadTickets(self):
        self.ui.listWidget.clearSelection()
        self.ui.listWidget.clear()
        self.value = self.ticket_db.ticket_show()
        self.ui.listWidget.addItems(
            [str(*[f"Номер рейса: {i[1]} | Откуда: {i[2]} | Куда: {i[3]} | Время вылета: {i[4]}"
                   f" | Дата вылета: {i[5]} | Цена: {i[6]} ₽ | Количество: {i[7]}"]) for i in self.value])

    '''Функция выхода в окно входа'''
    @staticmethod
    def to_sign():
        admin_window_main.close()
        sign_window.show()

    '''Функция входа в окно добавления рейса'''
    @staticmethod
    def addTickets():
        admin_window_main.close()
        admin_add_ticket.show()

    '''Функция удаления рейса'''
    def delTicket(self):
        current_index = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(current_index)
        if item is None:
            return

        question = QMessageBox.question(self, "Удаление билета", "Хотите удалить билет: " + '\n' + item.text() + '?')

        if question == QMessageBox.StandardButton.Yes:
            item = self.ui.listWidget.takeItem(current_index)
            self.ticket_db.ticket_del(item.text().split())
            user_window_main.loadTickets()
            cashier_window_main.loadTickets()

    '''Функция изменение даты вылета в рейсе'''
    def change_date(self):
        currentIndex = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(currentIndex)

        if item is not None:
            text, ok = QInputDialog.getText(self, "Изменить дату рейса", "Введите дату:")
            if text and ok is not None:
                self.ticket_db.data_change(item.text().split('|'), text)

        self.ui.listWidget.clear()
        self.loadTickets()
        user_window_main.loadTickets()
        cashier_window_main.loadTickets()

    '''Функция изменение цены в рейсе'''
    def change_price(self):
        currentIndex = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(currentIndex)

        if item is not None:
            price, ok = QInputDialog.getInt(self, "Изменить цену рейса", "Введите цену:")
            if price and ok is not None:
                self.ticket_db.cost_change(item.text().split('|'), price)

        self.ui.listWidget.clear()
        self.loadTickets()
        user_window_main.loadTickets()
        cashier_window_main.loadTickets()


class AdminTicket(AdminWindow):
    """Инициализация класса Админа для добавления билета"""
    def __init__(self):
        super().__init__()
        self.ui = Ui_admin_add_ticket()
        self.ui.setupUi(self)

        self.data_lines = [self.ui.lineEdit_from, self.ui.lineEdit_where, self.ui.lineEdit_number,
                           self.ui.lineEdit_date, self.ui.lineEdit_time, self.ui.lineEdit_price,
                           self.ui.lineEdit_quantity]

        self.ui.pushButton_return_to_adminmain.clicked.connect(self.return_to_admin_main)
        self.ui.pushButton_add_ticket.clicked.connect(self.add_ticket)
        self.ticket_db.my_signal.connect(self.signal_handler)

    '''Функция очистки полей'''
    def cleaning(self):
        for i in self.data_lines:
            i.clear()

    '''Возвращает сигнал(окно) с сообщением'''
    def signal_handler(self, value_admin_ticket):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value_admin_ticket)

    '''Функция возврата в главное окно админа'''
    def return_to_admin_main(self):
        admin_add_ticket.close()
        self.cleaning()
        admin_window_main.show()
        admin_window_main.loadTickets()
        user_window_main.loadTickets()
        cashier_window_main.loadTickets()

    '''Функция проверки есть ли символы в полях'''
    def check_input(funct: Callable):
        def wrapper(self):
            for line_edit in self.data_lines:
                if len(line_edit.text()) == 0:
                    return
            funct(self)

        return wrapper

    '''Функция добавления билета'''
    @check_input
    def add_ticket(self):
        where = self.ui.lineEdit_where.text()
        from_ = self.ui.lineEdit_from.text()
        number = self.ui.lineEdit_number.text()
        time = self.ui.lineEdit_time.text()
        date = self.ui.lineEdit_date.text()
        quantity = self.ui.lineEdit_quantity.text()
        price = self.ui.lineEdit_price.text()

        ticket = [number, from_, where, time, date, price, quantity]
        self.ticket_db.ticket_add(ticket)
        self.cleaning()


class UserMain(QtWidgets.QMainWindow):
    """Инициализация класса главного окна клиента"""
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.ticket_db = TicketSet()

        self.ui.btn_buy_ticket.clicked.connect(self.activate_buy_user)
        self.ui.btn_return.clicked.connect(self.to_sign)
        self.ui.btn_return_ticket.clicked.connect(self.return_ticket_window)

        self.value = []
        self.loadTickets()

    '''Функция возврата в окно входа'''
    @staticmethod
    def to_sign():
        user_window_main.close()
        sign_window.show()

    '''Функция возврата в окно входа'''
    def loadTickets(self):
        self.ui.listWidget.clearSelection()
        self.ui.listWidget.clear()
        self.value = self.ticket_db.ticket_show()
        self.ui.listWidget.addItems(
            [str(*[f"Номер рейса: {i[1]} | Откуда: {i[2]} | Куда: {i[3]} | Время вылета: {i[4]}"
                   f" | Дата вылета: {i[5]} | Цена: {i[6]} ₽ | Количество: {i[7]}"]) for i in self.value])

    '''Функция перехода в окно покупки билетов'''
    def activate_buy_user(self):
        currentIndex = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(currentIndex)

        if item is not None:
            BuyTicketUser.ticket = item.text().split('|')[:6]
            user_window_main.close()
            buy_window_user.show()

    '''Функция перехода в окно возврата билета билетов'''
    @staticmethod
    def return_ticket_window():
        user_window_main.close()
        return_ticket_window_user.show()


class BuyTicketUser(UserMain):
    """Инициализация класса окна покупки от клиента"""
    ticket = []

    def __init__(self):
        super().__init__()
        self.ui = Ui_buy_tic()
        self.ui.setupUi(self)

        self.lines_edit = [self.ui.lineEdit, self.ui.lineEdit_2, self.ui.lineEdit_3, self.ui.lineEdit_4,
                           self.ui.lineEdit_5, self.ui.lineEdit_6]

        self.ticket_db = TicketSet()
        self.ticket_db.my_signal.connect(self.signal_handler)

        self.ui.but_buy.clicked.connect(self.buy_ticket_user)
        self.ui.but_buy_2.clicked.connect(self.back_user_main)

    '''Возвращает сигнал(окно) с сообщением'''
    def signal_handler(self, value_signal):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value_signal)

    '''Функция проверки есть ли символы в полях'''
    def check_input(funct: Callable):
        def wrapper(self):
            for line_edit in self.lines_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)

        return wrapper

    '''Функция очистки полей'''
    def cleaning(self):
        for i in self.lines_edit:
            i.clear()

    '''Функция возврата в главное окно клиента'''
    def back_user_main(self):
        buy_window_user.close()
        user_window_main.loadTickets()
        self.cleaning()
        user_window_main.show()

    '''Функция покупки билета через клиента'''
    @check_input
    def buy_ticket_user(self):
        surname = self.ui.lineEdit.text().title()
        name = self.ui.lineEdit_2.text().title()
        patronymic = self.ui.lineEdit_3.text().title()
        gender = self.ui.box_gender.currentText()
        birthday = self.ui.dateEdit.text()
        citizenship = self.ui.lineEdit_4.text().upper()
        passport = self.ui.lineEdit_5.text()
        phone = self.ui.lineEdit_6.text()

        data = [surname, name, patronymic, gender, birthday, citizenship, passport, phone]

        self.ticket_db.purchase_ticket(data, self.ticket)
        self.cleaning()

        user_window_main.loadTickets()
        admin_window_main.loadTickets()
        cashier_window_main.loadTickets()


class ReturnTicketUser(UserMain):
    """Инициализация класса окна возврата билета от клиента"""
    def __init__(self):
        super().__init__()
        self.ui = Ui_Return_ticket_window()
        self.ui.setupUi(self)

        self.lines_edit = [self.ui.lineEdit_surname, self.ui.lineEdit_name, self.ui.lineEdit_patronymic,
                           self.ui.lineEdit_flying_number, self.ui.lineEdit_from, self.ui.lineEdit_date]

        self.ui.pushButton_back.clicked.connect(self.to_main_window)
        self.ui.pushButton_return_ticket.clicked.connect(self.return_ticket)

        self.ticket_db = TicketSet()
        self.ticket_db.my_signal.connect(self.signal_handler)

    '''Функция очистки полей'''
    def cleaning(self):
        for i in self.lines_edit:
            i.clear()

    '''Функция сигнала(окна)'''
    def signal_handler(self, value_signal):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value_signal)

    '''Функция проверки символов в полях'''
    def check_input(funct: Callable):
        def wrapper(self):
            for line_edit in self.lines_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)

        return wrapper

    '''Функция возврата в главное окно клиента'''
    def to_main_window(self):
        return_ticket_window_user.close()
        self.cleaning()
        user_window_main.show()

    '''Функция возврата билета от клиента'''
    @check_input
    def return_ticket(self):
        surname = self.ui.lineEdit_surname.text().title()
        name = self.ui.lineEdit_name.text().title()
        patronymic = self.ui.lineEdit_patronymic.text().title()
        flying_number = int(self.ui.lineEdit_flying_number.text())
        from_city = self.ui.lineEdit_from.text().title()
        date = self.ui.lineEdit_date.text()

        information = [surname, name, patronymic, flying_number, from_city, date]

        self.ticket_db.recovery_ticket(information)
        self.cleaning()

        user_window_main.loadTickets()
        admin_window_main.loadTickets()
        cashier_window_main.loadTickets()


class CashierMain(QtWidgets.QMainWindow):
    """Инициализация класса главного окна кассира"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CashierMainWindow()
        self.ui.setupUi(self)

        self.ui.pushbutton_to_sign.clicked.connect(self.to_sign)
        self.ui.pushbutton_cashier_buy_ticket.clicked.connect(self.activate_buy_cashier)
        self.ui.pushbutton_return_cashier_ticket.clicked.connect(self.return_ticket_window)
        self.ui.pushbutton_revenue.clicked.connect(self.revenue)

        self.ticket_db = TicketSet()
        self.ticket_db.my_signal.connect(self.signal_handler)

        self.value = []
        self.loadTickets()

    '''Функция загрузки билетов в окно кассира'''
    def loadTickets(self):
        self.ui.listWidget.clearSelection()
        self.ui.listWidget.clear()
        self.value = self.ticket_db.ticket_show()
        self.ui.listWidget.addItems(
            [str(*[f"Номер рейса: {i[1]} | Откуда: {i[2]} | Куда: {i[3]} | Время вылета: {i[4]}"
                   f" | Дата вылета: {i[5]} | Цена: {i[6]} ₽ | Количество: {i[7]}"]) for i in self.value])

    '''Функция возврата в окно входа'''
    @staticmethod
    def to_sign():
        cashier_window_main.close()
        sign_window.show()

    '''Функция сигнала(окна) о событии'''
    def signal_handler(self, value_signal):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value_signal)

    '''Функция открытия окна покупки билета от кассира'''
    def activate_buy_cashier(self):
        currentIndex = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(currentIndex)

        if item is not None:
            BuyTicketCashier.ticket = item.text().split('|')[:6]
            cashier_window_main.close()
            buy_window_cashier.show()

    '''Функция открытия окна возврата билета от кассира'''
    @staticmethod
    def return_ticket_window():
        cashier_window_main.close()
        return_ticket_window_cashier.show()

    '''Функция подсчета дневной выручки'''
    def revenue(self):
        self.ticket_db.cashier_revenue()


class BuyTicketCashier(CashierMain):
    """Инициализация класса окна покупки билета от кассира"""
    ticket = []

    def __init__(self):
        super().__init__()
        self.ui = Ui_buy_tic()
        self.ui.setupUi(self)

        self.lines_edit = [self.ui.lineEdit, self.ui.lineEdit_2, self.ui.lineEdit_3, self.ui.lineEdit_4,
                           self.ui.lineEdit_5, self.ui.lineEdit_6]

        self.ticket_db = TicketSet()
        self.ticket_db.my_signal.connect(self.signal_handler)

        self.ui.but_buy.clicked.connect(self.buy_ticket_cashier)
        self.ui.but_buy_2.clicked.connect(self.back_cashier_main)

    '''Функция возврата сигнала(окна)'''
    def signal_handler(self, value_signal):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value_signal)

    '''Функция очистки полей'''
    def cleaning(self):
        for i in self.lines_edit:
            i.clear()

    '''Функция проверки символов в полях'''
    def check_input(funct: Callable):
        def wrapper(self):
            for line_edit in self.lines_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)

        return wrapper

    '''Функция покупки билета от кассира'''
    @check_input
    def buy_ticket_cashier(self):
        surname = self.ui.lineEdit.text().title()
        name = self.ui.lineEdit_2.text().title()
        patronymic = self.ui.lineEdit_3.text().title()
        gender = self.ui.box_gender.currentText()
        birthday = self.ui.dateEdit.text()
        citizenship = self.ui.lineEdit_4.text().upper()
        passport = self.ui.lineEdit_5.text()
        phone = self.ui.lineEdit_6.text()

        data = [surname, name, patronymic, gender, birthday, citizenship, passport, phone]

        self.ticket_db.purchase_ticket(data, self.ticket)
        self.cleaning()

        user_window_main.loadTickets()
        admin_window_main.loadTickets()
        cashier_window_main.loadTickets()

    '''Функция возврата в главное окно кассира'''
    def back_cashier_main(self):
        buy_window_cashier.close()
        cashier_window_main.loadTickets()
        self.cleaning()
        cashier_window_main.show()


class ReturnTicketCashier(CashierMain):
    """Инициализация класса окна возврата билета от кассира"""
    def __init__(self):
        super().__init__()
        self.ui = Ui_Return_ticket_window()
        self.ui.setupUi(self)

        self.lines_edit = [self.ui.lineEdit_surname, self.ui.lineEdit_name, self.ui.lineEdit_patronymic,
                           self.ui.lineEdit_flying_number, self.ui.lineEdit_from, self.ui.lineEdit_date]

        self.ui.pushButton_back.clicked.connect(self.to_main_window)
        self.ui.pushButton_return_ticket.clicked.connect(self.return_ticket)

        self.ticket_db = TicketSet()
        self.ticket_db.my_signal.connect(self.signal_handler)

    '''Функция очистки полей'''
    def cleaning(self):
        for i in self.lines_edit:
            i.clear()

    '''Функция возврата сигнала(окна)'''
    def signal_handler(self, value_signal):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value_signal)

    '''Функция проверки наличия символов в полях'''
    def check_input(funct: Callable):
        def wrapper(self):
            for line_edit in self.lines_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)

        return wrapper

    '''Функция возврата в главное окно кассира'''
    def to_main_window(self):
        return_ticket_window_cashier.close()
        self.cleaning()
        cashier_window_main.show()

    '''Функция возврата билета от кассира'''
    @check_input
    def return_ticket(self):
        surname = self.ui.lineEdit_surname.text().title()
        name = self.ui.lineEdit_name.text().title()
        patronymic = self.ui.lineEdit_patronymic.text().title()
        flying_number = self.ui.lineEdit_flying_number.text()
        from_city = self.ui.lineEdit_from.text().title()
        date = self.ui.lineEdit_date.text()

        information = [surname, name, patronymic, int(flying_number), from_city, date]

        self.ticket_db.recovery_ticket(information)
        self.cleaning()

        user_window_main.loadTickets()
        admin_window_main.loadTickets()
        cashier_window_main.loadTickets()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    sign_window = EnterWindow()  # Создание экземпляра окна входа
    admin_window_main = AdminWindow()  # Создание экземпляра окна админа
    admin_add_ticket = AdminTicket()  # Создание экземпляра окна создания билета от админа
    user_window_main = UserMain()  # Создание экземпляра главного окна клиента
    buy_window_user = BuyTicketUser()  # Создание экземпляра окна покупки билета от клиента
    return_ticket_window_user = ReturnTicketUser()  # Создание экземпляра окна возврата билета от клиента
    cashier_window_main = CashierMain()  # Создание экземпляра главного окна кассира
    buy_window_cashier = BuyTicketCashier()  # Создание экземпляра окна покупки билета от кассира
    return_ticket_window_cashier = ReturnTicketCashier()  # Создание экземпляра окна возврата билета от кассира
    sign_window.show()
    sys.exit(app.exec())
