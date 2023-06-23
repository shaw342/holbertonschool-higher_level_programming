#!/usr/bin/python3
"""Write a class Student that defines a student"""


class Student:
    """Represent a Student"""

    def __init__(self, first_name, last_name, age):
        """Init a Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dict repres of a Student"""
        return self.__dict__
