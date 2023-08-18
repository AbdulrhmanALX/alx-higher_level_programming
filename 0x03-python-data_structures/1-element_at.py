#!/usr/bin/python3

def element_at(my_list, idx):
    """return element of a list

    Args:
        my_list (list): _description_
        idx (int): _description_
    """
    if idx < 0 or idx > len(my_list) - 1:
        return None
    else:
        return my_list[idx]