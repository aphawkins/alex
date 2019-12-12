from microbit import *
import jinglebells
import wewishyouamerrychristmas
import music
music.set_tempo(ticks=4, bpm=120)

while True:
    if button_a.is_pressed():
        music.play(jinglebells.tune,wait=False,loop=False)
        display.scroll(jinglebells.message)
    elif button_b.is_pressed():
        music.play(wewishyouamerrychristmas.tune,wait=False,loop=False)
        display.scroll(wewishyouamerrychristmas.message)
    