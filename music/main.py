from microbit import *
import jinglebells
import silentnight
import wewishyouamerrychristmas
import music

option = 1
display.show(option)

def play_music(option):
    if option == 1:
        musiclib = jinglebells
    elif option == 2:
        musiclib = silentnight
    else:
        musiclib = wewishyouamerrychristmas

    music.set_tempo(ticks=musiclib.ticks_per_beat, bpm=musiclib.bpm)
    music.play(musiclib.tune, wait=False, loop=False)
    display.scroll(musiclib.message)

while True:
    if button_a.was_pressed():
        option = option + 1
        if option > 3: option = 1
        display.show(option)
    elif button_b.was_pressed():
        play_music(option)