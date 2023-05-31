from concurrent.futures import ThreadPoolExecutor


from pydub import AudioSegment
from pydub.playback import play
from pygame import Color, Rect
from pygame.font import Font
from pygame.time import get_ticks


TEXT = [
    "",
    "",
    "",
    "NATIONAL ALERT",
    "",
    "",
    "A Primary Entry Point System has issued an Emergency Action Notification for the following counties: Los Angeles. Effective until 01/18/38 19:14:07 PST.",
    "",
    "Primary Entry Point System",
    "",
    "Issued an",
    "",
    "Emergency Action",
    "Notification"
]


FONT = (255, 255, 255)
executor = ThreadPoolExecutor(max_workers=1)


class EmergencyFace:
    def __init__(self, surface):
        self.surface = surface

        self.w = surface.get_width()
        self.h = surface.get_height()
        self.duration = 2
        self.font_size = 48
        self.tone = AudioSegment.from_wav('assets/800hz.wav')[0:self.duration * 1000]
        font = Font("assets/luximono.ttf", self.font_size)
        self.text = [font.render(text.encode(), False, FONT) for text in TEXT]
        self.scroll_start = 3300
        self.scroll_end = -3000
        self.scroll_current = self.scroll_start
        self.played = False

    def render(self, event):
        self.play_tone()
        self.render_background()
        self.render_text()

    def play_tone(self):
        if self.played:
            return

        self.played = True

        executor.submit(play, self.tone)


    def render_background(self):
        self.surface.fill(Color("#000000"), Rect(0, 0, self.w, self.h))

    def render_text(self):
        position = 10, 10
        ms = get_ticks()

        print(ms)
        for line in range(len(self.text)):
            text = self.text[line]
            vertical_pos = position[1] + (line * self.font_size) + (15 * line)

            # Add marquee 3300 to -3000
            if TEXT[line].startswith("A"):
                if self.scroll_current <= self.scroll_end:
                    self.scroll_current = self.scroll_start

                text_rect = text.get_rect(center=(self.scroll_current, vertical_pos))

                if ms % 2 == 0:
                    self.scroll_current -= 1
            else:
                text_rect = text.get_rect(center=(self.w / 2, vertical_pos))

            self.surface.blit(text, text_rect)
