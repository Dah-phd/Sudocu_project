import pygame as pg
from res.pg_inputbox import InputBox


def main():
    clock = pg.time.Clock()
    input_box1 = InputBox((100, 100, 140, 32),
                          INVIS_INACTIVE=True, REPLACE=True)
    input_box2 = InputBox((100, 300, 140, 32), REPLACE=True)
    input_boxes = [input_box1, input_box2]
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    screen = pg.display.set_mode((640, 480))
    main()
    pg.quit()
