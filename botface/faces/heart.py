from math import floor
from random import randint

from pygame.image import load
from pygame.mixer import Sound
from pygame.transform import scale

from .colorbg import ColorBg
from .audiomixin import AudioMixin


class HeartFace(AudioMixin, ColorBg):
    sounds = [
        Sound('assets/heart1.wav'),
        Sound('assets/heart2.wav'),
        Sound('assets/heart3.wav'),
    ]

    def __init__(self, surface, channel):
        super().__init__(surface)

        w = surface.get_width()
        h = surface.get_height()
        heart_w = floor(w / 1.5)
        heart_h = floor(h / 1.5)

        self.played = False
        self.heart = scale(load('assets/heart.svg'), (heart_w, heart_h))
        self.heart_x = (w / 2) - (heart_w / 2)
        self.heart_y = (h / 2) - (heart_h / 2)
        self.duration = randint(1, 3)
        self.sound = self.sounds[self.duration - 1]
        self.channel = channel

    def render(self, event):
        self.play_sound()
        self.render_background()
        self.render_heart()

    def render_heart(self):
        self.surface.blit(self.heart, (self.heart_x, self.heart_y))
