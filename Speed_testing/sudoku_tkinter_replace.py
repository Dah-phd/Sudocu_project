import time
import sys

sys.setrecursionlimit(10000)


class puzzle_board():
    def __init__(self, input, name):
        self.name = name
        self.lives = 4
        self.mistakes = []
        self.input = input
        self.base = 'copy of template'
        self.save = 'used for reset'
        self.template = self.build()
        self.solve()

    def build(self):
        a = [[], [], [], [], [], [], [], [], []]
        m = 0
        for t in range(9):
            for t1 in range(9):
                try:
                    if self.input[m]['x'] == t and self.input[m]['y'] == t1:
                        a[t1].append(self.input[m]['value'])
                        m += 1
                    else:
                        a[t1].append(0)
                except IndexError:
                    a[t1].append(0)
        self.base = a.copy()
        self.save = a.copy()
        return a

    def replace(self, row, column):
        possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for t in self.template[row]:
            if t != 0:
                possible_values.remove(t)
        for t in range(0, 9):
            if self.template[t][column] != 0:
                try:
                    possible_values.remove(self.template[t][column])
                except ValueError:
                    pass
        square_x = [0, 1, 2] if row < 3 else [3, 4, 5] if row < 6 else [6, 7, 8]
        square_y = [0, 1, 2] if column < 3 else [3, 4, 5] if column < 6 else [6, 7, 8]
        for t1 in square_x:
            for t in square_y:
                if self.template[t1][t] != 0:
                    try:
                        possible_values.remove(self.template[t1][t])
                    except ValueError:
                        pass
            return possible_values

    def find_location(self):
        for t in range(9):
            for t1 in range(9):
                if self.template[t][t1] == 0:
                    return (t, t1)
        return False

    def solve(self):
        find = self.find_location()
        if not find:
            return True
        else:
            row, column = find
            for t in self.replace(row, column):
                if t:
                    self.template[row][column] = t
                    if self.solve():
                        return True
        self.template[row][column] = 0
        return False


a = [{'x': 0, 'y': 1, 'value': 2}, {'x': 0, 'y': 4, 'value': 9},
     {'x': 0, 'y': 7, 'value': 8}, {'x': 1, 'y': 0, 'value': 9},
     {'x': 1, 'y': 8, 'value': 3}, {'x': 2, 'y': 2, 'value': 3},
     {'x': 2, 'y': 4, 'value': 5}, {'x': 3, 'y': 1, 'value': 1},
     {'x': 3, 'y': 5, 'value': 7}, {'x': 3, 'y': 6, 'value': 9},
     {'x': 4, 'y': 0, 'value': 6}, {'x': 4, 'y': 5, 'value': 5},
     {'x': 4, 'y': 8, 'value': 1}, {'x': 5, 'y': 3, 'value': 9},
     {'x': 5, 'y': 6, 'value': 6}, {'x': 6, 'y': 2, 'value': 6},
     {'x': 7, 'y': 3, 'value': 6}, {'x': 8, 'y': 1, 'value': 9},
     {'x': 8, 'y': 5, 'value': 8}, {'x': 8, 'y': 7, 'value': 6}]


def timer():
    f = time.time()
    global sudoku
    sudoku = puzzle_board(a, 'dah')
    sudoku.solve()
    print(sudoku.template)
    result = time.time()-f
    print(result)


timer()
