#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list_new = my_list[::-1]
    for i in range(len(my_list_new)):
        print("{:d}".format(my_list_new[i]))
