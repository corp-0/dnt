import abc
import random
from dungeons.base.door import Cardinal

class ICreateDoors():
    """Interface for create_doors() method"""

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def create_doors(self, *args, **kwargs):
        """Creates a new door in the room"""
        return object

class CreateRandomDoors(ICreateDoors):
    """Behavior for create_doors() method"""

    @abc.abstractproperty
    def first_room(self):
        return bool()

    @abc.abstractproperty
    def doors_classes(self):
        return list()

    @abc.abstractproperty
    def doors(self):
        return list()

    def create_doors(self, *args, door = None, **kwargs):
        door_amount = random.randint(1,4)
        prev_door = None
        for _ in range(1,door_amount+1):
            door_type = random.choice(self.doors_classes)
            new_door = door_type(self)
            self.doors.append(new_door)

            # Handling the case the player comes from another room
            if not self.first_room:
                prev_door = kwargs["door"]
                prev_room = door.parent_room()

                self.doors[0].direction = prev_door.get_opposite_cardinal(prev_door.direction)
                self.doors[0].goes_to = prev_room
            
            #Logic to assign semi-random cardinals to generated doors
            if not prev_door == None:
                current_door = prev_door.direction.value
            else:
                current_door = 0
            for door in self.doors:
                if door.direction == None:
                    current_door =+1
                    if current_door > 4:
                        current_door = 1
                    door.direction = Cardinal(current_door)
                
            return self.doors
