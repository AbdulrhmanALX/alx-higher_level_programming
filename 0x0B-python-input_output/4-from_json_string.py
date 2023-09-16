#!/usr/bin/python3
"""Module 1-write_file.
Writes in a text file.
"""
import json

def from_json_string(my_str):
    """Writes text in filename.
    Args:
        - filename: name of the file
        - text: string to write in the file
    Returns: number of characters written
    """
    
    return json.loads(my_str)
