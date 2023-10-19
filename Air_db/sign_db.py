import sqlite3 as sq
import pathlib
from pathlib import Path

switch = False


def sign_up(data_up):
    db = sq.connect(Path(pathlib.Path.home(), 'Desktop', 'МРПС', 'Programm', 'database', 'sign.db'))
    sql = db.cursor()

    sql.execute(f'''CREATE TABLE IF NOT EXISTS {data_up[-1]} (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        Login VARCHAR(50) NOT NULL,
        Password VARCHAR(50) NOT NULL
        )''')

    add_lp = f'''INSERT INTO {data_up[-1]} (Login, Password) values (?, ?)'''
    data_tuple = (data_up[1], data_up[0])

    sql.execute(add_lp, data_tuple)
    db.commit()


def check_user(data_in):
    tables = ['Кассир', 'Клиент', 'Админ']
    user = None
    db = sq.connect(Path(pathlib.Path.home(), 'Desktop', 'МРПС', 'Programm', 'database', 'sign.db'))
    sql = db.cursor()

    for actor in tables:
        sql.execute(f'''SELECT * FROM {actor} WHERE Login=? AND Password=?''', (data_in[1], data_in[0]))

        user = sql.fetchone()

        if user is not None:
            return actor
        else:
            continue

    if user is None:
        return False

    db.close()
