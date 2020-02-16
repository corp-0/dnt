from dungeons.base.door import Door

class DefaultDoor(Door):
    """The most basic usable door"""

    public = True
    name = "Boring looking door"
    desc = "This door looks like its made of wood... That's it."
    resistance = 5 #need roll 1d20+str_mod to be higher than this to break the door