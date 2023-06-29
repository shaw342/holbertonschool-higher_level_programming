#!/usr/bin/python3
"""define Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """classe square"""
    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str"""
        a = (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")
        return a

    @property
    def size(self):
        """size"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update """
        for key, value in kwargs.items():
            setattr(self, key, value)

        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]

    def to_dictionary(self):
        """doc"""
        return {"id" : self.id, "width": self.size, "height": size.size, "x": self.x, "y": self.y }
