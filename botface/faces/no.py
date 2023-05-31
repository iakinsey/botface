from concurrent.futures import ThreadPoolExecutor

from pydub import AudioSegment
from pydub.playback import play
from pygame import Color, Rect
from pygame.image import load
from pygame.transform import scale


executor = ThreadPoolExecutor(max_workers=1)


class NoFace:
    def __init__(self, surface):
        self.surface = surface
        self.w = surface.get_width()
        self.h = surface.get_height()
        self.duration = 5
        self.voice = AudioSegment.from_wav('assets/no.wav')
        self.played = False

        no = load('assets/no.png')
        old_w = no.get_width()
        old_h = no.get_height()
        no_w = self.h
        no_h = old_h * (no_w / old_w)

        self.no = scale(no, (no_w, no_h))
        self.no_rect = self.no.get_rect(center=(self.w / 2, self.h / 2))

    def render(self, event):
        self.play_voice()
        self.render_background()
        self.render_no()

    def render_background(self):
        self.surface.fill(Color("#FFFFFF"), Rect(0, 0, self.w, self.h))

    def render_no(self):
        self.surface.blit(self.no, self.no_rect)

    def play_voice(self):
        if self.played:
            return

        self.played = True

        executor.submit(play, self.voice)
