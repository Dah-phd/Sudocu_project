import requests
import tkinter as tk
import time
from tkinter import messagebox


class puzzle_board():
    def __init__(self, input, name):
        self.name = name
        self.lives = 4
        self.mistakes = []
        self.input = input
        self.base = self.build()
        self.save = self.build()
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
        return a

    def check(self, val, row, column):
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
            if self.check(t, row, column):
                self.template[row][column] = t
                if self.solve():
                    return True
        self.template[row][column] = 0
        return False


class timing():
    def __init__(self, window):
        self.start = time.time()
        self.window = window
        self.label = tk.Label(self.window, text=0, font=("TimesNewRoman", 44))
        self.label.grid(row=10, column=0, columnspan=4)
        self.tick_tock()

    def tick_tock(self):
        clean = int(time.time() - self.start)
        min = str(int(clean/60))
        sec = str(clean-60*int(clean/60))
        zilch = '' if int(sec) > 9 else '0'
        now = min+':'+zilch+sec
        self.label.configure(text=now)
        self.window.after(1000, self.tick_tock)

    def get_points(self):
        return int(time.time() - self.start)


def draw_template(template_):
    list_entry = []
    for t in range(9):
        for t1 in range(9):
            if template_.base[t][t1] != 0:
                static = tk.Label(text=str(template_.base[t][t1]), font=("TimesNewRoman", 44), borderwidth=4,
                                  relief="raised", padx=24, pady=8)
                static.grid(row=t, column=t1)
            else:
                entry = tk.Entry(width=2, font=("TimesNewRoman", 44),
                                 justify='center', fg='gray')
                entry.grid(row=t, column=t1)
                entry.bind('<Return>', lambda event: enter(
                    template_, list_entry))
                list_entry.append(entry)


def enter(template_, list_entry, m=0):
    # fix wincondition
    for t in range(9):
        for t1 in range(9):
            if template_.base[t][t1] == 0:
                if not list_entry[m].get() == '':
                    temp = int(list_entry[m].get())
                    list_entry[m].delete(0, 'end')
                    if temp == template_.template[t][t1]:
                        template_.base[t][t1] = temp
                        draw_template(template_)
                    else:
                        if template_.lives > 0:
                            template_.lives -= 1
                            label = tk.Label(
                                text='X', fg='red', font=("TimesNewRoman", 44))
                            label.grid(row=10, column=7-template_.lives)
                            template_.mistakes.append(label)
                        else:
                            res = messagebox.askokcancel(
                                title="GAME OVER!", message='Do you want ot reset?')
                            if res:
                                reset(template_)
                            else:
                                game_win.destroy()
                m += 1


def reset(template_):
    template_.base = template_.save
    template_.lives = 4
    for t in template_.mistakes:
        t.destroy()
    clock.start = time.time()


