from pygame import Color, Rect
from pygame.font import Font


TEXT = [
    'A problem has been detected and Windows has been shut down to prevent damage',
    'to your computer.',
    ' ',
    'The problem seems to be caused by the following file: SPCMDCON.SYS',
    ' ',
    'PAGE_FAULT_IN_NONPAGED_AREA',
    " ",
    "If this is the first time you've seen this stop error screen,",
    "restart your computer. if this screen appears again, follow",
    "these steps:",
    " ",
    "Check to make sure any new hardware or software is properly installed.",
    "I this is a new installation, ask your hardware or software manufacturer",
    "for and Windows updates you might need.",
    " ",
    "If problems continue, disable or remove any newly installed hardware",
    "or software. Disable BIOS memory options such as caching or shadowing.",
    "If you need to use Safe Mode to remove or disable components, restart",
    "your computer, press F8 to select Advanced Startup Options, and then",
    "select Safe Mode.",
    " ",
    "Technical information:",
    " ",
    "*** STOP: 0x000000FE (0x00000008, 0x000000006, 0x00000009, 0x847075cc)",
    "*** SPCMDCON.SYS - Address 0000009 base at FBFE5000, DateStamp 3d5dd67c"
]

BG = (0, 0, 51)
FONT = (255, 255, 255)


class BSODFace:
    def __init__(self, surface):
        self.surface = surface

        self.w = surface.get_width()
        self.h = surface.get_height()
        self.duration = 10
        self.font_size = int(self.h * 0.02)
        font = Font("assets/lucida_console.ttf", self.font_size)
        self.text = [font.render(text.encode(), False, FONT) for text in TEXT]

    def render(self, event):
        self.render_background()
        self.render_text()

    def render_background(self):
        self.surface.fill(Color("#000082"), Rect(0, 0, self.w, self.h))

    def render_text(self):
        position = 10, 10

        for line in range(len(self.text)):
            self.surface.blit(self.text[line], (position[0], position[1] + (line * self.font_size)+(15 * line)))
