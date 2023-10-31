from concurrent.futures import ThreadPoolExecutor
from math import floor
from random import randint

from pygame import Color, Rect
from pygame.image import load
from pygame.mixer import Sound
from pygame.time import get_ticks
from pygame.transform import flip, scale

from .colorbg import ColorBg
from .audiomixin import AudioMixin


executor = ThreadPoolExecutor(max_workers=1)


class TalkingFace(AudioMixin, ColorBg):
    sounds = [
        Sound('assets/talking2.mp3'),
        Sound('assets/talking3.mp3'),
        Sound('assets/talking4.mp3'),
        Sound('assets/talking5.mp3')
    ]

    def __init__(self, surface, channel):
        super().__init__(surface)

        width = surface.get_width()
        height = surface.get_height()
        sw = floor(width / 4)
        eye_x = floor(sw * 1.05)
        eye_y = floor(height / 3.1)
        eye_r = floor(height / 11)

        eye = load('assets/happy_eye.svg')
        old_w = eye.get_width()
        old_h = eye.get_height()

        eye_w = floor(height / 11) * 2
        eye_h = old_h * (eye_w / old_w)

        mouth_y = height - eye_y

        self.eye_left = scale(eye, (eye_w, eye_h))
        self.width = width
        self.eye_x = eye_x
        self.eye_y = eye_y
        self.eye_r = eye_r
        self.eye_right = flip(self.eye_left, True, False)
        self.mouth_y = mouth_y
        self.played = False
        self.duration = randint(2, 5)
        self.sound = self.sounds[self.duration - 2]
        self.channel = channel

    def render(self, event):
        self.play_sound()
        self.render_background()
        self.render_eyes()
        self.render_mouth()

    def get_duration(self):
        return self.duration

    def render_eyes(self):
        self.surface.blit(self.eye_left, (self.eye_x-self.eye_r, self.eye_y))
        self.surface.blit(self.eye_right, ((self.width - self.eye_x) - self.eye_r, self.eye_y))

    def render_mouth(self):
        ms = get_ticks() % 100

        if 66 < ms <= 100:
            self.do_render_mouth(250)
        elif 33 < ms < 66:
            self.do_render_mouth(150)
        else:
            self.do_render_mouth(75)

    def do_render_mouth(self, height):
        self.surface.fill(
            Color("#000000"),
            Rect(0, self.mouth_y - floor(height / 2), self.width, height)
        )
