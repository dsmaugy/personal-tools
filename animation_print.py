
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
        

print(colored("Smaugy", "light_blue") + ": ", end='')
animation_print_2("what do you want to create?")

print(colored("Bluecat", "light_red") + ": ", end='')
sleep(0.5)
animation_print_1("i'm not sure")
