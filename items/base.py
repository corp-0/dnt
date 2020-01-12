"""
Base class for items
"""

class ItemBase:
    type_of = "ITEM"
    name = str()
    desc = str()
    consumable = bool()
    effect = dict()
    weight = float()
    condition = None
    condition_desc = "This item has no condition"

    def consume(self, hero):
        """Destroy current item from player inventory"""

        pass

    def apply_effect(self, hero):
        """Applies the effect of the item on use"""

        pass

    def check_condition(self, hero):
        """Check if given hero mets the item condition to use"""

        result = eval(self.condition)

        return result
