from os import path
import sqlite3 as sq
from operator import itemgetter


class highscore:

    def __init__(self, base_name, name=None, high='max'):
        '''
        base name: the file to store the values (it will be txt always but you can use any extension).

        name: name of the player that is currently playing (or use later as self.name = 'myname').

        high: default is max so the higher the score the better.
        '''
        self.link = sq.connect(base_name)
        self.cur = self.link.cursor()
        self.table = 'scores'
        self.name = name
        self.high = high
        self._check()

    def _check(self):
        self.cur.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        )
        if self.table in [t[0] for t in self.cur]:
            return
        else:
            self.cur.execute(
                f"CREATE TABLE {self.table} (id integer primary key autoincrement, name varchar(50), score int)"
            )

    def quarry(self):
        '''
        returns all scores from the database.

        RETURNS LIST OF TUPLES
        '''
        self.cur.execute(
            f"SELECT name, score FROM {self.table}"
        )
        result = [sc for sc in self.cur]
        if self.high == 'max':
            result.sort(key=itemgetter(1), reverse=True)
        else:
            result.sort(key=itemgetter(1))
        return result

    def new_score(self, value):
        name = str(self.name)
        if len(name) > 50:
            name = name[:50]
        self.cur.execute(
            f"INSERT INTO {self.table} (name, score) VALUES (?, ?)", (name, value)
        )
        self.link.commit()
