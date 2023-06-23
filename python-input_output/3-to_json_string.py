import json
"""define function return new_obj"""


def to_json_string(my_obj):
    """function"""
    new_obj = json.dumps(my_obj)
    return new_obj
