from abc import ABC
from body.base.body import Body, Head, Hand, Leg, Torso, Eye
from body.interfaces.add_body_parts import IAddBodyParts


class HumanoidEye(Eye):
    """Human like eye"""

    desc = "Human like eye"
    night_vision = False


class HumanoidHead(Head):
    """Human like head"""

    desc = "Human like head"
    helmet = None

    def add_eyes(self):
        self.r_eye = HumanoidEye()
        self.l_eye = HumanoidEye()


class HumanoidTorso(Torso):
    """Human like torso"""

    desc = "Human like torso"
    armor = None

class HumanoidHand(Hand):
    """Human like hand"""

    desc = "Human like hand"
    can_hold = True
    holding = None
    strong_hand = False

    def unarmed_damage(self, hero):
        if self.strong_hand:
            weak_hand_penalty = 0
        else:
            weak_hand_penalty = -1
        
        return hero.STR_mod + 1 + (weak_hand_penalty)

class HumanoidLeg(Leg):
    """Human like leg"""

    desc = "Human Like leg"


class HumanoidParts(IAddBodyParts):
    """Add human like body parts"""

    def add_body_parts(self):
        self.head = HumanoidHead() 
        self.torso = HumanoidTorso()
        self.r_hand = HumanoidHand()
        self.l_hand = HumanoidHand()
        self.r_leg = HumanoidLeg()
        self.l_leg = HumanoidLeg()


class HumanoidBody(Body, HumanoidParts):
    """1 head, 2 hands and 2 legs"""

    pass
