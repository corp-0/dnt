import abc
import random


class ICreateRoom():
    """Interface for the create_room() method"""

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_room(self, *args, **kwargs):
        """Creates a new room to navigate to"""
        pass


class Choose_from_pool(ICreateRoom):
    """Behavior for create_room() method."""

    @abc.abstractproperty
    def room_classes(self):
        return list()

    @abc.abstractproperty
    def rooms(self):
        return list()

    def create_room(self):
        """Choose a random room class from the pool of classes"""
        room_type = random.choice(self.room_classes)
        room = room_type(first_room = True, parent_dungeon = self)
        self.rooms.append(room)

        return room


class NavigateToRandomRoom(ICreateRoom):
    """Behavior for create_room() method.
    Used by doors when the player navigates through them"""

    parent_room = None

    def create_room(self):
        """Choose a random room class from the pool of dungeon classes"""
        room_type = random.choice(self.parent_room().parent_dungeon().room_classes)
        return room_type(False, self)


class NavigateToRoom(ICreateRoom):
    """Behavior for create_room() method"""

    def create_room(self, room_class):
        """Navigates to a specific room class"""
        return room_class()
