"""
Base class for items
"""

class Item:
    type_of = "ITEM"
    name = str()
    desc = str()
    consumable = bool()
    effect = dict()
    weight = float()
    
    def consume(self, hero):
        """Destroy current item from player inventory"""

        pass

    def apply_effect(self, hero):
        """Applies the effect of the item on use"""

        pass

