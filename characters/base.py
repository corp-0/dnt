"""
Base class for characters
"""
import random
import pickle
from races.base import RaceBase
from inspect import getmembers, isclass
import skills

#magic numbers
CARRY_CAPACITY_MULTIPLICATOR = 11


class CharacterBase():
    name = str()
    alive = True
    race = RaceBase()

    strong_hand = None

    att = {
        "STR": int(),
        "DEX": int(),
        "CON": int(),
        "INT": int(),
        "LCK": int(),
        "CHAR": int()
    }

    STR_mod = int()
    DEX_mod = int()
    CON_mod = int()
    INT_mod = int()
    LCK_mod = int()
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
    skills = list()
    party = list()

    def calculate_att_modifier(self):
        self.STR_mod = int((self.att["STR"] - 10) / 2)
        self.DEX_mod = int((self.att["DEX"] - 10) / 2)
        self.CON_mod = int((self.att["CON"] - 10) / 2)
        self.INT_mod = int((self.att["INT"] - 10) / 2)
        self.LCK_mod = int((self.att["LCK"] - 10) / 2)
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
        self.carry_capacity = self.att["STR"] * CARRY_CAPACITY_MULTIPLICATOR

        return self.carry_capacity
        
    def calculate_current_carry(self):
        current_carry = 0
        for item in self.inventory:
            current_carry = current_carry + item.weight

        self.current_carry = current_carry

        return self.current_carry

    def add_item_to_inventory(self, item):
        if self.calculate_current_carry() + item.weight > self.carry_capacity:
            print(f"Maybe {item.name} is way too heavy to carry on your inventory now!")
            
            return False
                
        self.inventory.append(item)
        self.current_carry = self.current_carry + item.weight
        print(f"You take {item.name} and add it to your inventory.\n{item.desc}")
        
        return True

    def use_item(self, item):
        if not item.condition is None:
            if not item.check_condition:
                print(f"You can't use this item. {item.condition_desc}")

                return False
            else:
                item.apply_effect(self)
                print(f"You use your {item.name}")
        else:
            item.apply_effect(self)
            print(f"You use your {item.name}")

    def equip_item_to_hand(self, item, hand):
        if item.two_hands:
            count_free_hands = 0
            free_hands = []
            for h in self.hands:
                if h.holding == None:
                    free_hands.append(hand)
                    count_free_hands +=1

            if count_free_hands > 1:
                for h in free_hands:
                    h.holding = item

            else:
                print(f"{item.name} need two hands to be held!")

                return False

                            
            if item in self.inventory:
                self.inventory.pop(item)

            item.apply_effect(self)

            print(f"You're now holding your {item.name}")

            return True

        if hand.holding != None:
            print(f"{hand.desc} is already busy with {hand.holding.name}")

            return False
        else:
            hand.holding = item
            if item in self.inventory:
                    self.inventory.pop(item)
            
            item.apply_effect(self)

            print(f"You take your {item.name} in your {hand.desc}!")

            return True

    def holster_weapon(self, item):
        if item.two_hands:
            for hand in self.hands:
                hand.holding = None
        else:
            for hand in self.hands:
                if item in hand.holding:
                    hand.holding = None

        self.inventory.append(item)
        item.remove_effects(self)
        print(f"You put your {item.name} in your holster")
        

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
    
    def load_character(self, string):
        deserialized_chara = pickle.loads(string)

        return deserialized_chara

    def __init__(self):   
        self.body = self.race.body()
        self.head = self.body.head
        self.r_hand = self.body.r_hand
        self.l_hand = self.body.l_hand
        self.r_leg = self.body.r_leg
        self.l_leg = self.body.l_leg
        self.head.r_eye.night_vision = self.race.night_vision
        self.head.l_eye.night_vision = self.race.night_vision

        self.hands = self.body.hands
        self.legs = self.body.legs
        self.eyes = self.body.eyes

        if self.name == "":
            self.name = random.choice(self.race.names)

        self.calculate_att_modifier()
        self.MAX_HP = self.calculate_max_hp()
        self.MAX_MP = self.calculate_max_mana()

        self.HP = self.MAX_HP
        self.MP = self.MAX_MP

        self.calculate_AC()
        self.calculate_current_carry()
        self.calculate_carry_capacity()
        
        if self.strong_hand is None:
            handy = random.choice(self.hands)
            handy.strong_hand = True

        self.strong_hand = list()
        self.weak_hand = list()
        for h in self.hands:
            if h.strong_hand:
                self.strong_hand.append(h)
            else:
                self.weak_hand.append(h)

        self.race.add_bonuses(self)
        self.race.add_penalties(self)

        for name, obj in getmembers(skills):
            if isclass(obj) and hasattr(obj, "public"):
                if obj.public:
                    self.skills.append(obj)
