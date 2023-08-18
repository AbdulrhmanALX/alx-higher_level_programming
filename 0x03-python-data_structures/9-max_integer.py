#!/usr/bin/python3

def max_integer(my_list=[]):
    """Retrieves an element

    Args:
        my_list: a list
        idx: the index of item to retrieve

    """

    if len(my_list) == 0:
        return None
    max = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > max:
            max = my_list[i]
        else:
            continue
    return max