from pygame import mixer
import modules.volume as volume


def play_voice():
    mixer.init()
    mixer.music.load("sound.mp3")
    volume.set_max()
    mixer.music.play(loops=1)

    while mixer.music.get_busy():
        pass
