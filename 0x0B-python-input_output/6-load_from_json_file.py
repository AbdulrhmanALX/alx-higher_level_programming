#!/usr/bin/python3
"""Module 1-write_file.
Writes in a text file.
"""
import json

def load_from_json_file(filename):
    """Writes text in filename.
    Args:
        - filename: name of the file
        - text: string to write in the file
    Returns: number of characters written
    """
    with open(filename) as f:
        return json.load(f)
