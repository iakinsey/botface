from concurrent.futures import ThreadPoolExecutor
from math import floor
from pygame.image import load
from pygame.transform import scale
from pygame import Color, Rect

from .colorbg import ColorBg


executor = ThreadPoolExecutor(max_workers=1)


class MusicFace(ColorBg):
    def __init__(self, surface):
        super().__init__(surface)

        self.w = surface.get_width()
        self.h = surface.get_height()

        note_w = floor(self.w / 1.5)
        note_h = floor(self.h / 1.5)

        self.played = False
        self.note = scale(load('assets/music_notes.png'), (note_w, note_h))
        self.note_x = (self.w / 2) - (note_w / 2)
        self.note_top = self.h / 12
        self.note_bottom = (self.h / 12) * 11 - note_h
        self.note_y = self.note_top
        self.direction = 'down'

    def render(self, event):
        self.render_background()
        self.render_notes()

    def render_background(self):
        self.surface.fill(Color("#000000"), Rect(0, 0, self.w, self.h))

    def render_notes(self):
        if self.note_y <= self.note_top:
            self.direction = 'down'
        elif self.note_y >= self.note_bottom:
            self.direction = 'up'

        if self.direction == 'down':
            self.note_y += 1
        elif self.direction == 'up':
            self.note_y -= 1

        self.surface.blit(self.note, (self.note_x, self.note_y))
