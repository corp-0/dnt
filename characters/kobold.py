from characters.base import Base
from races.kobold import KoboldRace
import random

class Kobold(Base):
    desc = """Kobolds are craven reptilian humanoids that commonly infest dungeons.
They make up for their physical ineptitude with a cleverness for trap making
"""
    fame = 5
    race = KoboldRace()

    att = {
        "STR": 7,
        "DEX": 15,
        "CON": 9,
        "INT": 8,
        "LCK": 7,
        "CHAR": 8
    }