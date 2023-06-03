#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    higher_number = my_list[0]
    for i in my_list:
        if higher_number < i:
            higher_number = i

    return higher_number
