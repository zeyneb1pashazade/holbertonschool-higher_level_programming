#!/usr/bin/python3
"""
3-is_kind_of_class.py: Checks if an object is an instance of a class
or a class inherited from it.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or a class inherited from it,
    False otherwise.
    """
    return isinstance(obj, a_class)
