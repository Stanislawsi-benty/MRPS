import sqlite3 as sq
import random
import pathlib
from pathlib import Path


class TicketSet():
    def ticket_add(self):
        add_ticket()

    def ticket_show(self):
        value = show_tickets()
        return value

    def ticket_del(self, item):
        del_ticket(item)

    def data_change(self, ticket, text):
        change_data_ticket(ticket, text)

    def cost_change(self, ticket, cost):
        change_price_ticket(ticket, cost)


def add_ticket():
    where_from = ['Нью-Йорк', 'Париж', 'Лондон', 'Токио', 'Бангкок', 'Рим', 'Барселона', 'Дубай', 'Сингапур',
                  'Истанбул']
    where_to = ['Пекин', 'Сидней', 'Рио-де-Жанейро', 'Кейптаун', 'Москва', 'Берлин', 'Киев', 'Киото', 'Прага',
                'Марракеш', ]

    db = sq.connect(Path(pathlib.Path.home(), 'Desktop', 'МРПС', 'Programm', 'database', 'ticket.db'))
    sql = db.cursor()

    ticket = '''INSERT INTO ticket (FLYING_NUMBER, WHERE_FROM, WHERE_TO, TIME, DATE, PRICE, QUANTITY) 
                VALUES (?, ?, ?, ?, ?, ?, ?)'''
    data = (random.randint(1, 100),
            random.choice(where_from),
            random.choice(where_to),
            '{:02}:{:02}'.format(random.randint(0, 23), random.randint(0, 59)),
            '{:02}.{:02}'.format(random.randint(1, 31), random.randint(1, 12)),
            random.randint(10000, 1000000),
            random.randint(1, 20)
            )

    sql.execute(ticket, data)

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
