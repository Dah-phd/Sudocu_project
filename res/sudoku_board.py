import requests
import json


class request_tmp:
    def __init__(self, difficulty=2):
        self.difficulty = difficulty
        self._requesttemplate()
        self._build()

    def _requesttemplate(self):
        try:
            self.connection = False
            layout = {'size': 9, 'level': self.difficulty}
            r = requests.get('http://www.cs.utep.edu/cheon/ws/sudoku/new/',
                             params=layout, timeout=3)
            r = r.json()
            self.fields = r['squares']
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            self.connection = False
            with open('oftemp.json', 'r') as f:
                self.fields = json.load(f)

    def _build(self):
        self.board = [[], [], [], [], [], [], [], [], []]
        m = 0
        for t in range(9):
            for t1 in range(9):
                try:
                    if self.fields[m]['x'] == t and self.fields[m]['y'] == t1:
                        self.board[t1].append(self.fields[m]['value'])
                        m += 1
                    else:
                        self.board[t1].append(0)
                except IndexError:
                    print(len(self.fields))
                    self.board[t1].append(0)
