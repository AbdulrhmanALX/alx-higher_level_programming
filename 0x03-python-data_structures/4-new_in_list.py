#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Retrieves an element

    Args:
        my_list: a list
        idx: the index of item to retrieve

    """

    if idx < 0:
        return my_list.copy()
    elif idx > len(my_list) - 1:
        return my_list.copy()
    new = my_list.copy()
    new[idx] = element
    return new
