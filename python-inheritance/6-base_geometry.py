#!/usr/bin/python3
"""
6-base_geometry.py: Defines BaseGeometry class with an area method
that raises an Exception.
"""


class BaseGeometry:
    """
    A base class for geometric objects.
    """
    def area(self):
        """
        Calculates the area (currently not implemented).

        Raises:
            Exception: Always raises an Exception with the message:
                       "area() is not implemented".
        """
        raise Exception("area() is not implemented")
