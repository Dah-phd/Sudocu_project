import pygame as pg


class InputBox:

    def __init__(
        self, rect, text='',
        COLOR_ACTIVE=(23, 236, 236),
        COLOR_INACTIVE=(0, 0, 0),
        INVIS_INACTIVE=False,
        REPLACE=False,
        font_size=32
    ):
        self.rect = pg.Rect(rect[0], rect[1], rect[2], rect[3])
        self.text = text
        self.INVIS_INACTIVE = INVIS_INACTIVE
        self.COLOR_INACTIVE = COLOR_INACTIVE
        self.COLOR_ACTIVE = COLOR_ACTIVE
        self.REPLACE = REPLACE
        self.FONT = pg.font.Font(None, font_size)
        self.color = self.COLOR_INACTIVE
        self.txt_surface = self.FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text = self.text+event.unicode if not self.REPLACE else event.unicode

                # Re-render the text.
                self.txt_surface = self.FONT.render(
                    self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect,
                     -1 if not self.active and self.INVIS_INACTIVE else 2)
