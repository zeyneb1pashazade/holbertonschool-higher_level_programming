#!/usr/bin/python3
"""
3-to_json_string.py

A function that returns the JSON representation of an object (string).
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON string representation of a Python object.

    Args:
        my_obj: The object to serialize (e.g., list, dict, string, int).

    Returns:
        str: The JSON string representation of the object.
    """
    # Use the json.dumps() function to serialize the Python object
    # into a JSON formatted string.
    return json.dumps(my_obj)
