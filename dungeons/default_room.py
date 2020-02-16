from dungeons.base.room import Room
from dungeons.default_door import DefaultDoor

class DefaultRoom(Room):
    """Most basic usable Room"""

    public = True
    name = "Ordinary dungeon room"
    desc = "This room looks like any other room in any forgeteable dungeon"
    
    doors_classes = [DefaultDoor]