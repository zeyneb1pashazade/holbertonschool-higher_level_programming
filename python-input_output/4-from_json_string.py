#!/usr/bin/python3
"""
4-from_json_string.py

A function that returns an object (Python data structure) represented 
by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Returns the Python data structure represented by a JSON string.

    Args:
        my_str (str): The JSON formatted string to deserialize.

    Returns:
        object: The Python data structure (e.g., list, dict) represented 
                by the string.
    """
    # Use the json.loads() function to deserialize the JSON string
    # back into a native Python object.
    return json.loads(my_str)
