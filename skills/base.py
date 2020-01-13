"""
Base class for regular skills (all heroes can perform any of these)
"""

class SkillBase():
    name = str()
    desc = str()
    command = str()
    conditions = {
        "target_class":None,
        "target_hp_min":None,
        "target_mp_min":None,
        "target_hp_max":None,
        "target_mp_max":None,
        "target_attribute_min":[None, int()],
        "target_attribute_max":[None, int()],
        "hero_attribute_min":[None, int()],
        "hero_attribute_max":[None, int()],
    }
    public = False

    attribute = None

    other_effect = dict()

    def __init__(self, hero):
        if self.public:
            hero.skills.append(self)

    def valid_target_class(self, target):
        """Compare if target object is a subclass of the specified class"""

        valid = self.conditions["target_class"]

        return issubclass(target.__class__, valid)
        
    def compare_chara_attribute(self, cond, chara, comparation="min"):
        """Compare if given character's attribute with the specified number"""

        attribute = (self.conditions[cond])[0]
        number = (self.conditions[cond])[1]

        if comparation == "min":
            operator = ">="
        else:
            operator = "<="

        return eval(f'{chara.att[attribute]} {operator} {number}')

    def compare_chara_points(self, cond, chara, comparation="min"):
        """Compare if given character's HP/MP with the specified number"""

        if "_mp_" in cond:
            attribute = "MP"
        else:
            attribute = "HP"

        if comparation == "min":
            operator = ">="
        else:
            operator = "<="

        number = self.conditions[cond]

        return eval(f"{chara}.{attribute} {operator} {number}")

        
    def check_conditions(self):
        """overwrite this method to meet your conditions!"""
        return bool()
