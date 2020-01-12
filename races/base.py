"""
Base class for races
"""
from races.body import BodyBase

class Base():
    name = str()
    desc = str()

    dice = int()

    night_vision = bool()
    cold_resistance = int()
    heat_resistance = int()

    bonuses = dict()
    penalties = dict()

    def add_bonuses(self, character):
        for attribute in self.bonuses.keys():
            character.att[attribute] = character.att[attribute] + self.bonuses[attribute]

    def add_penalties(self, character):
        for attribute in self.penalties.keys():
            character.att[attribute] = character.att[attribute] - self.penalties[attribute]

    def __init__(self):
        self.body = BodyBase()