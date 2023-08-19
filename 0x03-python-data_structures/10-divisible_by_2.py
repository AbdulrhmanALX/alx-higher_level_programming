#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Retrieves an element

    Args:
        my_list: a list
        idx: the index of item to retrieve

    """

    tf = []
    for _ in my_list:
        if _ % 2 == 0:
            tf.append(True)
        else:
            tf.append(False)
    return tf
