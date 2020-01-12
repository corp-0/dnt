"""
Body classes. 
Different bodies will be avaible for different races in the future
"""

class BodyBase():
    """Main body class"""
    
    wearing = None
    
    def __init__(self):
        self.head = Head()
        self.chest = Chest()
        self.r_hand = R_hand()
        self.l_hand = L_hand()
        self.r_leg = R_Leg()
        self.l_leg = L_Leg()

class Head():
    helmet = None
    desc = "Head"

    def __init__(self):
        self.r_eye = R_Eye()
        self.l_eye = L_Eye()

class Eyes():
    desc = "Base Eyes"
    night_vision = False

class R_Eye(Eyes):
    desc = "Right eye"

class L_Eye(Eyes):
    desc = "Left eye"

class Chest():
    armor = None
    desc = "Chest"

class Hand():
    holding = None
    desc = "Base Hand"
    used = False

    def unarmed_damage(self, hero):
        strong_hand = self.is_strong_hand(hero)
        
        return hero.STR_mod + 1 + (strong_hand)

    def is_strong_hand(self, hero):
        if hero.strong_hand == self:
            return 0
        if not hero.strong_hand == self:
            return -1

class R_hand(Hand):
    holding = None
    desc = "Right hand"

class L_hand(Hand):
    holding = None
    desc = "Left hand"

class Legs():
    desc = "Base legs"

class R_Leg(Legs):
    desc = "Right leg"

class L_Leg(Legs):
    desc = "Left leg" 