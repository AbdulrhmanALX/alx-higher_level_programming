#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Retrieves an element

    Args:
        my_list: a list
        idx: the index of item to retrieve

    """

    if idx < 0 or idx > len(my_list) - 1:
        return None
    my_list[idx] = element
    return my_list
