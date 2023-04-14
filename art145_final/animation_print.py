
from random import randrange
from time import sleep
from termcolor import colored

import sys

def animation_print_1(text: str, hold_dur: int = 10, type_speed: float = 0.003):
    for c in text:
        for i in range(hold_dur):
            sys.stdout.write(chr(randrange(33, 127)))
            sys.stdout.flush()
            sleep(type_speed)
            sys.stdout.write("\b")
            sys.stdout.flush()

        
        print(f"{c}", end='')
    print()

def animation_print_2(text: str, hold_dur: int = 10, type_speed: float = 0.05):
    for i, c in enumerate(text):
        for j in range(i):
            sys.stdout.write(chr(randrange(33, 127)))
            sys.stdout.flush()

        sleep(type_speed)
        sys.stdout.write("\b"*i)

    sys.stdout.write(text)
    print()

def animation_print_3(text: str, hold_dur: int = 20, type_speed: float = 0.03):
    for i in range(hold_dur):
        for c in text:
            sys.stdout.write(chr(randrange(33, 127)))
            sys.stdout.flush()
        sleep(type_speed)
        sys.stdout.write("\b"*len(text))
        sys.stdout.flush()
        
    print(text)

        


if __name__ == "__main__":
    print(colored("Bluecat", "light_red") + ": ", end='')
    animation_print_3("why does it feel different this time?")

    print(colored("Smaugy", "light_blue") + ": ", end='')
    animation_print_1("because he has learned to see it")

    animation_print_2("sound in you, waves in me")
