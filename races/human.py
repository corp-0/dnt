from races.base import RaceBase

class HumanRace(RaceBase):
    name = "Human"
    desc = """Humans are the younger race to appear in this world, yet they are the more common to see.
    Humans are not very strong nor very intelligent, in comparison with other races and are quite fragile.
    Nonetheless, a human can always be an outstanding hero."""

    dice = 8

    night_vision = False
    cold_resistance = -30
    heat_resistance = 45


