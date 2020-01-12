from races.base import Base

class KoboldRace(Base):
    name = "Human"
    desc = """Kobolds are some little reptilians dudes. They are not very strong, but
they are quite intelligent and are known traps makers."""

    dice = 6

    night_vision = True
    cold_resistance = 1
    heat_resistance = 60

    
