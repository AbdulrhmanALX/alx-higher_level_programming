#!/usr/bin/python3

def multiple_returns(sentence):
    """Retrieves an element

    Args:
        my_list: a list
        idx: the index of item to retrieve

    """

    first = sentence[:1]
    if len(sentence) == 0:
        first = None
    return len(sentence), first
