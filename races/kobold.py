from races.base import Base

class KoboldRace(Base):
    name = "Kobold"
    desc = """Kobolds are some little reptilians dudes. They are not very strong, but
they are quite intelligent and are known traps makers."""

    dice = 6

    night_vision = True
    cold_resistance = 1
    heat_resistance = 60

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

    
