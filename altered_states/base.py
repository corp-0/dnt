"""
Base class for the altered states
"""

class StateBase():
    name = str()
    desc = str()

    effects = dict()

    def apply_effect(self,hero):
        for effect in self.effects.keys():
            exec(self.effects[effect])