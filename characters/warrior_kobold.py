from characters.kobold import Kobold
import random

class Warrior_Kobold(Kobold):
    desc = """Kobolds are craven reptilian humanoids that commonly infest dungeons.
Warrior Kobolds are Kobolds who studied the art of fighting from very early in their lifes.
"""    
    fame = 7

    def __init__(self):
        args = [
            random.choice(self.names),
            None,
            12,
            17,
            12,
            9,
            10,
            10
        ]
        self.create_new_character(*args)