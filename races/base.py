"""
Base class for races
"""
class BodyBase():
    """Main body class for human like creatures.
    1 head, 1 torso, 2 hands, 2 legs"""
    
    wearing = None
    desc = "1 head, 2 eyes, 1 torso, 2 hands, 2 legs."
    
    def __init__(self):
        self.head = HeadBase()
        self.chest = ChestBase()
        self.r_hand = R_hand()
        self.l_hand = L_hand()
        self.r_leg = R_Leg()
        self.l_leg = L_Leg()

        self.hands = [self.r_hand, self.l_hand]
        self.legs = [self.r_leg, self.l_leg]
        self.eyes = [self.head.r_eye, self.head.l_eye]

class HeadBase():
    helmet = None
    desc = "Head"

    def __init__(self):
        self.r_eye = R_EyeBase()
        self.l_eye = L_EyeBase()

class EyeBase():
    desc = "Base Eyes"
    night_vision = False

class R_EyeBase(EyeBase):
    desc = "Right eye"

class L_EyeBase(EyeBase):
    desc = "Left eye"

class ChestBase():
    armor = None
    desc = "Chest"

class HandBase():
    holding = None
    desc = "Base Hand"
    used = False
    strong_hand = False

    def unarmed_damage(self, hero):
        if self.strong_hand:
            weak_hand_penalty = 0
        else:
            weak_hand_penalty = -1
        
        return hero.STR_mod + 1 + (weak_hand_penalty)


class R_hand(HandBase):
    holding = None
    desc = "Right hand"

class L_hand(HandBase):
    holding = None
    desc = "Left hand"

class LegBase():
    desc = "Base legs"

class R_Leg(LegBase):
    desc = "Right leg"

class L_Leg(LegBase):
    desc = "Left leg" 


class RaceBase():
    name = str()
    desc = str()
    body = BodyBase

    dice = 1

    night_vision = bool()
    cold_resistance = int()
    heat_resistance = int()

    bonuses = dict()
    penalties = dict()

    names = ["Bob"]

    def add_bonuses(self, hero):
        for key in self.bonuses:
            exec(self.bonuses[key])

    def add_penalties(self, hero):
        for key in self.penalties:
            exec(self.penalties[key])