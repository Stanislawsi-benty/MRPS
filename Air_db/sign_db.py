import sqlite3 as sq
import pathlib
from pathlib import Path
from PyQt6 import QtCore

answer = ''
value = []


class CheckThread(QtCore.QThread):
    """Класс для работы с базой данных"""
    my_signal = QtCore.pyqtSignal(str)

    def thr_login(self, login, password):
        check_user(login, password, self.my_signal)
        return answer

    def thr_registration(self, data):
        sign_up(data, self.my_signal)


def sign_up(data, signal):
    """Функция регистрации в под-системе"""
    db = sq.connect(Path(pathlib.Path.home(), 'Desktop', 'МРПС', 'Programm', 'database', 'sign.db'))
    sql = db.cursor()

    sql.execute(f'''SELECT * FROM {data[0]} WHERE Login="{data[1]}";''')
    value_up = sql.fetchall()

    if value_up:
        signal.emit("Пользователь уже зарегистрирован!")

    elif not value_up:
        add_lp = f'''INSERT INTO {data[0]} (Login, Password) VALUES (?, ?);'''
        data_tuple = (data[1], data[2])
        sql.execute(add_lp, data_tuple)
        signal.emit("Вы успешно зарегистрированы! Войдите снова")

    db.commit()


def check_user(login, password, signal):
    """Функция входа в под-систему"""
    global answer, value
    tables = ['Кассир', 'Клиент', 'Админ']

    db = sq.connect(Path(pathlib.Path.home(), 'Desktop', 'МРПС', 'Programm', 'database', 'sign.db'))
    sql = db.cursor()

    for actor in tables:
        sql.execute(f'''SELECT * FROM {actor} WHERE Login=? AND Password=?;''', (login, password))
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
