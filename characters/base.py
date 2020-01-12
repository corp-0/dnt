"""
Base class for characters
"""
import random
import pickle
from appdirs import AppDirs

class Body():
    wearing = None
    
    def __init__(self):
        self.head = Head()
        self.chest = Chest()
        self.r_hand = R_hand()
        self.l_hand = L_hand()

class Head():
    helmet = None
    desc = "Head"

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


class Base():
    name = str()
    alive = True
    race = None
    body = Body()

    head = Head()
    chest = Chest()
    l_hand = L_hand()
    r_hand = R_hand()

    hands = [l_hand, r_hand]

    strong_hand = None

    att = {
        "STR": int(),
        "DEX": int(),
        "CON": int(),
        "INT": int(),
        "WIS": int(),
        "CHAR": int()
    }

    STR_mod = int()
    DEX_mod = int()
    CON_mod = int()
    INT_mod = int()
    WIS_mod = int()
    CHAR_mod = int()

    MAX_HP = int()
    MAX_MP = int()
    HP = int()
    MP = int()

    AC = int()
    INITIATIVE = int()

    fame = 0
    armor = 0
    shield = 0

    inventory = list()
    carry_capacity = float()
    current_carry = float()

    spells = list()

    side = None


    def calculate_att_modifier(self):
        self.STR_mod = int((self.att["STR"] - 10) / 2)
        self.DEX_mod = int((self.att["DEX"] - 10) / 2)
        self.CON_mod = int((self.att["CON"] - 10) / 2)
        self.INT_mod = int((self.att["INT"] - 10) / 2)
        self.WIS_mod = int((self.att["WIS"] - 10) / 2)
        self.CHAR_mod = int((self.att["CHAR"] - 10) /2)
    
    def calculate_max_hp(self):
        dice = random.randint(1,self.race.dice)
        max_hp = dice + self.CON_mod

        return max_hp

    def calculate_max_mana(self):
        dice = random.randint(1,self.race.dice)
        max_mana = dice + self.INT_mod

        return max_mana

    def calculate_AC(self, bonus=0):
        self.AC = self.DEX_mod + self.armor + self.shield

    def calculate_initiative(self):
        dice = random.randint(1,20)
        initiative = dice + self.DEX_mod

        return initiative

    def calculate_carry_capacity(self):
        self.carry_capacity = self.att["STR"] * 15
        
    def calculate_current_carry(self):
        current_carry = 0
        for item in self.inventory:
            current_carry = current_carry + item.weight

        self.current_carry = current_carry

    def add_item_to_inventory(self, item):
        if self.calculate_current_carry() + item.weight > self.calculate_carry_capacity():
            print("You're over encumbered and can't take that item!")
            
            return False
        
        if item.condition != None:
            if item.condition():
                print(f"You take {item.name} and add it to your inventory.\n{item.desc}")
                self.inventory.append(item)
                
                return True
            else:
                print(f"You can not take {item.name}. {item.condition_desc}")
                
                return False
        
        print(f"You take {item.name} and add it to your inventory.\n{item.desc}")
        self.inventory.append(item)
        
        return True

    def equip_item_to_hand(self, item, hand):
        if hand.holding != None:
            print("{hand.desc} is already busy with {hand.holding.name}")
        else:
            hand.holding = item

    def attack(self, target, hand):
        hand.used = True
        if hand.holding == None:
            weapon = "bare hand"
        else:
            weapon = hand.holding.name
        dmg = self.calculate_attack_damage(hand)

        print(f"{self.name} uses his {weapon} to attack {target.name}!")
        print(f"{self.name}'s attack deals {dmg} points of damage on {target.name}'")

        target.receive_damage(dmg, self)
    
    def calculate_attack_damage(self, hand):
        if hand.holding == None:
            return hand.unarmed_damage(self)
        else:
            return hand.holding.damage + self.STR_mod + (hand.is_strong_hand(self))

    def receive_damage(self, damage, attacker):
        if damage > self.HP:
            self.alive = False
            print(f"{self.name} has died!")
            attacker.fame = attacker.fame + self.fame
            print(f"{attacker.name} is granted {self.fame} points of fame!")
            del self
        elif damage < self.AC:
            print(f"{attacker.name}'s attack makes no effect on {self.name}!'")
        else:
            damage = damage - self.AC
            self.HP = self.HP - damage
            print(f"{attacker.name} deals {damage} points of damage on {self.name}")
       
    def serialize_character(self):
        serialized_chara = pickle.dumps(self)

        return serialized_chara
    
    def deserialize_character(self, string):
        deserialized_chara = pickle.loads(string)

        return deserialized_chara

    def __init__(self, name:str, race:object, 
                            STR:int, DEX:int, CON:int, INT:int, WIS:int,CHAR:int, 
                            side=None, strong_hand=None):
        
        self.name = name
        self.race = race
        self.att["STR"] = STR
        self.att["DEX"] = DEX
        self.att["CON"] = CON
        self.att["INT"] = INT
        self.att["WIS"] = WIS
        self.att["CHAR"] = CHAR

        self.body = Body()
        self.head = self.body.head
        self.chest = self.body.chest
        self.l_hand = self.body.l_hand
        self.r_hand = self.body.r_hand
        self.hands = [self.l_hand, self.r_hand]

        self.calculate_att_modifier()
        self.MAX_HP = self.calculate_max_hp()
        self.MAX_MP = self.calculate_max_mana()

        self.HP = self.MAX_HP
        self.MP = self.MAX_MP

        self.race.add_bonuses(self)
        self.race.add_penalties(self)
        
        if strong_hand is None:
            self.strong_hand = random.choice(self.hands)
        else:
            self.strong_hand = strong_hand

        if self.side is None:
            self.side = "HERO"
        else:
            self.side = side
