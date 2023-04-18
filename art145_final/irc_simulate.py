from print_utils import animation_print_1, animation_print_3, animation_print_2, permutate_string

from time import sleep
from typing import Callable
from termcolor import colored


IRC_WELCOME = """
                         __                                                      __               
                        |  \                                                    |  \\
 __   __   __   ______  | $$  _______   ______   ______ ____    ______         _| $$_     ______
|  \ |  \ |  \ /      \ | $$ /       \ /      \ |      \    \  /      \       |   $$ \   /      \\
| $$ | $$ | $$|  $$$$$$\| $$|  $$$$$$$|  $$$$$$\| $$$$$$\$$$$\|  $$$$$$\       \$$$$$$  |  $$$$$$\\
| $$ | $$ | $$| $$    $$| $$| $$      | $$  | $$| $$ | $$ | $$| $$    $$        | $$ __ | $$  | $$
| $$_/ $$_/ $$| $$$$$$$$| $$| $$_____ | $$__/ $$| $$ | $$ | $$| $$$$$$$$        | $$|  \| $$__/ $$
 \$$   $$   $$ \$$     \| $$ \$$     \ \$$    $$| $$ | $$ | $$ \$$     \         \$$  $$ \$$    $$
  \$$$$$\$$$$   \$$$$$$$ \$$  \$$$$$$$  \$$$$$$  \$$  \$$  \$$  \$$$$$$$          \$$$$   \$$$$$$ 
"""

IRC_MOTD = """
   ▄███████▄    ▄████████     ███        ▄█    █▄     ▄██████▄     ▄████████  ▄█     ▄████████  ▄████████ 
  ███    ███   ███    ███ ▀█████████▄   ███    ███   ███    ███   ███    ███ ███    ███    ███ ███    ███ 
  ███    ███   ███    ███    ▀███▀▀██   ███    ███   ███    ███   ███    █▀  ███▌   ███    ███ ███    █▀  
  ███    ███   ███    ███     ███   ▀  ▄███▄▄▄▄███▄▄ ███    ███   ███        ███▌  ▄███▄▄▄▄██▀ ███        
▀█████████▀  ▀███████████     ███     ▀▀███▀▀▀▀███▀  ███    ███ ▀███████████ ███▌ ▀▀███▀▀▀▀▀   ███        
  ███          ███    ███     ███       ███    ███   ███    ███          ███ ███  ▀███████████ ███    █▄  
  ███          ███    ███     ███       ███    ███   ███    ███    ▄█    ███ ███    ███    ███ ███    ███ 
 ▄████▀        ███    █▀     ▄████▀     ███    █▀     ▀██████▀   ▄████████▀  █▀     ███    ███ ████████▀ 
                                                                                    ███    ███          
"""

DESIGN_ONE = """
      ____________
     /\  ________ \\
    /  \ \______/\ \\
   / /\ \ \  / /\ \ \\
  / / /\ \ \/ / /\ \ \\
 / / /__\_\/ / /__\_\ \\
/ /_/_______/ /________\\
\ \ \______ \ \______  /
 \ \ \  / /\ \ \  / / /
  \ \ \/ / /\ \ \/ / /
   \ \/ / /__\_\/ / /
    \  / /______\/ /
     \/___________/
"""

DESIGN_TWO = """
  _______________________________
 /\                              \\
/++\    __________________________\\
\+++\   \ ************************/
 \+++\   \___________________ ***/
  \+++\   \             /+++/***/
   \+++\   \           /+++/***/
    \+++\   \         /+++/***/
     \+++\   \       /+++/***/
      \+++\   \     /+++/***/
       \+++\   \   /+++/***/
        \+++\   \ /+++/***/
         \+++\   /+++/***/
          \+++\ /+++/***/
           \+++++++/***/
            \+++++/***/
             \+++/***/
              \+/___/
"""

