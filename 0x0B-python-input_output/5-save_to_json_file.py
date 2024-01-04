#!/usr/bin/python3
"""_summary_
"""
import json
def save_to_json_file(my_obj, filename):
    """_summary_

    Args:
        my_obj (_type_): _description_
        filename (_type_): _description_
    """
    with open(filename, 'w') as f:
        txt = json.dumps(my_obj)
        return f.write(txt)