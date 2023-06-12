#!/usr/bin/python3
"""define Square class"""


class Square:
    """Square"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if 0 > size:
            raise ValueError("size must be >= 0")
        self.__size = size
