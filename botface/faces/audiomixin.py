#from concurrent.futures import ThreadPoolExecutor

#executor = ThreadPoolExecutor(max_workers=1)


class AudioMixin:
    playing = False

    def play_sound(self):
        if self.playing:
            return

        try:
            self.channel.stop()
        except:
            pass

        self.playing = True
        self.channel.play(self.sound)
        #executor.submit(self.channel.play, self.sound)
