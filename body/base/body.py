"""Base classes for bodies"""

from abc import ABC, abstractmethod, ABCMeta, abstractproperty
from body.interfaces.add_body_parts import IAddBodyParts

class Body(ABC, IAddBodyParts):
    """Base for all body types"""

    __metaclass__  = ABCMeta

    @abstractproperty
    def desc(self):
        return str()

    @abstractproperty
    def wearing(self):
        pass

    def __init__(self):
        self.add_body_parts()

class Head(ABC):
    """Base for all heads types"""

    __metaclass__ = ABCMeta

    @abstractproperty
    def desc(self):
        return str()

    @abstractproperty
    def helmet(self):
        pass

    @abstractmethod
    def add_eyes(self):
        pass

class Eye(ABC):
    """Base for all eyes types"""

    __metaclass__ = ABCMeta

    @abstractproperty
    def desc(self):
        return str()

    @abstractproperty
    def night_vision(self):
        pass

class Torso(ABC):
    """Base for all torsos"""

    __metaclass__ = ABCMeta

    @abstractproperty
    def desc(self):
        return str()

    @abstractproperty
    def armor(self):
        pass


class Hand(ABC):
    """Base for all hands"""

    __metaclass__ = ABCMeta

    @abstractproperty
    def desc(self):
        return str()

    @abstractproperty
    def can_hold(self):
        pass
    
    @abstractproperty
    def holding(self):
        pass

    @abstractproperty
    def strong_hand(self):
        pass

    @abstractmethod
    def unarmed_damage(self, hero):
        pass

class Leg(ABC):
    """Base for all legs types"""

    __metaclass__ = ABCMeta

    @abstractproperty
    def desc(self):
        return str()