DESIGN_THREE = """

"""
GLITCH_MESSAGE = """Y_^‹Mð3Íè] ‹å]Ãè	 ÌÌÌÌÌÌÌÌÌÌÌÌÌÌÌU‹ìjÿhN¢R d¡    
Pì¸¡ˆÄ\ 3Å‰EðVWPEôd£    
¡àõS WÀ…dÿÿÿ‰…hÿÿÿ¶äõS Ç…tÿÿÿ    Ç…xÿÿÿÇ…|ÿÿÿˆ…lÿÿÿÆ…mÿÿÿ E„ÇE€ÇE”ÇE˜
ÇE„infoÆEˆ ¡èõS E ‰E f¡ìõS f‰E¤¶îõS ÇEœ   ÇE°   ÇE´   ˆE¦ÆE§ ¡ðõS E¼‰E¼¶ôõS ÇE¸   ÇEÌ   ÇEÐ
ˆEÀÆEÁ ¡øõS EØ‰EØ¶üõS ÇEÔ   ÇEè   ÇEì   ˆEÜÆEÝ j,ÇEü   µdÿÿÿ}ðè0Y ƒÄ‰…\ÿÿÿ‰ ‰@‰@fÇ@£<Å] ÆEü;÷„Ú   fVP…<ÿÿÿ¹<Å] Pèýê
ó~ ‹@fÖ…Hÿÿÿ‰…Pÿÿÿ„À…–   =@Å] ]tÑ„Ü   ¡<Å] ‰…`ÿÿÿÇ…Tÿÿÿ<Å] j,ÆEüÇ…Xÿÿÿ    èœX ‹øƒÄ‰½Xÿÿÿ‹V‰OORÆEüèï 
‹…`ÿÿÿ¹<Å] WÿµLÿÿÿ‰ÿµHÿÿÿ‰G‰GfÇG  ÆEüÇ…Xÿÿÿ
èÝ }ðƒÆ;÷t‹…\ÿÿÿé(ÿÿÿh€!A jj…dÿÿÿÇEüÿÿÿÿPèýV hà­S è‚Z ƒÄ‹Môd‰
"""

class Chatter():

    max_name_width = 0

    def __init__(self, name: str, color: str, chat_style: Callable, hold_dur=8, type_speed=0.01) -> None:
        self._color = color
        self._name = name
        self._animation_print = chat_style
        self._hold_dur = hold_dur
        self._type_speed = type_speed

        Chatter.max_name_width = max(len(self._name), Chatter.max_name_width)

    def say(self, text: str, prompt=True):
        print(colored(self._name, self._color, attrs=["bold", "underline"]) + " "*(Chatter.max_name_width - len(self._name)) + ": ", end="")
        self._animation_print(text, newline=False, hold_dur=self._hold_dur, type_speed=self._type_speed)

        if prompt:
            input()

def gateway_bootup():
    animation_print_1("", delay=2)
    animation_print_1(GLITCH_MESSAGE[0:10], newline=True, delay=1.5)
    animation_print_1(permutate_string(GLITCH_MESSAGE[0:10]), newline=True, delay=1.5)
    animation_print_1(permutate_string(GLITCH_MESSAGE[10:25]), newline=True, delay=1.5)
    for i in range(6):
        animation_print_1(".", newline=True, delay=0.8)
    animation_print_1(permutate_string(GLITCH_MESSAGE[10:25]) + "...", newline=True, delay=0.7)

    
    for i in range(5):
        animation_print_1(permutate_string(GLITCH_MESSAGE), hold_dur=2, type_speed=0.0003, newline=True, delay=0.4)

    for i in range(15):
        animation_print_1(permutate_string(GLITCH_MESSAGE), hold_dur=1, type_speed=0.0003, newline=True, delay=0.01)

    for i in range(20):
        animation_print_1(permutate_string(GLITCH_MESSAGE), hold_dur=1, type_speed=0.00005, newline=True, delay=0.001)

    animation_print_1(". . .", hold_dur=1,  type_speed=1, newline=True, delay=1)
    animation_print_1("\n\n", hold_dur=1,  type_speed=1, newline=True, delay=1)
    animation_print_1(DESIGN_ONE, newline=True, type_speed=0.001, delay=1.3)
    animation_print_1("\n\n", hold_dur=1,  type_speed=1, newline=True, delay=1)

    animation_print_1("system bootup complete...", newline=True, delay=1.5)
    animation_print_1("starting gateway irc client...", newline=True, delay=1)
    animation_print_1("started!", newline=True, delay=0.2)
    animation_print_1("connecting to [ffff:c0a8:0001:0:0:ffff:47e9:282e]:6667", newline=True, delay=2)
    animation_print_1("connected!", newline=True, delay=1)

    animation_print_3(IRC_WELCOME, newline=True)
    animation_print_1(IRC_MOTD, type_speed=0.0005, newline=True)


if __name__ == "__main__":
    # gateway_bootup()

    user_smaugy = Chatter("smaugy", "light_red", animation_print_3, 20, 0.1)
    user_agarthus = Chatter("agarthus", "light_red", animation_print_1)

    # user_smaugy.say("i tried beating a moonfish in a race")
    # user_agarthus.say("is that so?")
    user_agarthus.say("look, don't be the kid i aint with throw in the towel i know dont make me reload i marry my")

