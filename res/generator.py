# easy 40
# normal 30
# hard 20
import random
import time

# could be used in conjunction with checking algorithm and


class board_builder:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self, difficulty=3):
        self.difficulty = difficulty
        self.generate()

    def generate(self):
        done = False
        while not done:
            self.full_board = [[0 for _ in range(9)] for _ in range(9)]
            self.board = [[0 for _ in range(9)] for _ in range(9)]
            self.back_track(self.full_board)
            self.puzzle_up()
            if self.test():
                done = True

    def back_track(self, board):
        location = self._find(board)
        if not location:
            return True
        else:
            possible = self.numbers.copy()
            for _ in range(9):
                if possible:
                    val = random.choice(possible)
                    possible.remove(val)
                    if self._check(board, location, val):
                        board[location[0]][location[1]] = val
                        if self.back_track(board):
                            return True
        board[location[0]][location[1]] = 0
        return False

    def puzzle_up(self):
        ls = [t for t in range(81)]
        revealed = 20 if self.difficulty == 3 else 30 if self.difficulty == 2 else 40
        while revealed > 0:
            revealed -= 1
            cell = random.choice(ls)
            if cell == 0:
                self.board[0][0] = self.full_board[0][0]
            else:
                self.board[int(cell/9)][cell %
                                        9] = self.full_board[int(cell/9)][cell % 9]

    def solver(self, board):
        location = self._find(board)
        if not location:
            return True
        else:
            for val in self.numbers:
                if self._check(board, location, val):
                    board[location[0]][location[1]] = val
                    if self.solver(board):
                        return True
        board[location[0]][location[1]] = 0
        return False

    def test(self):
        print('tick')
        for _ in range(6):
            self.new_b = [row.copy() for row in self.board]
            self.solver(self.new_b)
            if self.new_b == self.full_board:
                return True
            self.rev_b = self._reverse(self.board)
            self.solver(self.rev_b)
            if self._reverse(self.rev_b) == self.full_board:
                return True
        return False

    def __repr__(self):
        print()
        print("FULL BOARD!")
        for row in self.full_board:
            print(row)
        print()
        print("BOARD!")
        for row in self.board:
            print(row)
        print()
        print("new_b!")
        for row in self.full_board:
            print(row)
        print()
        print("rev_b!")
        for row in self.full_board:
            print(row)

    def _reverse(self, board):
        table = [row.copy() for row in board]
        for row in table:
            row.reverse()
        table.reverse()
        return table

    def _find(self, board):
        for n_row, row in enumerate(board):
            for n_cell, cell in enumerate(row):
                if cell == 0:
                    return (n_row, n_cell)
        return False

    def _check(self, board, location, val):
        if val in board[location[0]]:
            return False
        for row in board:
            if row[location[1]] == val:
                return False
        rows = (0, 3) if location[0] < 3 else (
            3, 6) if location[0] < 6 else (6, 9)
        cells = (0, 3) if location[1] < 3 else (
            3, 6) if location[1] < 6 else (6, 9)
        for row in range(rows[0], rows[1]):
            if val in board[row][cells[0]:cells[1]]:
                return False
        return True
