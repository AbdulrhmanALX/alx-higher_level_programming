#!/usr/bin/python3
"""_summary_
"""
def read_file(filename=""):
    """_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
    """
    with open(filename) as f:
        txt = f.read()
        print(txt, end='')