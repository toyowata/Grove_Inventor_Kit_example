from microbit import *

def create_bar(value, max_val):
    img = ""
    for i in range(5):
        str = "00000:"
        leftovers = (max_val/5)
        if (value > leftovers*(5-i)):
            str = "99999:"
        elif (value > (leftovers*(4-i) + (leftovers/6)*5)):
            str = "59995:"
        elif (value > (leftovers*(4-i) + (leftovers/6)*4)):
            str = "09990:"
        elif (value > (leftovers*(4-i) + (leftovers/6)*3)):
            str = "05950:"
        elif (value > (leftovers*(4-i) + (leftovers/6)*2)):
            str = "00900:"
        elif (value > (leftovers*(4-i) + (leftovers/6)*1)):
            str = "00500:"
        img += str
    return Image(img)

while True:
    ain = pin0.read_analog()
    display.show(create_bar(ain, 700))
    sleep(10)