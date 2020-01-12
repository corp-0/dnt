from characters.base import CharacterBase
from races.skelly import SkellyRace
import random

class Skelly(CharacterBase):
    desc = """Spooky scary skelletons!"""    
    fame = 10
    race = SkellyRace()

    att = {
        "STR": 7,
        "DEX": 15,
        "CON": 9,
        "INT": 8,
        "LCK": 7,
        "CHAR": 8
    }