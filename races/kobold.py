from races.base import RaceBase

class KoboldRace(RaceBase):
    name = "Kobold"
    desc = """Kobolds are some little reptilians dudes. They are not very strong, but
they are quite intelligent and are known traps makers."""

    dice = 6


    night_vision = True
    cold_resistance = 1
    heat_resistance = 60

    penalties = {
        "Lizard fingers of Kobolds make it difficult to carry a lot of stuff":
        "hero.carry_capacity = hero.carry_capacity - 5"
    }

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

    
