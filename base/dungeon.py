from abc import ABC
from .interface.create_room import Choose_from_pool
import random


class Dungeon(ABC, Choose_from_pool):
    """Abstract base class for dungeons"""

    public = False
    name = str()
    desc = str()
    temp = int()#ºC

    floor_desc = list()
    wall_desc = list()

    current_room = None
    max_rooms = int()
    rooms = list()
    room_classes = list()

    enemy_pool = list()
    loot_pool = list()

    def __init__(self):
        self.current_room = self.create_room()

    def move_to(self, door):
        self.current_room = door.create_room()
