from concurrent.futures import ThreadPoolExecutor
from math import floor
from random import randint

from pydub import AudioSegment
from pydub.playback import play
from pygame.image import load
from pygame.transform import scale

from .colorbg import ColorBg


executor = ThreadPoolExecutor(max_workers=1)


class HeartFace(ColorBg):
    def __init__(self, surface):
        super().__init__(surface)

        w = surface.get_width()
        h = surface.get_height()
        heart_w = floor(w / 1.5)
        heart_h = floor(h / 1.5)

        self.played = False
        self.voice = AudioSegment.from_wav('assets/heart{}.wav'.format(randint(1, 3)))
        self.duration = self.voice.duration_seconds
        self.heart = scale(load('assets/heart.svg'), (heart_w, heart_h))
        self.heart_x = (w / 2) - (heart_w / 2)
        self.heart_y = (h / 2) - (heart_h / 2)

    def render(self, event):
        self.play_voice()
        self.render_background()
        self.render_heart()

    def play_voice(self):
        if self.played:
            return

        self.played = True

        executor.submit(play, self.voice)

    def render_heart(self):
        self.surface.blit(self.heart, (self.heart_x, self.heart_y))
