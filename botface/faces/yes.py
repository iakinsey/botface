from pygame import Color, Rect
from pygame.image import load
from pygame.mixer import Sound
from pygame.transform import scale


from .audiomixin import AudioMixin


class YesFace(AudioMixin):
    sound = Sound('assets/yes.wav')

    def __init__(self, surface, channel):
        self.surface = surface
        self.w = surface.get_width()
        self.h = surface.get_height()
        self.duration = 5
        self.played = False

        yes = load('assets/yes.png')
        old_w = yes.get_width()
        old_h = yes.get_height()
        yes_w = self.h
        yes_h = old_h * (yes_w / old_w)

        self.yes = scale(yes, (yes_w, yes_h))
        self.yes_rect = self.yes.get_rect(center=(self.w / 2, self.h / 2))
        self.channel = channel

    def render(self, event):
        self.play_sound()
        self.render_background()
        self.render_yes()

    def render_background(self):
        self.surface.fill(Color("#FFFFFF"), Rect(0, 0, self.w, self.h))

    def render_yes(self):
        self.surface.blit(self.yes, self.yes_rect)
