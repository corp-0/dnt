from base.dungeon import Dungeon
from dungeons.default_room import DefaultRoom

class DefaultDungeon(Dungeon):
    """Most basic usable dungeon"""

    public = True
    name = "Forgeteable Dungeon"
    desc = "A very regular looking dungeon"
    temp = 20 #ºC

    floor_desc = ["This floor is so lame!"]
    wall_desc = ["Walls look like any dungeon wall"]

    room_classes = [DefaultRoom]