def set():
    # this could use a lot of work - not # optimized neither well written
    def get_board(difficulty=2):
        name = name_tag.get()
        instruct.destroy()
        name_tag.destroy()
        easy.destroy()
        normal.destroy()
        hard.destroy()
        try:
            layout = {'size': 9, 'level': difficulty}
            r = requests.get('http://www.cs.utep.edu/cheon/ws/sudoku/new/',
                             params=layout, timeout=3)
            r = r.json()
            a = r['squares']
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            if difficulty == 1:
                a = [{'x': 0, 'y': 0, 'value': 5}, {'x': 0, 'y': 3, 'value': 8},
                     {'x': 0, 'y': 4, 'value': 1}, {
                         'x': 0, 'y': 8, 'value': 4},
                     {'x': 1, 'y': 1, 'value': 2}, {
                         'x': 1, 'y': 4, 'value': 5},
                     {'x': 1, 'y': 5, 'value': 4}, {
                         'x': 1, 'y': 6, 'value': 1},
                     {'x': 1, 'y': 7, 'value': 6}, {
                         'x': 2, 'y': 3, 'value': 7},
                     {'x': 2, 'y': 5, 'value': 9}, {
                         'x': 2, 'y': 8, 'value': 5},
                     {'x': 3, 'y': 2, 'value': 1}, {
                         'x': 3, 'y': 6, 'value': 7},
                     {'x': 3, 'y': 7, 'value': 5}, {
                         'x': 3, 'y': 8, 'value': 6},
                     {'x': 4, 'y': 0, 'value': 2}, {
                         'x': 4, 'y': 3, 'value': 6},
                     {'x': 4, 'y': 4, 'value': 9}, {
                         'x': 4, 'y': 5, 'value': 7},
                     {'x': 5, 'y': 0, 'value': 8}, {
                         'x': 5, 'y': 1, 'value': 7},
                     {'x': 5, 'y': 2, 'value': 6}, {
                         'x': 5, 'y': 5, 'value': 1},
                     {'x': 5, 'y': 6, 'value': 2}, {
                         'x': 6, 'y': 1, 'value': 5},
                     {'x': 6, 'y': 2, 'value': 9}, {
                         'x': 6, 'y': 3, 'value': 1},
                     {'x': 6, 'y': 5, 'value': 3}, {
                         'x': 6, 'y': 8, 'value': 2},
                     {'x': 7, 'y': 1, 'value': 1}, {
                         'x': 7, 'y': 3, 'value': 4},
                     {'x': 7, 'y': 6, 'value': 5}, {
                         'x': 7, 'y': 7, 'value': 9},
                     {'x': 7, 'y': 8, 'value': 8}, {
                         'x': 8, 'y': 0, 'value': 7},
                     {'x': 8, 'y': 1, 'value': 8}, {
                         'x': 8, 'y': 3, 'value': 9},
                     {'x': 8, 'y': 4, 'value': 6}, {
                         'x': 8, 'y': 7, 'value': 1},
                     {'x': 8, 'y': 8, 'value': 3}]
            elif difficulty == 2:
                a = [{'x': 0, 'y': 2, 'value': 6}, {'x': 0, 'y': 4, 'value': 2},
                     {'x': 0, 'y': 6, 'value': 3}, {
                         'x': 0, 'y': 8, 'value': 1},
                     {'x': 1, 'y': 4, 'value': 7}, {
                         'x': 1, 'y': 6, 'value': 6},
                     {'x': 2, 'y': 0, 'value': 5}, {
                         'x': 2, 'y': 1, 'value': 1},
                     {'x': 2, 'y': 7, 'value': 8}, {
                         'x': 3, 'y': 0, 'value': 3},
                     {'x': 3, 'y': 6, 'value': 7}, {
                         'x': 3, 'y': 8, 'value': 8},
                     {'x': 4, 'y': 3, 'value': 3}, {
                         'x': 4, 'y': 5, 'value': 5},
                     {'x': 4, 'y': 6, 'value': 1}, {
                         'x': 5, 'y': 0, 'value': 8},
                     {'x': 5, 'y': 2, 'value': 5}, {
                         'x': 5, 'y': 5, 'value': 7},
                     {'x': 5, 'y': 7, 'value': 3}, {
                         'x': 5, 'y': 8, 'value': 9},
                     {'x': 6, 'y': 1, 'value': 8}, {
                         'x': 6, 'y': 3, 'value': 7},
                     {'x': 6, 'y': 7, 'value': 1}, {
                         'x': 7, 'y': 0, 'value': 9},
                     {'x': 7, 'y': 4, 'value': 5}, {
                         'x': 7, 'y': 8, 'value': 3},
                     {'x': 8, 'y': 2, 'value': 2}, {
                         'x': 8, 'y': 4, 'value': 3},
                     {'x': 8, 'y': 5, 'value': 6}, {'x': 8, 'y': 6, 'value': 9}]

            else:
                a = [{'x': 0, 'y': 1, 'value': 2}, {'x': 0, 'y': 4, 'value': 9},
                     {'x': 0, 'y': 7, 'value': 8}, {
                         'x': 1, 'y': 0, 'value': 9},
                     {'x': 1, 'y': 8, 'value': 3}, {
                         'x': 2, 'y': 2, 'value': 3},
                     {'x': 2, 'y': 4, 'value': 5}, {
                         'x': 3, 'y': 1, 'value': 1},
                     {'x': 3, 'y': 5, 'value': 7}, {
                         'x': 3, 'y': 6, 'value': 9},
                     {'x': 4, 'y': 0, 'value': 6}, {
                         'x': 4, 'y': 5, 'value': 5},
                     {'x': 4, 'y': 8, 'value': 1}, {
                         'x': 5, 'y': 3, 'value': 9},
                     {'x': 5, 'y': 6, 'value': 6}, {
                         'x': 6, 'y': 2, 'value': 6},
                     {'x': 7, 'y': 3, 'value': 6}, {
                         'x': 8, 'y': 1, 'value': 9},
                     {'x': 8, 'y': 5, 'value': 8}, {'x': 8, 'y': 7, 'value': 6}]
        global sudoku
        global clock
        sudoku = puzzle_board(a, name)
        for t in range(5):
            lif = tk.Label(game_win, text="\U0001F600",
                           font=("TimesNewRoman", 40), fg='green')
            lif.grid(row=10, column=4+t)
        clock = timing(game_win)
        draw_template(sudoku)

    def diff(list_to_kill=[]):
        for t in list_to_kill:
            t.destroy()
        global easy, normal, hard, name_tag, instruct
        instruct = tk.Label(game_win, text='Enter name, than select difficulty:',
                            font=("TimesNewRoman", 40), wraplength=500, justify="center")
        name_tag = tk.Entry(game_win, font=("TimesNewRoman", 40), width=12, borderwidth=8,
                            relief="sunken")
        easy = tk.Button(game_win, text='Easy', font=("TimesNewRoman", 40),
                         fg='green', command=lambda: get_board(1))
        normal = tk.Button(game_win, text='Normal', font=(
            "TimesNewRoman", 40), command=lambda: get_board(2))
        hard = tk.Button(game_win, text='Hard', font=("TimesNewRoman", 40),
                         fg='red', command=lambda: get_board(3))
        instruct.grid(row=0, column=0)
        name_tag.grid(row=1, column=0)
        easy.grid(row=2, column=0)
        normal.grid(row=3, column=0)
        hard.grid(row=4, column=0)

    try:
        with open("data.wb", "r") as score_safe:
            score_t = score_safe.read()
            score_t = score_t.split('_')
            del score_t[-1]
            # score_t = score_t[0:9]
            names = []
            points = []
            for t in score_t:
                temp = t.split(':')
                names.append(temp[0])
                points.append(temp[1])
            counter = 0
            list = []
            for t in names:
                post = tk.Label(game_win, text=counter+1, font=(
                    "TimesNewRoman", 40), wraplength=500, justify="center")
                post.grid(row=counter, column=0)
                list.append(post)
                post = tk.Label(game_win, text=names[counter], font=(
                    "TimesNewRoman", 40), wraplength=500, justify="left")
                post.grid(row=counter, column=1)
                list.append(post)
                post = tk.Label(game_win, text=points[counter], font=(
                    "TimesNewRoman", 40), wraplength=500, justify="left")
                post.grid(row=counter, column=2)
                list.append(post)
                counter += 1
            next = tk.Button(game_win, text='Start new game', font=("TimesNewRoman", 40),
                             relief='raised', borderwidth=8, command=lambda: diff(list))
            list.append(next)
            next.grid(row=100, column=0, columnspan=3)
    except FileNotFoundError:
        score_safe = open('data.wb', 'x')
        score_safe.close()
        diff()
    except IndexError:
        pass


def scoring(name, scorepoints):
    # saving final results
    score_list = []
    with open('data.wb', 'r') as score_safe:
        score_t = score_safe.read().split('_')
        del score_t[-1]
        # removing the final _ to evade problems while reading and splitting
        try:
            for t in score_t:
                temp = t.split(':')
                score_list.append((temp[0], temp[1]))
        except IndexError:
            pass
    score_safe = open('data.wb', 'w')
    num = 0
    for t in score_list:
        if int(t[1]) < scorepoints:
            num += 1
    score_list.insert(num, (name, scorepoints))
    for t in score_list:
        t = str(t[0])+':'+str(t[1])+'_'
        score_safe.write(t)
    score_safe.close()

# actual solve
# base variables


def main():
    if __name__ == '__main__':
        global game_win
        game_win = tk.Tk()
        set()
        game_win.title('TkSudoku by Dah')
        tk.mainloop()


main()
