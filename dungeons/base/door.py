from abc import ABC, abstractmethod, ABCMeta
from dungeons.interfaces.create_room import NavigateToRandomRoom
from enum import Enum
import weakref

class Cardinal(Enum):
    """ENUM containing Cardinals"""
    
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

class Door(NavigateToRandomRoom):
    """Abstract base class for doors"""
    public = False
    name = str()
    desc = str()
    direction = None
    locked = bool()
    resistance = float()
    goes_to = None

    def __init__(self, parent_room):
        self.parent_room = weakref.ref(parent_room)

    def get_opposite_cardinal(self):
        if self.direction == Cardinal.NORTH:
            return Cardinal.SOUTH
        elif self.direction == Cardinal.SOUTH:
            return Cardinal.NORTH
        elif self.direction == Cardinal.EAST:
            return Cardinal.WEST
        elif self.direction == Cardinal.WEST:
            return Cardinal.EAST
        else:
            raise ValueError(f"Door {str(self)} has invalid value for direction: {str(self.direction)}")