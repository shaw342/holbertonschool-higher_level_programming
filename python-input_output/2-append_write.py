#!/usr/bin/python3
"""define filename"""


def append_write(filename="", text=""):
    """function filename"""
    with open(filename, "a", encoding='utf-8') as f:
        append_write = f.write(text)
        return append_write
