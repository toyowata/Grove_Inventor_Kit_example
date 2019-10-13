from microbit import *
import music

notes = ["c4:4"]
while True:
    if button_a.is_pressed():
        music.play(notes)
    elif button_b.is_pressed():
        music.play(music.DADADADUM)
