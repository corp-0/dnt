"""
Base class for dungeons
"""

class DoorBase():
    desc = str()
    direction = str()
    locked = bool()
    goes_to = None

    NORTH = "NORTH"
    SOUTH = "SOUTH"
    EAST = "EAST"
    WEST = "WEST"

    def opposite_door(self, direction):
        if direction == self.NORTH:
            return self.SOUTH
        elif direction == self.SOUTH:
            return self.NORTH
        elif direction == self.EAST:
            return self.WEST
        elif direction == self.WEST:
            return self.EAST

    def unlock(self, hero):
        pass


class RoomBase():
    desc = str()
    prev_room = None
    doors = list()

class DungeonBase():
    name = str()
    desc = str()

    temperature = float()

    floor_desc = str()
    walls_desc = str()

    max_rooms = int()
    rooms = list()

    enemy_pool = list()
