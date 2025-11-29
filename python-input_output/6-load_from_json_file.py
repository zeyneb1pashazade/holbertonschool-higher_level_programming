#!/usr/bin/python3
"""
5-save_to_json_file.py

A function that writes an Object to a text file, using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file using its JSON string representation.

    Args:
        my_obj: The Python object (data structure) to serialize and save.
        filename (str): The name of the file to write the JSON string to.
    """
    # First, serialize the Python object into a JSON formatted string.
    json_string = json.dumps(my_obj)

    # Use the 'with' statement to open the file in 'w' (write/overwrite) mode.
    # We don't need to specify encoding here as 'w' for text files defaults
    # to the system default, which usually handles the simple ASCII characters
    # of the JSON string correctly, but for maximum compatibility with text
    # files (as per previous exercises), let's explicitly use UTF-8.
    with open(filename, mode='w', encoding='utf-8') as f:
        # Write the JSON string to the file.
        f.write(json_string)
