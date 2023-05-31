from pygame.image import load
from pygame.transform import scale

class GigachadFace:
    def __init__(self, surface):
        w = surface.get_width()
        h = surface.get_height()

        self.surface = surface
        self.face = scale(load('assets/gigachad.jpg'), (w, h))
        self.duration = 6

    def render(self, event):
        self.surface.blit(self.face, (0, 0))
