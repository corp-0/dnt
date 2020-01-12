from races.base import Base

class SkellyRace(Base):
    name = "Skelleton"
    desc = """Skelletons are undead warriors resucited by some evil dude who knows
necromancy!."""

    dice = 6

    night_vision = True
    cold_resistance = 1
    heat_resistance = 60
    
    names = [    
            "Snake Plisskill","Chris Rot","Chris Hellsworth","Killa Knightley","Elijah Woe","John Mallkillvich","Dorotty Gale","Travis Bikill",
            "Christian Bane","Pelvis Presley","Sofia Vergora","Idris Elbane","Boney Stark","Pelvis Costello","Indiana Bones","Hugh Grave",
            "Scary Poppins","Michael Bane Jordan","Arhuritis","Helter Skeletor","Severot Snape","Christian Bane","Clarence Marrow","Skully",
            "Abra Cadaver","Barnie Skinson","Rottingthon II","Hell 'n Boneham Carcass","Pelvis Presley","Olivia Wight","Jonah Kill","Elisablight Olsen",
            "Gary Sinews","Ewan McGregore","Woody Harrowson","Rick R. Mortis","Sarumarrow","Kristen Bane","Inigo Bonetoya","Steve Businew"
    ]