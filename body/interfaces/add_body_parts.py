import abc

class IAddBodyParts():
    """Interface to add body parts
    to a body"""

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def add_body_parts(self):
        """Add body parts to a body"""
        pass



