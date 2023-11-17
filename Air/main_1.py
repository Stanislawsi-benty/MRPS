import sys
from PyQt6.QtWidgets import QLineEdit, QMessageBox, QInputDialog
from Air_db.sign_db import *
from Air_db.ticket_db import *
from py_interfaces.sign_ui import Ui_Form
from py_interfaces.admin_main_ui import Ui_AdminWindowMain
from py_interfaces.admin_add_ticket_ui import Ui_admin_add_ticket
from py_interfaces.client_main_ui import Ui_mainWindow
from py_interfaces.buy_ticket_ui import Ui_buy_tic
from py_interfaces.return_ticket_ui import Ui_Return_ticket_window


class EnterWindow(QtWidgets.QMainWindow, Ui_Form):
    '''Инициализация класса входа'''

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
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
            sign_window.close()
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            adminWindow.show()
        elif answer == 'Кассир':
            print("Кассир")
        elif answer == 'Клиент':
            sign_window.close()
            self.ui.lineEdit.clear()
            self.ui.lineEdit_2.clear()
            user_window.show()

    '''функция регистрации'''

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
        sign_window.show()

    def addTickets(self):
        adminWindow.close()
        admin_add_ticket.show()

    def loadTickets(self):
        self.ui.listWidget.clear()
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
            user_window.loadTickets()

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


class AdminTicket(AdminWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_admin_add_ticket()
        self.ui.setupUi(self)

        self.data_lines = [self.ui.lineEdit_from, self.ui.lineEdit_where, self.ui.lineEdit_number,
                           self.ui.lineEdit_date, self.ui.lineEdit_time, self.ui.lineEdit_price,
                           self.ui.lineEdit_quantity]

        self.ui.pushButton_return_to_adminmain.clicked.connect(self.return_to_admin_main)
        self.ui.pushButton_add_ticket.clicked.connect(self.add_ticket)
        self.ticket_db.mysignal.connect(self.signal_handler)

    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    def return_to_admin_main(self):
        admin_add_ticket.close()
        adminWindow.show()
        adminWindow.loadTickets()
        user_window.loadTickets()

    def check_input(funct):
        def wrapper(self):
            for line_edit in self.data_lines:
                if len(line_edit.text()) == 0:
                    return
            funct(self)

        return wrapper

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

    def cleaning(self):
        for i in self.data_lines:
            i.clear()


class UserMain(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        self.ticket_db = TicketSet()

        self.ui.btn_buy_ticket.clicked.connect(self.activatebuy)
        self.ui.btn_return.clicked.connect(self.to_sign)
        self.ui.btn_return_ticket.clicked.connect(self.return_ticket_window)

        self.value = []
        self.loadTickets()

    def to_sign(self):
        user_window.close()
        sign_window.show()

    def loadTickets(self):
        self.ui.listWidget.clear()
        self.value = self.ticket_db.ticket_show()
        self.ui.listWidget.addItems(
            [str(*[f"Номер рейса: {i[1]} | Откуда: {i[2]} | Куда: {i[3]} | Время вылета: {i[4]}"
                   f" | Дата вылета: {i[5]} | Цена: {i[6]} ₽ | Количество {i[7]}"]) for i in self.value])

    # открытие окна покупки билетов
    def activatebuy(self):
        currentIndex = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(currentIndex)

        if item is not None:
            BuyTicket.ticket = item.text().split('|')[:6]
            user_window.close()
            buy_window.show()

    # возврат билета
    def return_ticket_window(self):
        user_window.close()
        return_ticket_window.show()


class BuyTicket(UserMain):
    ticket = []

    def __init__(self):
        super().__init__()
        self.ui = Ui_buy_tic()
        self.ui.setupUi(self)

        self.lines_edit = [self.ui.lineEdit, self.ui.lineEdit_2, self.ui.lineEdit_3, self.ui.lineEdit_4,
                           self.ui.lineEdit_5, self.ui.lineEdit_6]

        self.ticket_db = TicketSet()
        self.ticket_db.mysignal.connect(self.signal_handler)

        self.ui.but_buy.clicked.connect(self.buyticket)
        self.ui.but_buy_2.clicked.connect(self.backmenu)

    def check_input(funct):
        def wrapper(self):
            for line_edit in self.lines_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)

        return wrapper

    # Сохрание данных в БД
    @check_input
    def buyticket(self):
        surname = self.ui.lineEdit.text()
        name = self.ui.lineEdit_2.text()
        patronymic = self.ui.lineEdit_3.text()
        gender = self.ui.box_gender.currentText()
        birthday = self.ui.dateEdit.text()
        citizenship = self.ui.lineEdit_4.text()
        passport = self.ui.lineEdit_5.text()
        phone = self.ui.lineEdit_6.text()

        data = [surname.title(), name.title(), patronymic.title(), gender, birthday, citizenship.upper(), passport,
                phone]

        self.ticket_db.purchase_ticket(data, self.ticket)
        self.cleaning()

        user_window.loadTickets()

    def signal_handler(self, value_signal):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value_signal)

    def cleaning(self):
        for i in self.lines_edit:
            i.clear()

    # Возврат в главное меню
    def backmenu(self):
        buy_window.close()
        user_window.show()

        # ___________Окно возврата билета___________#


class ReturnTicket(UserMain):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Return_ticket_window()
        self.ui.setupUi(self)

        self.lines_edit = [self.ui.lineEdit_surname, self.ui.lineEdit_name, self.ui.lineEdit_patronymic,
                           self.ui.lineEdit_flying_number, self.ui.lineEdit_from, self.ui.lineEdit_date]

        self.ui.pushButton_back.clicked.connect(self.to_main_window)
        self.ui.pushButton_return_ticket.clicked.connect(self.return_ticket)

        self.ticket_db = TicketSet()
        self.ticket_db.mysignal.connect(self.signal_handler)

    def cleaning(self):
        for i in self.lines_edit:
            i.clear()

    def signal_handler(self, value_signal):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value_signal)

    def check_input(funct):
        def wrapper(self):
            for line_edit in self.lines_edit:
                if len(line_edit.text()) == 0:
                    return
            funct(self)

        return wrapper

    def to_main_window(self):
        return_ticket_window.close()
        self.cleaning()
        user_window.show()

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

        user_window.loadTickets()
        adminWindow.loadTickets()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    sign_window = EnterWindow()  # Создание экземпляра окна входа
    adminWindow = AdminWindow()  # Создание экземпляра окна админа
    admin_add_ticket = AdminTicket()
    user_window = UserMain()
    buy_window = BuyTicket()
    return_ticket_window = ReturnTicket()
    sign_window.show()
    sys.exit(app.exec())
