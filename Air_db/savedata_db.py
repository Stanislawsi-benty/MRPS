import sqlite3 as sq
import pathlib
from pathlib import Path


class Save():
    def savedata(self, data):
        saveperson(data)

def saveperson(data):
    db = sq.connect(Path(pathlib.Path.home(), 'PycharmProjects', 'MyMRPS', 'Dataset', 'people.db'))
    sql = db.cursor()

    # sql.execute('''CREATE TABLE persondata (
    # surname TEXT NOT NULL,
    # name TEXT NOT NULL,
    # patronymic TEXT,
    # citizenship TEXT NOT NULL,
    # serial INTEGER NOT NULL,
    # phone INTEGER NOT NULL
    # );''')

    add = '''INSERT INTO persondata (surname, name, patronymic, citizenship, serial, phone) VALUES (?, ?, ?, ?, ?, ?);
    '''

    dat = (*data,)
    sql.execute(add, dat)


    db.commit()
