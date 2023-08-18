#!/usr/bin/python3

def no_c(my_string):
    """Retrieves an element

    Args:
        my_list: a li 
        idx: the index of item to retrieve

    """

    st = ""
    for i in my_string:
        if i in "Cc":
            continue
        st += i
    return st
