from print_utils import animation_print_1, animation_print_3, animation_print_2, permutate_string, animation_print_1_uniform

from time import sleep
from typing import Callable, MutableSet, List
from termcolor import colored
from datetime import datetime
from random import choice


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

TIME_CONVERSION = "ᛯ�␢ᚡ▓�ᚸ░ᛩ⚳"

class Chatter():

    max_name_width = 0

    def __init__(self, name: str, color: str, chat_style: Callable, hold_dur=8, type_speed=0.01) -> None:
        self._color = color
        self._name = name
        self._animation_print = chat_style
        self._hold_dur = hold_dur
        self._type_speed = type_speed
        self._bot = True if name == "*" else False

        Chatter.max_name_width = max(len(self._name), Chatter.max_name_width)

    def _get_chat_prefix(self):
        current_ts = datetime.now().strftime("%H:%M:%S")
        ts_string = "["
        for c in current_ts:
            if c.isdigit():
                ts_string += TIME_CONVERSION[int(c)]
            else:
                ts_string += c
        ts_string += "]" + " "*5

        display_name = f"<{self._name}>" if not self._bot else f"  {self._name}"
        display_attrs = ["bold", "underline"] if not self._bot else ["bold"]

        return ts_string + " "*(Chatter.max_name_width - len(self._name)) + colored(display_name, self._color, attrs=display_attrs) + ": "

    def say(self, text: str, newline=True, prompt=True, delay=0, pretext=""):
        print_newline = newline and not prompt
        print(self._get_chat_prefix() + pretext, end="")

        self._animation_print(text, newline=print_newline, hold_dur=self._hold_dur, type_speed=self._type_speed, delay=delay)

        if prompt:
            input("")


class RandomChatter(Chatter):

    def __init__(self, names, color: str, chat_style: Callable, hold_dur=20, type_speed=0.05) -> None:
        selected_name = choice(list(names))
        names.remove(selected_name)
        super().__init__(selected_name, color, chat_style, hold_dur, type_speed)

    def say(self, text: str, newline=True, prompt=True, delay=0):
        return super().say(text, newline, prompt, delay)

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
    animation_print_1("connecting to [����:c0�8:0�01:0:�:ff�f:4��9:28�e]:6667", newline=True, delay=2)
    animation_print_1("connected!", newline=True, delay=1)

    animation_print_3(IRC_WELCOME, newline=True)
    animation_print_1(IRC_MOTD, type_speed=0.0005, newline=True)
    animation_print_1("-"*105, newline=True, delay=5)

def join_personal_channel(system: Chatter):
    system.say(f"automatically joining channel #❂❂❂❂❂...", prompt=False)
    system.say(f"joined channel #❂❂❂❂❂", prompt=False)
    system.say("�̶͑̊̓☐ users currently online", newline=False, prompt=True)

def join_world_channel(system: Chatter):
    system.say(f"automatically joining channel #❦❦❦❦❦...", prompt=False)
    system.say(f"joined channel #❦❦❦❦❦", prompt=False)
    system.say(f"{permutate_string('☐�̶͑̊̓𐠢 ')} users currently online", newline=False, prompt=True)

def simulate_world_chat(system: Chatter, world_channel_names):
    num_chatters = len(world_channel_names)
    world_chatters = [RandomChatter(world_channel_names, "light_green", animation_print_3) for i in range(num_chatters)]
    
    join_world_channel(system)
    world_chatters[0].say("if you could start your life over as a child, would you?", prompt=True)
    world_chatters[1].say("yes.", prompt=True)
    world_chatters[1].say("I would do it to see my mom again.", prompt=True)
    world_chatters[2].say("no. the thought of going back and not seeing my daughter any more physically hurts", prompt=True)
    world_chatters[3].say("but then I would have to relive my childhood...", prompt=True)
    world_chatters[3].say("so no", prompt=True)

    join_world_channel(system)
    world_chatters[4].say("after death, you wake up again in a child's body. what do you do differently?", prompt=True)
    world_chatters[5].say("Stand up for myself and kick up a fuss")
    world_chatters[6].say("I'll be a lot kinder to others")
    world_chatters[7].say("It would kill me")
    world_chatters[7].say("to have memories of my family, wife and kids")
    world_chatters[7].say("but knowing I will never see them again...")
    world_chatters[7].say("no thanks")

    join_world_channel(system)
    world_chatters[8].say("do you ever feel like an empty shell?")
    world_chatters[9].say("yes")
    world_chatters[9].say("my wife left me 13 months ago. I still pretend that she's around.")
    world_chatters[9].say("no one knows shes gone.")
    world_chatters[10].say("yes, drinking didn't help...")
    world_chatters[10].say("quite the oppposite")
    world_chatters[10].say("running saved my life though")

    join_world_channel(system)
    world_chatters[11].say("how do you carry the emptiness you feel inside?")
    world_chatters[12].say("by having someone by my side to remind me that I'm not empty")
    world_chatters[13].say("Emptiness is weightless. Carrying it isn't difficult")
    world_chatters[14].say("in a jar")
    
