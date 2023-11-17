import sqlite3 as sq
import pathlib
from pathlib import Path
from PyQt6 import QtCore, QtGui, QtWidgets

answer = ''
value = []


class CheckThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def thr_login(self, login, password):
        check_user(login, password, self.mysignal)
        return answer

    def thr_registration(self, data):
        sign_up(data, self.mysignal)


def sign_up(data, signal):
    db = sq.connect(Path(pathlib.Path.home(), 'Desktop', 'МРПС', 'Programm', 'database', 'sign.db'))
    sql = db.cursor()

    sql.execute(f'''SELECT * FROM {data[0]} WHERE Login="{data[1]}";''')
    value = sql.fetchall()

    if value != []:
        signal.emit("Пользователь уже зарегистрирован!")

    elif value == []:
        add_lp = f'''INSERT INTO {data[0]} (Login, Password) VALUES (?, ?)'''
        data_tuple = (data[1], data[2])
        sql.execute(add_lp, data_tuple)
        signal.emit("Вы успешно зарегистрированы! Войдите снова")

    db.commit()


def check_user(login, password, signal):
    global answer, value
    tables = ['Кассир', 'Клиент', 'Админ']

    db = sq.connect(Path(pathlib.Path.home(), 'Desktop', 'МРПС', 'Programm', 'database', 'sign.db'))
    sql = db.cursor()

    for actor in tables:
        sql.execute(f'''SELECT * FROM {actor} WHERE Login=? AND Password=?''', (login, password))
        value = sql.fetchall()
        if value:
            break

    if value != [] and value[0][2] == password:
        signal.emit("Успешная авторизация!")
        answer = actor
    else:
        signal.emit("Неверный логин или пароль!")
        answer = ''

    db.commit()
