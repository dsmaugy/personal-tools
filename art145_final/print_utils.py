
from random import randrange, random
from time import sleep
from termcolor import colored

import sys

def get_normalized_random(n: float) -> float:
    dec_place = 0
    while n * 10 < 1:
        n *= 10
        dec_place += 1
    dec_place += 1

    scaling = 2 * pow(10, -dec_place)
    offset = scaling / -2

    return random() * scaling + offset

def animation_print_1(text: str, hold_dur: int = 5, type_speed: float = 0.005, newline: bool = False, delay: float = 0.0):
    for c in text:
        if c != "\n":
            for _ in range(hold_dur):            
                sys.stdout.write(chr(randrange(33, 127)))
                sys.stdout.flush()
                sleep(type_speed + get_normalized_random(type_speed))
                sys.stdout.write("\b")
                sys.stdout.flush()

        print(f"{c}", end='')
    if newline:
        print()

    sleep(delay) 

def animation_print_2(text: str, hold_dur: int = 10, type_speed: float = 0.05,  newline: bool = False, delay: float = 0.0):
    for i, c in enumerate(text):
        for j in range(i):
            sys.stdout.write(chr(randrange(33, 127)))
            sys.stdout.flush()

        sleep(type_speed)
        sys.stdout.write("\b"*i)

    sys.stdout.write(text)
    sys.stdout.flush()
    
    if newline:
        print()

    sleep(delay) 

def animation_print_3(text: str, hold_dur: int = 20, type_speed: float = 0.03, newline: bool = False, delay: float = 0.0):
    for _ in range(hold_dur):
        for _ in text:
            sys.stdout.write(chr(randrange(33, 127)))
            sys.stdout.flush()
        sleep(type_speed)
        sys.stdout.write("\b"*len(text))
        sys.stdout.flush()
    
    term = "\n" if newline else ""
    print(text, end=term)
    sleep(delay)

def permutate_string(text: str) -> str:
    permutated_str = ""
    for _ in text:
        permutated_str += text[randrange(0, len(text))]
    return permutated_str



if __name__ == "__main__":
    print(get_normalized_random(0.00002))
    # print(colored("Bluecat", "light_red") + ": ", end='')
    # animation_print_3("why does it feel different this time?")

    # print(colored("Smaugy", "light_blue") + ": ", end='')
    # animation_print_1("because he has learned to see it")

    # animation_print_2("sound in you, waves in me")
