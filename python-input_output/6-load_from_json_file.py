#!/usr/bin/python3
import json
def load_from_json_file(filename):
    with open(filename,'r') as f:
        new_obj = json.load(f)
        return new_obj
