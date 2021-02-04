import numpy as np
import requests
import tkinter as tk
import sys
from tkinter import messagebox

# temporary
sys.setrecursionlimit(15000)


def set(diff=3, size=9):
    global puzzle
    global key
    global a
    try:
        layout = {'size': size, 'level': diff}
        r = requests.get('http://www.cs.utep.edu/cheon/ws/sudoku/new/', params=layout, timeout=3)
        r = r.json()
        a = [[], [], [], [], [], [], [], [], []]
        m = 0
        for t in range(9):
            for t1 in range(9):
                try:
                    if r['squares'][m]['x'] == t and r['squares'][m]['y'] == t1:
                        a[t1].append(r['squares'][m]['value'])
                        m += 1
                    else:
                        a[t1].append(0)
                except IndexError:
                    a[t1].append(0)
    except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
        a = [[9, 0, 6, 3, 4, 0, 8, 1, 0],
             [0, 5, 1, 7, 0, 0, 3, 0, 0],
             [4, 7, 0, 0, 9, 1, 0, 0, 5],
             [0, 0, 0, 9, 0, 3, 0, 0, 2],
             [0, 0, 2, 0, 8, 7, 0, 0, 0],
             [1, 0, 7, 2, 0, 0, 6, 0, 0],
             [0, 8, 5, 0, 0, 9, 1, 0, 0],
             [0, 3, 4, 0, 6, 0, 0, 0, 9],
             [0, 1, 0, 5, 0, 8, 7, 0, 6]]
    puzzle = np.array(a)
    key = puzzle.copy()
    solve(key)


# function for solving puzzle


def replace(array, row, column):
    possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for t in array[row]:
        if t != 0:
            possible_values.remove(t)
    for t in array[:, column]:
        if t != 0:
            try:
                possible_values.remove(t)
            except ValueError:
                pass
    square_x = [0, 3] if row < 3 else [3, 6] if row < 6 else [6, 9]
    square_y = [0, 3] if column < 3 else [3, 6] if column < 6 else [6, 9]
    for t1 in array[square_x[0]:square_x[1], square_y[0]:square_y[1]]:
        for t in t1:
            if t != 0:
                try:
                    possible_values.remove(t)
                except ValueError:
                    pass
    return possible_values


# actual solve
def find_location(array):
    for t in range(9):
        for t1 in range(9):
            if array[t][t1] == 0:
                return (t, t1)
            else:
                return False


def solve(array):
    find = find_location(array)
    if not find:
        return True
    else:
        row, column = find
        for t in replace(array, row, column):
            if t:
                array[row][column] = t
                if solve(array):
                    return True
            else:
                array[row][column] = 0
    return False


# base variables
lives = 4
mistakes = []


def reset():
    global puzzle
    global lives
    puzzle = np.array(a)
    lives = 4
    for t in mistakes:
        t.destroy()
    draw_grid(puzzle)


def draw_grid(array):
    global list_entry
    list_entry = []
    for t in range(9):
        for t1 in range(9):
            if array[t][t1] != 0:
                static = tk.Label(text=str(array[t][t1]), font=("TimesNewRoman", 44), borderwidth=4,
                                  relief="raised", padx=24, pady=8)
                static.grid(row=t, column=t1)
            else:
                entry = tk.Entry(width=2, font=("TimesNewRoman", 44), justify='center', fg='gray')
                entry.grid(row=t, column=t1)
                entry.after(200, enter)
                #   entry.bind('<Return>', lambda event: enter(array))
                list_entry.append(entry)


def enter(m=0):
    global list_entry
    for t in range(9):
        for t1 in range(9):
            if puzzle[t][t1] == 0:
                if not list_entry[m].get() == '':
                    temp = int(list_entry[m].get())
                    list_entry[m].delete(0, 'end')
                    if temp == key[t][t1]:
                        puzzle[t][t1] = temp
                        draw_grid(puzzle)
                    else:
                        global lives
                        if lives > 0:
                            lives -= 1
                            label = tk.Label(text='X', fg='red', font=("TimesNewRoman", 44))
                            label.grid(row=10, column=7-lives)
                            mistakes.append(label)
                        else:
                            res = messagebox.askokcancel(
                                title="GAME OVER!", message='Do you want ot reset?')
                            if res:
                                reset()
                            else:
                                game_win.destroy()
                m += 1


game_win = tk.Tk()
game_win.title('TkSudoku by Dah')
live = tk.Label(game_win, text='X (max 5):', font=("TimesNewRoman", 44))
live.grid(row=10, column=0, columnspan=4)
set()
draw_grid(puzzle)
tk.mainloop()
