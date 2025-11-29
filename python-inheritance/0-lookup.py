#!/usr/bin/python3
"""
0-lookup.py: Contains a function to return the list of available attributes
and methods of an object.
"""


def lookup(obj):
    """Returns a list of an object's available attributes and methods."""
    return dir(obj)
