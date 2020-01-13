"""
Tries to unlock a door using brute force
"""

from skills.base import SkillBase
from dungeons.base import DoorBase

class BashDoor(SkillBase):
    name = "Bash door"
    desc = "Tries to open a door using brute force"
    command = "BASH"
    public = True

    conditions = {
        "target_class": DoorBase,
        "hero_attribute_min": ["STR", 10]
    }

    def check_conditions(self, target, hero):
        return self.valid_target_class(target) and \
                self.compare_chara_attribute(
                    self.conditions["hero_attribute_min"],hero)