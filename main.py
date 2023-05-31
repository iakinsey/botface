from math import ceil

from pygame import init, quit, QUIT, KEYUP
from pygame.display import flip, set_mode
from pygame.event import poll
from pygame.time import get_ticks

from botface.faces.bsod import BSODFace
from botface.faces.music import MusicFace
from botface.faces.heart import HeartFace
from botface.faces.neutral import NeutralFace
from botface.faces.talking import TalkingFace
from botface.faces.emergency import EmergencyFace
from botface.faces.gigachad import GigachadFace
from botface.faces.uwu import UwuFace
from botface.faces.yes import YesFace
from botface.faces.no import NoFace


def start():
    init()
    surface = set_mode((1080, 1080))
    neutral = NeutralFace(surface)
    current_face = neutral
    neutral_revert_time = None

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
                current_face = TalkingFace(surface)
                neutral = NeutralFace(surface)
            elif ev.unicode == '8':
                current_face = HeartFace(surface)
                neutral = NeutralFace(surface)
            elif ev.unicode == '7':
                current_face = MusicFace(surface)
                neutral = current_face
            elif ev.unicode == '6':
                current_face = BSODFace(surface)
                neutral = NeutralFace(surface)
            elif ev.unicode == '5':
                current_face = EmergencyFace(surface)
                neutral = NeutralFace(surface)
            elif ev.unicode == '4':
                current_face = UwuFace(surface)
                neutral = NeutralFace(surface)
            elif ev.unicode == '3':
                current_face = GigachadFace(surface)
                neutral = NeutralFace(surface)
            elif ev.unicode == '2':
                current_face = NoFace(surface)
                neutral = NeutralFace(surface)
            elif ev.unicode == '1':
                current_face = YesFace(surface)
                neutral = NeutralFace(surface)





        if neutral_revert_time is None and hasattr(current_face, 'duration'):
            neutral_revert_time = ceil(get_ticks() + (current_face.duration * 1000))
        elif neutral_revert_time is not None and neutral_revert_time <= get_ticks():
            current_face = neutral
            neutral_revert_time = None

        current_face.render(ev)
        flip()

    quit()


if __name__ == "__main__":
    start()
