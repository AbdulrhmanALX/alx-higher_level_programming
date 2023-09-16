#!/usr/bin/python3
"""Module 1-write_file.
Writes in a text file.
"""
import json

def save_to_json_file(my_obj, filename):
    """Writes text in filename.
    Args:
        - filename: name of the file
        - text: string to write in the file
    Returns: number of characters written
    """
    with open(filename,'w') as f:
        rd = json.dumps(my_obj)
        return f.write(rd)
