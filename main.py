from math import ceil

from pygame.mixer import init as init_mixer


init_mixer()


from pygame import init, quit, Surface, QUIT, KEYUP, FULLSCREEN, SRCALPHA
from pygame.display import flip, set_mode
from pygame.event import poll
from pygame.mixer import Channel
from pygame.time import get_ticks

from botface.faces.bsod import BSODFace
from botface.faces.music import MusicFace
from botface.faces.heart import HeartFace
from botface.faces.neutral import NeutralFace
from botface.faces.talking import TalkingFace
from botface.faces.gigachad import GigachadFace
from botface.faces.surprise import SurpriseFace
from botface.faces.uwu import UwuFace
from botface.faces.yes import YesFace
from botface.faces.no import NoFace


def start():
    init()
    back_surface = set_mode((1080, 1080))
    surface = Surface((1080, 1080), SRCALPHA)
    channel = Channel(0)
    neutral = NeutralFace(surface)
    current_face = neutral
    neutral_revert_time = None

    back_surface.blit(surface, (0,0))
    while True:
        ev = poll()

        if ev.type == QUIT:
            break
        elif ev.type == KEYUP:
            if ev.unicode == 'q':
                break

            if ev.unicode == '0':
                current_face = NeutralFace(surface)
                neutral = current_face
            elif ev.unicode == '9':
                current_face = TalkingFace(surface, channel)
                neutral = NeutralFace(surface)
            elif ev.unicode == '8':
                current_face = HeartFace(surface, channel)
                neutral = NeutralFace(surface)
            elif ev.unicode == '7':
                current_face = MusicFace(surface)
                neutral = current_face
            elif ev.unicode == '6':
                current_face = SurpriseFace(surface)
                neutral = NeutralFace(surface)
            elif ev.unicode == '5':
                current_face = BSODFace(surface)
                neutral = NeutralFace(surface)
            elif ev.unicode == '4':
                current_face = UwuFace(surface)
                neutral = NeutralFace(surface)
            elif ev.unicode == '3':
                current_face = GigachadFace(surface)
                neutral = NeutralFace(surface)
            elif ev.unicode == '2':
                current_face = NoFace(surface, channel)
                neutral = NeutralFace(surface)
            elif ev.unicode == '1':
                current_face = YesFace(surface, channel)
                neutral = NeutralFace(surface)

        if neutral_revert_time is None and hasattr(current_face, 'duration'):
            neutral_revert_time = ceil(get_ticks() + (current_face.duration * 1000))
        elif neutral_revert_time is not None and neutral_revert_time <= get_ticks():
            current_face = neutral
            neutral_revert_time = None

        current_face.render(ev)
        back_surface.blit(surface, (0,0))
        flip()

    quit()


if __name__ == "__main__":
    start()
