import sqlite3 as sq
import pathlib
from pathlib import Path


class Save():
    def saveperson(self, data):
        tablecreate(data)


def tablecreate():
    db = sq.connect(Path('C:', 'Users', 'nik-a', 'Onedrive', 'Рабочий стол', 'MIIT', 'МРПС', 'ANDR_MRPS', 'Dataset', 'dsave.db'))
    sql = db.cursor()

    sql.execute("""CREATE TABLE persondata (
    surname TEXT NOT NULL,
    name TEXT NOT NULL,
    patronymic TEXT,
    citizenship TEXT NOT NULL,
    serial INTEGER NOT NULL,
    phone INTEGER NOT NULL
    );""")

    # add = """INSERT INTO persondata (surname, name, patronymic, citizenship, serial, phone)
    #  VALUES (?, ?, ?, ?, ?, ?)
    #  """
    #
    # dat = (*data,)
    # sql.execute(add, dat)

    db.commit()

if __name__ == '__main__':
    tablecreate()