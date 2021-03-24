class sudoku:
    def __init__(self, board):
        self.board = board
        self.template = [row.copy() for row in board]
        self._solve()

    def _check(self, val, row, column):
        for row_ in range(9):
            if self.template[row_][column] == val and row_ != row:
                return False
        for column_ in range(9):
            if self.template[row][column_] == val and column_ != column:
                return False
        square_x = [0, 1, 2] if row < 3 else [
            3, 4, 5] if row < 6 else [6, 7, 8]
        square_y = [0, 1, 2] if column < 3 else [
            3, 4, 5] if column < 6 else [6, 7, 8]
        for row_ in square_x:
            for column_ in square_y:
                if self.template[row_][column_] == val and (row_, column_) != (row, column):
                    return False
        return True

    def _find_location(self):
        for row in range(9):
            for square in range(9):
                if self.template[row][square] == 0:
                    return (row, square)
        return False

    def _solve(self):
        find = self._find_location()
        if not find:
            return True
        for t in range(1, 10):
            if self._check(t, find[0], find[1]):
                self.template[find[0]][find[1]] = t
                if self._solve():
                    return True
        self.template[find[0]][find[1]] = 0
        return False

    def is_correct(self, val, x, y):
        if val == self.template[x][y]:
            self.board[x][y] = val
            return True
        else:
            return False

    def is_win(self):
        return True if self.board == self.template else False
