from concurrent.futures import ThreadPoolExecutor
from math import floor
from random import randint

from pydub import AudioSegment
from pydub.playback import play
from pygame import mixer, Color, Rect
from pygame.draw import circle
from pygame.image import load
from pygame.time import get_ticks
from pygame.transform import flip, scale

from .colorbg import ColorBg


executor = ThreadPoolExecutor(max_workers=1)


class TalkingFace(ColorBg):
    def __init__(self, surface):
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

        self.voice = AudioSegment.from_wav('assets/morusque_full.wav')
        self.eye_left = scale(eye, (eye_w, eye_h))
        self.width = width
        self.eye_x = eye_x
        self.eye_y = eye_y
        self.eye_r = eye_r
        self.eye_right = flip(self.eye_left, True, False)
        self.mouth_y = mouth_y
        self.played = False
        self.duration = randint(2, 5)

    def render(self, event):
        self.play_voice()
        self.render_background()
        self.render_eyes()
        self.render_mouth()

    def get_duration(self):
        return self.duration

    def play_voice(self):
        if self.played:
            return

        self.played = True
        voice_duration = self.voice.duration_seconds
        start = randint(0, floor(voice_duration - self.duration))
        end = start + self.duration
        stream = self.voice[start * 1000:end * 1000].fade_in(100).fade_out(100)

        executor.submit(play, stream)

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
