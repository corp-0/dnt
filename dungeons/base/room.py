from abc import ABC
from dungeons.interfaces.create_door import CreateRandomDoors
import weakref

class Room(ABC, CreateRandomDoors):
    public = False
    name = str()
    desc = str()
    first_room = bool()
    visited = bool()
    
    
    doors_classes = list()
    doors = list()

    content = dict()

    def __init__(self, first_room, parent_dungeon, door=None):
        self.first_room = first_room
        self.parent_dungeon = weakref.ref(parent_dungeon)
        if not self.first_room:
            self.create_doors(door=door)
        self.create_doors()
        self.first_room = False

