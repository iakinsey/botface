from math import floor
from pygame import Color, Rect


class ColorBg:
    def __init__(self, surface):
        width = surface.get_width()
        height = surface.get_height()
        sw = floor(width / 4)
        r = width % 4

        self.surface = surface
        self.bg_shapes = [
            (Color("#a99c7e"), Rect(0, 0, sw, height)),
            (Color("#881d14"), Rect(sw, 0, sw + r, height)),
            (Color("#3e4f64"), Rect(sw * 2, 0, sw, height)),
            (Color("#258d25"), Rect(sw * 3, 0, sw, height))
        ]

    def render_background(self):
        for shape in self.bg_shapes:
            self.surface.fill(*shape)
