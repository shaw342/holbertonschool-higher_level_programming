#!/usr/bin/python3
""" define class Base"""
import json


class Base:
    """class base count the number of object and fix the id """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ json to string """
        if list_dictionaries is None:
            return "[]"

        return json.dumps(list_dictionaries)
