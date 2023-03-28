
from random import randrange
from time import sleep
from termcolor import colored

import sys

def animation_print(text: str, hold_dur: int = 10, type_speed: float = 0.003):
    for c in text:
        for i in range(hold_dur):
            print(chr(randrange(33, 127)), end='')
            sys.stdout.flush()
            sleep(type_speed)
            print("\b", end='')
            sys.stdout.flush()

        
        print(f"{c}", end='')
    print()
        

print(colored("Smaugy", "light_blue") + ": ", end='')
animation_print("what do you want to create?")
