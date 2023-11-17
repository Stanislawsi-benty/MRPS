import sqlite3 as sq
import random
import pathlib
from pathlib import Path
from PyQt6 import QtCore, QtGui, QtWidgets


class TicketSet(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def ticket_add(self, ticket):
        add_ticket(ticket, self.mysignal)

    def ticket_show(self):
        value = show_tickets()
        return value

    def ticket_del(self, item):
        del_ticket(item)

    def data_change(self, ticket, text):
        change_data_ticket(ticket, text)

    def cost_change(self, ticket, cost):
        change_price_ticket(ticket, cost)

    def purchase_ticket(self, data, ticket):
        client_buy_ticket(data, ticket, self.mysignal)

    def recovery_ticket(self, information):
        client_return_ticket(information, self.mysignal)


def add_ticket(ticket, signal):
    db = sq.connect(Path(pathlib.Path.home(), 'Desktop', 'МРПС', 'Programm', 'database', 'ticket.db'))
    sql = db.cursor()

    add_ticket_into = '''INSERT INTO ticket (FLYING_NUMBER, WHERE_FROM, WHERE_TO, TIME, DATE, PRICE, QUANTITY) 
                         VALUES (?, ?, ?, ?, ?, ?, ?)'''
    data = (*ticket,)

    sql.execute(add_ticket_into, data)
    signal.emit("Билет успешно добавлен!")

    db.commit()


def show_tickets():
    db = sq.connect(Path(pathlib.Path.home(), 'Desktop', 'МРПС', 'Programm', 'database', 'ticket.db'))
    sql = db.cursor()

    sql.execute(f'''SELECT * FROM ticket;''')
    value = sql.fetchall()

    return value


def del_ticket(ticket):
    db = sq.connect(Path(pathlib.Path.home(), 'Desktop', 'МРПС', 'Programm', 'database', 'ticket.db'))
    sql = db.cursor()

    delTicket = '''DELETE FROM ticket WHERE FLYING_NUMBER =? AND PRICE =?;'''
    data = (ticket[2], ticket[19])
    sql.execute(delTicket, data)

    db.commit()


def change_data_ticket(ticket, date):
    db = sq.connect(Path(pathlib.Path.home(), 'Desktop', 'МРПС', 'Programm', 'database', 'ticket.db'))
    sql = db.cursor()
    flying_number = ticket[0].split(':')[1].strip()
    flying_date = ticket[4].split(':')[1].strip()

    change = f'''UPDATE ticket set DATE = ? where FLYING_NUMBER = ? AND DATE = ?;'''
    data = (date, flying_number, flying_date)
    sql.execute(change, data)

    db.commit()


def change_price_ticket(ticket, price):
    db = sq.connect(Path(pathlib.Path.home(), 'Desktop', 'МРПС', 'Programm', 'database', 'ticket.db'))
    sql = db.cursor()
    flying_number = ticket[0].split(':')[1].strip()
    flying_date = ticket[4].split(':')[1].strip()

    change = f'''UPDATE ticket set PRICE = ? where FLYING_NUMBER = ? AND DATE = ?;'''
    data = (price, flying_number, flying_date)
    sql.execute(change, data)

    db.commit()


def client_buy_ticket(data, ticket, signal):
    db = sq.connect(Path(pathlib.Path.home(), 'Desktop', 'МРПС', 'Programm', 'database', 'ticket.db'))
    sql = db.cursor()

    request = '''SELECT QUANTITY FROM ticket WHERE FLYING_NUMBER = ? AND TIME = ? AND DATE = ?;'''
    response = (int(ticket[0].split(':')[1]), ticket[3].split(":", 1)[1].strip(), ticket[4].split(':')[1].strip())
    sql.execute(request, response)

    value = sql.fetchone()

    if int(*value) > 0:
        buy_ticket = '''INSERT INTO sold_tickets (SURNAME, NAME, PATRONYMIC, GENDER, BIRTHDAY, CITIZENSHIP, PASSPORT, PHONE,
                    FLYING_NUMBER, WHERE_FROM, WHERE_TO, TIME, DATE, PRICE)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'''

        data_client = (*[int(i) if i.isdigit() else str(i) for i in data],
                       *[int(i.split(':', 1)[1].strip()) if i.split(':', 1)[1].strip().isdigit()
                         else str(i.split(':', 1)[1].strip()) for i in ticket[:5]],
                       int(ticket[5].split()[1]))
        sql.execute(buy_ticket, data_client)
        signal.emit("Благодарим за покупку!" + '\n' + "Приятного полета!")

        up_quantity = '''UPDATE ticket set QUANTITY = ? WHERE FLYING_NUMBER = ? AND TIME = ? AND DATE = ?;'''
        new_quantity = (int(*value, ) - 1, *response)
        sql.execute(up_quantity, new_quantity)

    else:
        signal.emit(f"К сожалению, билеты на рейс {ticket[0].split(':')[1]} раскуплены")

    db.commit()


def client_return_ticket(information, signal):
    db = sq.connect(Path(pathlib.Path.home(), 'Desktop', 'МРПС', 'Programm', 'database', 'ticket.db'))
    sql = db.cursor()

    request_ticket = '''SELECT * FROM sold_tickets WHERE SURNAME = ? AND NAME = ? AND PATRONYMIC = ? AND FLYING_NUMBER = ? AND 
                 WHERE_FROM = ? AND DATE = ?;'''
    info_1 = (*information,)

    sql.execute(request_ticket, info_1)
    value_ticket = sql.fetchall()

    if value_ticket:
        delete = '''DELETE FROM sold_tickets WHERE SURNAME = ? AND NAME = ? AND PATRONYMIC = ? AND FLYING_NUMBER = ? AND
                    WHERE_FROM = ? AND DATE = ?;'''
        info = (*information,)
        sql.execute(delete, info)

        request_quantity = '''SELECT QUANTITY FROM ticket WHERE FLYING_NUMBER = ? AND WHERE_FROM = ? AND DATE = ?;'''
        response_quantity = (*information[3:],)
        sql.execute(request_quantity, response_quantity)
        value_quantity = sql.fetchone()

        up_quantity = '''UPDATE ticket set QUANTITY = ? WHERE FLYING_NUMBER = ? AND WHERE_FROM = ? AND DATE = ?;'''
        new_quantity = (int(*value_quantity, ) + 1, *information[3:])
        sql.execute(up_quantity, new_quantity)

        signal.emit("Данный билет возвращен!" + '\n' + '\n' + "Деньги поступят на Ваш счет в течение 7 дней")

    else:
        signal.emit("Вы не приобретали данный билет")

    db.commit()


# def start():
#     db = sq.connect(Path(pathlib.Path.home(), 'Desktop', 'МРПС', 'Programm', 'database', 'ticket.db'))
#     sql = db.cursor()
#
#     sql.execute('''CREATE TABLE ticket (
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     FLYING_NUMBER INTEGER NOT NULL,
#     WHERE_FROM TEXT NOT NULL,
#     WHERE_TO TEXT NOT NULL,
#     TIME TEXT NOT NULL,
#     DATE TEXT NOT NULL,
#     PRICE INTEGER NOT NULL,
#     QUANTITY INTEGER NOT NULL
#     );''')
#
#     db.commit()

# def start():
#     db = sq.connect(Path(pathlib.Path.home(), 'Desktop', 'МРПС', 'Programm', 'database', 'ticket.db'))
#     sql = db.cursor()
#
#     sql.execute('''CREATE TABLE sold_tickets (
#     ID INTEGER PRIMARY KEY AUTOINCREMENT,
#     SURNAME TEXT NOT NULL,
#     NAME TEXT NOT NULL,
#     PATRONYMIC TEXT NOT NULL,
#     GENDER TEXT NOT NULL,
#     BIRTHDAY TEXT NOT NULL,
#     CITIZENSHIP TEXT NOT NULL,
#     PASSPORT INTEGER NOT NULL,
#     PHONE INTEGER NOT NULL,
#     FLYING_NUMBER INTEGER NOT NULL,
#     WHERE_FROM TEXT NOT NULL,
#     WHERE_TO TEXT NOT NULL,
#     TIME TEXT NOT NULL,
#     DATE TEXT NOT NULL,
#     PRICE INTEGER NOT NULL
#     );''')
#
#     db.commit()

# if __name__ == '__main__':
#     client_buy_ticket(1, 2, 3)
