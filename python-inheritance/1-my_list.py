#!/usr/bin/python
"""define  class"""


class MyList(list):
    """MyList """

    def __init__(self):
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
