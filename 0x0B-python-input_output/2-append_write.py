#!/usr/bin/python3
"""Module 1-write_file.
Writes in a text file.
"""


def append_write(filename="", text=""):
    """Writes text in filename.
    Args:
        - filename: name of the file
        - text: string to write in the file
    Returns: number of characters written
    """

    with open(filename, 'a') as f:
        return f.write(text)
