#!/usr/bin/python3
"""define function open and write"""


def write_file(filename="", text=""):
    """function open and write and return write_file"""
    with open(filename, "w", encoding='utf-8') as f:
        write_file = f.write(text)
        return write_file
