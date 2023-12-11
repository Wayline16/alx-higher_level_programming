#!/usr/bin/python3

"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Class Square"""
    
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string info about this square. Format: [Square] (<id>) <x>/<y> - <size>"""
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)
            
    @property
    def size(self):
        """Size of this square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value