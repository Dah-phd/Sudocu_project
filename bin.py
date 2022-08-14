from res.sudoku_board import request_tmp
from res.sudoku_log import sudoku
from res.scoring import Highscore
from res.pg_inputbox import InputBox
import time
import pygame as pg


class GUI:
    keys = [
        pg.K_1, pg.K_2, pg.K_3,
        pg.K_4, pg.K_5, pg.K_6,
        pg.K_7, pg.K_8, pg.K_9,
        pg.K_KP1, pg.K_KP2, pg.K_KP3,
        pg.K_KP4, pg.K_KP5, pg.K_KP6,
        pg.K_KP7, pg.K_KP8, pg.K_KP9,
        pg.K_BACKSPACE
    ]

    def __init__(self):
        self.klok = pg.time.Clock()
        self.font = pg.font.SysFont('Times New Roman', 66)
        self.dims = (730, 800)
        self.grid = pg.display.set_mode(self.dims)
        self.difficulty = 3

    def run(self):

        while self.active:
            self.klok.tick(30)
            self.draw()
            if self.lives >= 0:
                self.controls()
            else:
                self.active = False
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
            str(self._timer(time.time()-self.time)), True, (23, 236, 236)), (580, 730))

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
            self.active = False
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
                if event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER:
                    self.check()
                elif event.key in self.keys:
                    for box in self._text_boxes:
                        box[2].handle_event(event)
                elif event.key == pg.K_UP:
                    self._box_arrows(0, -1)
                elif event.key == pg.K_DOWN:
                    self._box_arrows(0, 1)
                elif event.key == pg.K_LEFT:
                    self._box_arrows(-1, 0)
                elif event.key == pg.K_RIGHT:
                    self._box_arrows(1, 0)

    def _box_arrows(self, x, y):
        for box in self._text_boxes:
            if box[2].active:
                box[2].active = False
                for newbox in self._text_boxes:
                    if box[0]+y == newbox[0] and box[1]+x == newbox[1]:
                        newbox[2].active = True
                        break
                break

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
        self.active = False
        active = True
        while active:
            self.grid.fill((255, 255, 255))
            if self.lives >= 0:
                if self.difficulty == 3:
                    self.score.new_score(time.time()-self.time)
                    self.difficulty = 2
                color = (23, 236, 236)
                self.grid.blit(self.font.render(
                    'WINNER!!!', True, color), (100, 300))
            else:
                color = (255, 50, 50)
                self.grid.blit(self.font.render(
                    'GAME OVER', True, color), (100, 300))
            self.grid.blit(self.font.render(
                'ESC to quit', True, color), (100, 400))
            self.grid.blit(self.font.render(
                'Enter for new game', True, color), (100, 480))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    active = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        active = False
                    elif event.key == pg.K_SPACE or event.key == pg.K_RETURN:
                        active = False
                        self.start()
            pg.display.update()

    def start(self):
        '''
        Quite fat, and far from pretty but most if is drawing and it dose the job well
        '''
        self.score = Highscore(
            base_name='res\\saves',
            high='min')
        name_box = InputBox((250, 60, 400, 53), font_size=66)
        easy = InputBox((50, 130, 200, 50), text='Easy', font_size=66)
        normal = InputBox((250, 130, 200, 50), text='Normal', font_size=66)
        hard = InputBox((450, 130, 200, 50), text='Hard', font_size=66)
        active = True
        while active:
            self.grid.fill((100, 100, 100))
            name_box.draw(self.grid)
            self.grid.blit(self.font.render(
                'Name:', True, (23, 236, 236)), (50, 45))
            self.grid.blit(self.font.render(
                'Press enter to continue', True, (23, 236, 236)), (50, 700))
            self.grid.blit(self.font.render(
                'HIGHSCORE:', True, (23, 236, 236)), (50, 180))
            hs = self.score.quarry()
            easy.draw(self.grid)
            normal.draw(self.grid)
            hard.draw(self.grid)
            if hs:
                for n, score in enumerate(hs, start=2):
                    self.grid.blit(self.font.render(
                        str(n+1), True, (23, 236, 236)), (70, 200+n*60))
                    self.grid.blit(self.font.render(
                        score[0], True, (23, 236, 236)), (115, 200+n*60))
                    self.grid.blit(self.font.render(
                        str(self._timer(score[1])), True, (23, 236, 236)), (440, 200+n*60))
                    if n == 4:
                        break
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    active = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        active = False
                        self._gameprep(
                            name_box, 2 if normal.active else 1 if easy.active else 3
                        )

                easy.handle_event(event)
                normal.handle_event(event)
                hard.handle_event(event)
                name_box.handle_event(event)
            pg.display.update()

    def _gameprep(self, name_box, diff):
        self.difficulty = diff
        self.active = True
        self.score.name = name_box.text
        self.lives = 4
        self.template = request_tmp(self.difficulty)
        self.board = sudoku(self.template.board)
        self.time = time.time()
        self._text_boxes = []
        self.run()

    def _timer(self, val):
        seconds = str(int(val % 60))
        return str(int(val/60))+(':0' if len(seconds) == 1 else ':') + seconds


if __name__ == '__main__':
    pg.init()
    pg.display.set_caption('Sudoku by Dah')
    main = GUI()
    main.start()


pg.quit()
