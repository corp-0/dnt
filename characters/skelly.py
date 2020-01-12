from characters.base import Chara
import random

class Skelly(Chara):
    desc = """Spooky scary skelletons!"""    
    fame = 10

    names = [    
            "Snake Plisskill","Chris Rot","Chris Hellsworth","Killa Knightley","Elijah Woe","John Mallkillvich","Dorotty Gale","Travis Bikill",
            "Christian Bane","Pelvis Presley","Sofia Vergora","Idris Elbane","Boney Stark","Pelvis Costello","Indiana Bones","Hugh Grave",
            "Scary Poppins","Michael Bane Jordan","Arhuritis","Helter Skeletor","Severot Snape","Christian Bane","Clarence Marrow","Skully",
            "Abra Cadaver","Barnie Skinson","Rottingthon II","Hell 'n Boneham Carcass","Pelvis Presley","Olivia Wight","Jonah Kill","Elisablight Olsen",
            "Gary Sinews","Ewan McGregore","Woody Harrowson","Rick R. Mortis","Sarumarrow","Kristen Bane","Inigo Bonetoya","Steve Businew"
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