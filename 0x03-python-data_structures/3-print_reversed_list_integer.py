#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Retrieves an element

    Args:
        my_list: a list
        idx: the index of item to retrieve

    """

    if my_list:
        my_list.reverse()
        for _ in my_list:
            print("{:d}".format(_))
    