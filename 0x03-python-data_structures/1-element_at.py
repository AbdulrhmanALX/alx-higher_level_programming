#!/usr/bin/python3

def element_at(my_list, idx):
    """Retrieves an element

    Args:
        my_list: a list
        idx: the index of item to retrieve

    """

    # Check for negative and out of range index
    if idx < 0 or idx > len(my_list) - 1:
        return None
    else:
    return my_list[idx]
