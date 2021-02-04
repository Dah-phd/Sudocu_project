import pygame
import numpy as np


pygame.init()


# temporary
a = [[9, 0, 6, 3, 4, 0, 8, 1, 0],
     [0, 5, 1, 7, 0, 0, 3, 0, 0],
     [4, 7, 0, 0, 9, 1, 0, 0, 5],
     [0, 0, 0, 9, 0, 3, 0, 0, 2],
     [0, 0, 2, 0, 8, 7, 0, 0, 0],
     [1, 0, 7, 2, 0, 0, 6, 0, 0],
     [0, 8, 5, 0, 0, 9, 1, 0, 0],
     [0, 3, 4, 0, 6, 0, 0, 0, 9],
     [0, 1, 0, 5, 0, 8, 7, 0, 6]]
a = np.array(a)


# base_variables
elements = [0, 1, 2, 3, 4, 5, 6, 7, 8]
possible_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
w_lenght = 720
sq_lenght = w_lenght/9
font = pygame.font.SysFont('Times New Roman', 60)
small_font = pygame.font.SysFont('Times New Roman', 30)
the_grid = pygame.display.set_mode((w_lenght, w_lenght))
pygame.display.set_caption('Sudoku, by Dah')
clock = pygame.time.Clock()


def render_numbers(surface, array):
    for t in elements:
        for t1 in elements:
            if array[t][t1] > 0:
                text = font.render(str(array[t][t1]), True, (0, 0, 0))
                surface.blit(text, (sq_lenght*t1+25, sq_lenght*t+10))
            elif array[t][t1] == 0:
                pass
                # entry((sq_lenght*t1+25, sq_lenght*t+10))
                # 25 = sq_lenght/2 - text.get_hight()/2


# def entry(box_position):
#     text = ''
#     if event.type == pygame.MOUSEBUTTONDOWN:
#         pass
#     if event.type == pygame.KEYDOWN:
#         if active:
#             if event.key == pygame.K_RETURN:
#                 print(text)
#                 text = ''
#             elif event.key == pygame.K_BACKSPACE:
#                 text = text[:-1]
#             else:
#                 text += event.unicode
    # function to generate text box where you can write down answares


def draw(surface):
    surface.fill((230, 255, 255))
    for t in possible_values[:8]:
        if t == 3 or t == 6:
            pygame.draw.line(surface, (0, 0, 0), (0,  sq_lenght*t+1),
                             (w_lenght, sq_lenght*t), width=4)
        else:
            pygame.draw.line(surface, (60, 60, 60), (0,  sq_lenght*t+1),
                             (w_lenght, sq_lenght*t), width=2)
    for t in possible_values[:8]:
        if t == 3 or t == 6:
            pygame.draw.line(surface, (0, 0, 0), (sq_lenght*t, 0),
                             (sq_lenght*t, w_lenght), width=4)
        else:
            pygame.draw.line(surface, (60, 60, 60), (sq_lenght*t, 0),
                             (sq_lenght*t, w_lenght), width=2)
    render_numbers(surface, a)


def main():
    finished = False
    while not finished:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
        draw(the_grid)
        pygame.display.update()


main()
