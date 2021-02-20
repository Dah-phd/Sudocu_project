from res.sudoku_board import request_tmp
from res.sudoku_log import sudoku
from res.scoring import highscore
from res.pg_inputbox import InputBox
import time
import pygame as pg


class GUI:
    keys = [
        pg.K_1, pg.K_2, pg.K_3,
        pg.K_4, pg.K_5, pg.K_6,
        pg.K_7, pg.K_8, pg.K_9,
        pg.K_BACKSPACE
    ]

    def __init__(self):
        self.active = True
        self.klok = pg.time.Clock()
        self.font = pg.font.SysFont('Times New Roman', 66)
        self.dims = (730, 800)
        self.grid = pg.display.set_mode(self.dims)
        self._text_boxes = []

    def run(self):

        while self.active:
            self.klok.tick(30)
            self.draw()
            if self.lives >= 0:
                self.controls()
            else:
                self.end()
            pg.display.update()

    def draw(self):
        self.grid.fill((0, 0, 0))
        # draw field and static boxes
        for n_row, row in enumerate(self.board.board):
            for n_sq, sq in enumerate(row):
                pad_x = 2 if n_row < 3 else 7 if n_row < 6 else 12
                pad_y = 0 if n_sq < 3 else 5 if n_sq < 6 else 10
                pg.draw.rect(self.grid, (255, 255, 255),
                             (n_sq*80+pad_y, n_row*80+pad_x, 78, 78))
                if sq != 0:
                    self.grid.blit(self.font.render(
                        str(sq), True, (0, 0, 0)), (n_sq*80+20+pad_y, n_row*80+pad_x)
                    )
        self._make_boxes()
        self.grid.blit(self.font.render(
            'LIVES:', True, (23, 236, 236)), (20, 730))
        self.grid.blit(self.font.render(
            str(self.lives), True, (23, 236, 236)), (250, 730))
        self.grid.blit(self.font.render(
            str(self._timer(time.time()-self.time)), True, (23, 236, 236)), (600, 730))

    def _make_boxes(self):
        if not self._text_boxes:
            for n_row, row in enumerate(self.board.board):
                for n_sq, sq in enumerate(row):
                    if sq == 0:
                        pad_x = 2 if n_row < 3 else 7 if n_row < 6 else 12
                        pad_y = 0 if n_sq < 3 else 5 if n_sq < 6 else 10
                        rect = (n_sq*80+pad_y, n_row * 80+pad_x, 78, 78)
                        self._text_boxes.append((n_row, n_sq,
                                                 InputBox(
                                                     rect,
                                                     INVIS_INACTIVE=True,
                                                     REPLACE=True)
                                                 ))
        if not self._text_boxes:
            self.end()
        for box in self._text_boxes:
            box[2].draw(self.grid)

    def controls(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.active = False
            if event.type == pg.MOUSEBUTTONDOWN:
                for box in self._text_boxes:
                    box[2].handle_event(event)
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    self.check()
                elif event.key in self.keys:
                    for box in self._text_boxes:
                        box[2].handle_event(event)

    def check(self):
        for box in self._text_boxes:
            if box[2].active and box[2].text != '':
                if self.board.is_correct(int(box[2].text), box[0], box[1]):
                    self._text_boxes = []
                else:
                    box[2].text = ''
                    box[2].draw(self.grid)
                    self.lives -= 1

    def end(self):
        self.grid.fill((255, 255, 255))
        if self.lives >= 0:
            self.score.new_score(time.time()-self.time)
            color = (23, 236, 236)
            self.grid.blit(self.font.render(
                'WINNER!!!', True, color), (100, 300))
        else:
            color = (255, 50, 50)
            self.grid.blit(self.font.render(
                'GAME OVER', True, color), (100, 300))
        self.grid.blit(self.font.render(
            'ESC to quit | Enter for new game', True, color), (100, 400))
        self.grid.blit(self.font.render(
            'ESC to quit | Enter for new game', True, color), (100, 400))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.active = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.active = False
                elif event.key == pg.K_SPACE or event.key == pg.K_RETURN:
                    self.start()

    def start(self):
        '''
        Quite fat, and far from pretty but most if is drawing and it dose the job well
        '''
        self.score = highscore(
            dbase_name='res\\saves',
            high='min')
        name_box = InputBox((250, 60, 350, 53), font_size=66)
        while self.active:
            self.grid.fill((100, 100, 100))
            name_box.draw(self.grid)
            self.grid.blit(self.font.render(
                'Name:', True, (23, 236, 236)), (50, 45))
            self.grid.blit(self.font.render(
                'Press enter to continue', True, (23, 236, 236)), (50, 700))
            self.grid.blit(self.font.render(
                'HIGHSCORE:', True, (23, 236, 236)), (50, 130))
            hs = self.score.quarry()
            if hs:
                for n, score in enumerate(hs):
                    self.grid.blit(self.font.render(
                        str(n), True, (23, 236, 236)), (50, 130))
                    self.grid.blit(self.font.render(
                        score[0], True, (23, 236, 236)), (50, 130))
                    self.grid.blit(self.font.render(
                        str(self._timer(score[1])), True, (23, 236, 236)), (50, 130))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.active = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        self.score.name = name_box.text
                        self.lives = 4
                        self.template = request_tmp()
                        self.board = sudoku(self.template.board)
                        self.time = time.time()
                        self.run()
                name_box.handle_event(event)
            pg.display.update()

    def _timer(self, val):
        seconds = str(int(val % 60))
        return str(int(val/60))+(':0' if len(seconds) == 1 else ':') + seconds


if __name__ == '__main__':
    pg.init()
    pg.display.set_caption('Sudoku by Dah')
    main = GUI()
    main.start()


pg.quit()
