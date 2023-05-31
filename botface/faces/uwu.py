from math import floor

from pygame.font import Font
from pygame import Color, Rect
from pygame.image import load
from pygame.transform import scale


class UwuFace:
    def __init__(self, surface):
        self.surface = surface
        self.w = surface.get_width()
        self.h = surface.get_height()
        self.duration = 5

        uwu = load('assets/uwu.png')
        old_w = uwu.get_width()
        old_h = uwu.get_height()
        uwu_w = self.h
        uwu_h = old_h * (uwu_w / old_w)

        self.uwu = scale(uwu, (uwu_w, uwu_h))
        self.uwu_rect = self.uwu.get_rect(center=(self.w / 2, self.h / 2))

    def render(self, event):
        self.render_background()
        self.render_uwu()

    def render_background(self):
        self.surface.fill(Color("#FFFFFF"), Rect(0, 0, self.w, self.h))

    def render_uwu(self):
        self.surface.blit(self.uwu, self.uwu_rect)
