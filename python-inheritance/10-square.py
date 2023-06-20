#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""define class"""


class Square(Rectangle):
    """ Base Geometry """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """define area function"""
        return self.__size ** 2
