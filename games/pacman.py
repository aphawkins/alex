from microbit import *
import music

pacman_1 = Image(
         "07970:"
         "79997:"
         "99999:"
         "79997:"
         "07970")
pacman_2 = Image(
         "07970:"
         "79985:"
         "99972:"
         "79985:"
         "07970")
pacman_3 = Image(
         "07970:"
         "79970:"
         "99700:"
         "79970:"
         "07970")
pacman_4 = Image(
         "07950:"
         "79700:"
         "99200:"
         "79700:"
         "07950")
         
intro = [
    'b1:2', 'b2:2', 'b1:2', 'b2:2',
    'c2:2', 'c3:2', 'c2:2', 'c3:2',
    'b1:2', 'b2:2', 'b1:2', 'b2:2',
    'f#2:2', 'g#2:2', 'a#1:2', 'b2:2',
]

pacman_eat = [pacman_1, pacman_2, pacman_3, pacman_4, pacman_3, pacman_2]

music.play(intro)

while True:
    display.show(pacman_eat, delay=100)
