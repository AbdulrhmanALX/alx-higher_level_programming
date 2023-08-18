#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrieves an element

    Args:
        my_list: a list
        idx: the index of item to retrieve

    """

    # Check for negative and out of range index
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None
    return my_list[idx]
