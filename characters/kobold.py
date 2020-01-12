from characters.base import Base
from races.kobold import KoboldRace
import random

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

name = random.choice(names)
race = KoboldRace
STR = 7
DEX = 15
CON = 9
INT = 8
WIS = 7
CHAR = 8

class Kobold(Base):
    desc = """Kobolds are craven reptilian humanoids that commonly infest dungeons.
They make up for their physical ineptitude with a cleverness for trap making
"""    
    fame = 5