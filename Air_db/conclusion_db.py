import sqlite3 as sq
import pathlib
from pathlib import Path


class conclusion():
    db = sq.connect(Path(pathlib.Path.home(), 'PycharmProjects', 'MyMRPS', 'Dataset', 'ticket.db'))
    sql = db.cursor()
