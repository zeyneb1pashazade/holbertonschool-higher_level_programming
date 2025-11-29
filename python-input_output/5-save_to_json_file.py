#!/usr/bin/python3
"""
6-load_from_json_file.py

A function that creates an Object from a "JSON file".
"""
import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON formatted file.

    It reads the JSON string from the file and deserializes it into
    the corresponding Python data structure (e.g., list, dict).

    Args:
        filename (str): The name of the JSON file to read.

    Returns:
        object: The Python data structure represented by the file's content.
    """
    # Use the 'with' statement to open the file in 'r' (read) mode.
    with open(filename, mode='r', encoding='utf-8') as f:
        # Read the content (JSON string) and deserialize it using json.load().
        return json.load(f)
