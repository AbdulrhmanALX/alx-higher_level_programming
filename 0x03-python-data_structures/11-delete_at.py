#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Retrieves an element

    Args:
        my_list: a list
        idx: the index of item to retrieve

    """

    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    my_list.remove(idx)
    return my_list
