"""
Base class for dungeons
"""

import random
from enum import Enum
import weakref

class Cardinal(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4

class DoorBase():
    public = False
    desc = str()
    direction = None
    locked = bool()
    resistance = float()
    goes_to = None

    def __init__(self, parent):
        self.room = weakref.ref(parent)

    def create_new_room(self):
        new_room = self.room.__class__(self)

        return new_room
        
    def get_opposite_door(self):
        if self.direction == Cardinal.NORTH:
            return Cardinal.SOUTH
        elif self.direction == Cardinal.SOUTH:
            return Cardinal.NORTH
        elif self.direction == Cardinal.EAST:
            return Cardinal.WEST
        elif self.direction == Cardinal.WEST:
            return Cardinal.EAST

class RoomBase():
    public = False
    desc = str()
    first_room = bool()

    doors_classes = [DoorBase]
    doors = list()

    content = list()
    enemies = list()

    def __init__(self, from_where):
        self.check_if_first_room(from_where)
        self.create_doors()
        self.assign_opposite_door(from_where)
        self.assign_doors_to_cardinals()

        self.first_room = False

    def check_if_first_room(self, from_where):
        if not issubclass(from_where.__class__, DoorBase):
            self.first_room = True
        else:
            self.first_room = False

        return self.first_room    

    def create_doors(self):
        random_door_type = random.choice(self.doors_classes)
        door_amount = random.randint(1,4)

        for i in range(1, door_amount+1):
            new_door = random_door_type(self)
            self.doors.append(new_door)

    def assign_opposite_door(self, from_where):
        if not issubclass(from_where.__class__, DoorBase):
            return False
        else:
            self.doors[0].direction = from_where.get_opposite_door()
            self.doors[0].goes_to = from_where.room

    def assign_doors_to_cardinals(self):
        for door in self.doors:
            if door.direction != None:
                current_door = door.direction.value

        if self.first_room:
            current_door = 0
        for door in self.doors:
            if door.direction == None:
                current_door += 1
                if current_door == 5:
                    current_door = 1
                door.direction = Cardinal(current_door)
    
class DungeonBase():
    public = False
    name = str()
    desc = str()

    temperature = float()

    floor_desc = str()
    walls_desc = str()

    max_rooms = int()
    rooms = list()
    current_room = None

    enemy_pool = list()

    room_classes = [RoomBase]
    
    def __init__(self):
        random_room_type = random.choice(self.room_classes)
        self.current_room = random_room_type(self)
        self.rooms.append(self.current_room)

    def move_to(self, door):
        if door.goes_to == None:
            room = random.choice(self.room_classes)
            room = room(door)
        else:
            room = door.goes_to()

        self.current_room = room
        if not self.current_room in self.rooms:
            self.rooms.append(self.current_room)

