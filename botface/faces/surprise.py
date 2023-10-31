from math import floor
from pygame import Color, Rect, Surface, SRCALPHA
from pygame.draw import circle, ellipse
from pygame.time import get_ticks
from random import randint

from .colorbg import ColorBg


class SurpriseFace(ColorBg):
    def __init__(self, surface):
        super().__init__(surface)

        width = surface.get_width()
        height = surface.get_height()
        sw = floor(width / 4)
        eye_x = floor(sw * 1.05)
        eye_y = floor(height / 2.7)
        eye_r = floor(height / 11)
        mouth_w = sw / 2
        mouth_h = sw / 2.5
        mouth_x = (width / 2) - (mouth_w / 2)
        mouth_y = (height - eye_y) * 1.2

        self.surface = surface
        self.width = width
        self.eye_x = eye_x
        self.eye_y = eye_y
        self.big_eye_r = eye_r * 1.3
        self.eye_r = eye_r * 0.8
        self.mouth_w = mouth_w
        self.mouth_h = mouth_h
        self.mouth_x = mouth_x
        self.mouth_y = mouth_y
        self.duration = 5

    def render(self, event):
        self.render_background()
        self.render_eyes()
        self.render_mouth()

    def render_eyes(self):
        ms = get_ticks() % 1000

        if ms < randint(775, 825):
            self.render_open_eyes()
        elif ms > randint(925, 975):
            self.render_blink()
        elif ms > randint(875, 925):
            self.render_open_eyes()
        elif ms > randint(825, 875):
            self.render_blink()

    def render_open_eyes(self):
        l_circle = Surface((self.big_eye_r * 2, self.big_eye_r * 2), SRCALPHA)
        r_circle = Surface((self.big_eye_r * 2, self.big_eye_r * 2), SRCALPHA)

        circle(l_circle, (0, 0, 0, 160), (self.big_eye_r, self.big_eye_r), self.big_eye_r)
        self.surface.blit(l_circle, (self.eye_x - self.big_eye_r, self.eye_y - self.big_eye_r))

        circle(l_circle, (0, 0, 0, 160), (self.big_eye_r, self.big_eye_r), self.big_eye_r)
        self.surface.blit(l_circle, (self.width - self.eye_x - self.big_eye_r, self.eye_y - self.big_eye_r))

        circle(self.surface, "#000000", (self.eye_x, self.eye_y), self.eye_r)
        circle(self.surface, "#000000", (self.width - self.eye_x, self.eye_y), self.eye_r)

    def render_blink(self):
        self.surface.fill(
            Color("#000000"),
            Rect(0, self.eye_y - (self.eye_r / 4), self.width, self.eye_r / 2)
        )

    def render_mouth(self):
        r = Surface((self.mouth_w, self.mouth_h), SRCALPHA)
        r.fill((0,0,0,200))

        self.surface.blit(r, (self.mouth_x, self.mouth_y))
        #self.surface.fill(
        #    Color("#000000"),
        #    Rect(self.mouth_x, self.mouth_y, self.mouth_w, self.mouth_h)
        #)self
