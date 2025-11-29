#!/usr/bin/python3
"""
2-is_same_class.py: Checks if an object is exactly an instance of the class.
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
