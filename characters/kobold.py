from characters.base import Chara
import random

class Kobold(Chara):
    desc = """Kobolds are craven reptilian humanoids that commonly infest dungeons.
They make up for their physical ineptitude with a cleverness for trap making
"""    
    fame = 5

    names = [    
            "Ved", "Vod","Run","Marn","Mapla","Ohsi","Snepo","Nalli",
            "Erko","Zale","Natt","Sid","Nos","Regs","Narpu","Kagne",
            "Nirku","Zihru","Uba","Rekde","Koss","Nud","Tuv","Varn",
            "Mahse","Telte","Sullu","Nagu","Duvlu","Zuplu","Zug","Kon",
            "Ram","Nod","Vetra","Radra","Zepo","Zeggu","Snugge","Iro",
            "Mes","Kar","Zus","Snass","Gegri","Tihzi","Hilpi","Nolda",
            "Vogu","Ede","Snan","Snugs","Gags","Snik","Galtu","Olti",
            "Rupli","Kahsa","Kodu","Uggo"
            ]

    def __init__(self):
        args = [
            random.choice(self.names),
            None,
            7,
            15,
            9,
            8,
            7,
            8
        ]
        self.create_new_character(*args)