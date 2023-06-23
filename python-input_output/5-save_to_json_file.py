#!/usr/bin/python3
import json
"""define function"""


def save_to_json_file(my_obj, filename):
    """function"""
    with open(filename, "w", encoding="utf-8") as f:
        new_obj = json.dump(my_obj, f)
        return new_obj
