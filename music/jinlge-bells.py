# Add your Python code here. E.g.
from microbit import *

import music
music.set_tempo(ticks=4, bpm=120)
jingle = [
    'e:2','e:2','e:4',
    'e:2','e:2','e:4',
    'e:2','g:2','c','d',
    'e:8','f:2','f:2','f:3',
    'f:1','f:2','e:2',
    'e:2','e:2','e:1',
    'e:2','d:2','d:2',
    'e:2','d:4','g:4',
    'e:2','e:2','e:4',
    'e:2','e:2','e:4',
    'e:2','g:2','c','d',
    'e:8','f:2','f:2','f:2',
    'f:2','f:2','e:2',
    'e:2','e:1','e:1',
    'g:2','g:2','f:2',
    'd:2','c:4',
]
music.play(jingle,wait=False,loop=False)