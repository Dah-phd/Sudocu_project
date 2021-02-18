from res.sudoku_board import request_tmp
from res.sudoku_log import sudoku
from res.scoring import highscore
import time
import pygame as pg

pg.init()

h, w = 900, 800


class GUI:
    def __init__(self):
        self.active = True
        self.template = request_tmp()
        self.board = sudoku(self.template.board)
        self.lives = 4
        self.klok = pg.time.Clock()
        self.font = pg.font.SysFont('Times New Roman', 66)
        self.dims = (900, 800)
        self.grid = pg.display.set_mode(self.dims)
        print(self.board.board)

    def run(self):
        while self.active:
            self.klok.tick(10)
            self._controls()
            self._draw()

            pg.display.update()

    def _draw(self):
        self.grid.fill((0, 0, 0))
        for n_row, row in enumerate(self.board.board):
            for n_sq, sq in enumerate(row):
                pg.draw.rect(self.grid, (255, 255, 255),
                             (n_sq*80, n_row*80, 78, 78))
                self.grid.blit(self.font.render(
                    str(sq), True, (0, 0, 0)), (n_sq*80+20, n_row*80)
                )
        return False

    def _controls(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.active = False


if __name__ == '__main__':
    main = GUI()
    main.run()


pg.quit()
