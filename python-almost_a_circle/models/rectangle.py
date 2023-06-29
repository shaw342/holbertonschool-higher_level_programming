#!/usr/bin/python3
""" define class Rectangle """
from models.base import Base


class Rectangle(Base):
    """rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width check  value """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ x """
        return self.__x

    @x.setter
    def x(self, value):
        """x and value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y """
        return self.__y

    @y.setter
    def y(self, value):
        """y and value"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """display rectangle"""
        for i in range(self.__height):
            print("#" * self.__width)

    def display(self):
        """display rectangle"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """ update """
        for key, value in kwargs.items():
            setattr(self, key, value)

        if len(args) >= 1:
            self.id = args[0]
        if len(args) == 2:
            self.width = args[1]
        if len(args) == 3:
            self.height = args[2]
        if len(args) == 4:
            self.x = args[3]
        if len(args) == 5:
            self.y = args[4]

    def __str__(self):
        """str"""
        m = (
                f"[Rectangle] ({self.id}) "
                f"{self.x}/{self.y } - {self.width}/{self.height}").strip()
        return m
