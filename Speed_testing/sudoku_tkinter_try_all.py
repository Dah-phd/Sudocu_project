import time


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

    def replace(self, val, row, column):
        for t in range(9):
            if self.template[t][column] == val and t != row:
                return False
        for t in range(9):
            if self.template[row][t] == val and t != column:
                return False
        square_x = [0, 1, 2] if row < 3 else [
            3, 4, 5] if row < 6 else [6, 7, 8]
        square_y = [0, 1, 2] if column < 3 else [
            3, 4, 5] if column < 6 else [6, 7, 8]
        for t in square_x:
            for t1 in square_y:
                if self.template[t][t1] == val and (t, t1) != (row, column):
                    return False
        return True

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
        for t in range(1, 10):
            if self.replace(t, row, column):
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
    f = time.time()-f
    print(f)


timer()