def list_say(chatter: Chatter, phrases: List[str], pretext: str = ""):
    for phrase in phrases:
        chatter.say(phrase, pretext=pretext)

if __name__ == "__main__":
    # gateway_bootup()

    world_channel_names = {"hijan", "KuraManga", "queeblo154", "pal_", "vultix522", "gaoelan", "koinoyokan", 
                           "spectralanimosity", "Zingles", "spinchev", "wislser", "orangezhao35", 
                           "moonlover41", "blacktabby74", "7sages"}
    user_smaugy = Chatter("smaugy", "light_red", animation_print_3, 20, 0.09)
    user_smaugy_quick = Chatter("smaugy", "light_red", animation_print_1, 5, 0.009)

    user_agarthus = Chatter("agarthus", "light_red", animation_print_3, 20, 0.05)
    user_system = Chatter("*", "light_cyan", animation_print_2, type_speed=0.008)

    # simulate_world_chat(user_system, world_channel_names)
    # join_personal_channel(user_system)

    # world_user_one = RandomChatter(world_channel_names, "light_green", animation_print_3)
    # world_user_one.say("bruh")
    # world_user_one.say("ok i pull up, hop out at the after party")
    
    # world_user_two = RandomChatter(world_channel_names, "light_green", animation_print_3)
    # world_user_two.say("this monitor is serial, so you would need a D or whatever")


    # smaugy stuff
    # user_smaugy.say("I dreamed I was an electron on an overhead power line", prompt=True)
    # user_smaugy.say("hurtling across transmission towers placed in empty plains", prompt=True)
    # user_agarthus.say("where were you going?", prompt=True)
    # user_smaugy.say("to wherever the line ended", prompt=True)
    # user_smaugy.say("when i was a kid, i really liked to scrunch up the corner of my blanket", prompt=True)
    # user_smaugy.say("then i would hold it close to my face", prompt=True)
    # user_smaugy.say("it felt comforting", prompt=True)
    # user_smaugy.say("i also cried a lot as a kid")
    # user_smaugy.say("my parents didnt like that")
    # user_smaugy.say("i didnt like it")
    # user_smaugy.say("because my parents didnt like it")
    
    want_list = ["to paint my nails", "to dye my hair", "to eat a cheeseburger with pickles", "to eat a cheeseburger with no pickles", "to be taller", "to not disappoint",
                 "to love my family", "to not be annoying", "to reach grandmaster", "to reach diamond", "to fix my resume", "to make my friends laugh", "to play piano"]
    
    wave_list = ["transverse waves", "radio waves", "longitudinal waves", "hand waves", "sound waves", 
                 "zombie waves", "ocean waves", "goodbye waves", "hello waves"]
    
    like_list = ["turning on my computer", "staying connected", "when it's cold and sunny", "walking to the beat", "tapping to the beat", "talking online", 
                 "my stuffed animals", "the airport", "using the subway", "winning as a team", "6th period physics lab", "driving my friends", "getting driven by friends", 
                 "windows vista", "watching people eat", "reading youtube comments"]
    
    begin_list = ["on a random seed", "surrounded by love", "surrounded by books", "in a random seed", "to explore (on a random seed)", "a workout routine", "to think about my future", 
                  "a better sleep schedule", "eating more", "conscious listening"]

    
    # list_say(user_smaugy_quick, want_list, "i want ")
    # list_say(user_smaugy_quick, wave_list)
    # list_say(user_smaugy_quick, like_list, "i like ")
    # list_say(user_smaugy_quick, begin_list, "i will begin ")

    # user_smaugy.say("", False, True)

    # join_personal_channel(user_system)
    # user_smaugy_quick.say("A system of cells interlinked within", prompt=False)
    # user_smaugy_quick.say("Cells interlinked within cells interlinked", prompt=False)
    # user_smaugy_quick.say("Within one stem. And dreadfully distinct", prompt=False)
    # user_smaugy_quick.say("Against the dark, a tall white fountain played", prompt=False)
    # user_smaugy_quick.say("...")
    # user_smaugy.say("am I special?")
    # user_agarthus.say("do you want to be special?")

    # TODO: make a mode where timings are all exactly the same regardless of string length
    # TODO: re-record affirmations with more prompts and with randomization

    affirmations_set = set()
    user_smaugy_uniform = Chatter("smaugy", "light_red", animation_print_1_uniform, hold_dur=25, type_speed=1.0)

    for want in want_list:
        affirmations_set.add(("i want ", want))
    for like in like_list:
        affirmations_set.add(("i like ", like))
    for begin in begin_list:
        affirmations_set.add(("i will begin ", begin))

    while len(affirmations_set) > 0:
        rand = choice(list(affirmations_set))
        affirmations_set.remove(rand)

        user_smaugy_uniform.say(text=rand[1], prompt=False, delay=0.3, pretext=rand[0])



    
