#!/usr/bin/python3
"""
7-base_geometry.py: Defines BaseGeometry class with area and integer_validator
methods.
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

    def integer_validator(self, name, value):
        """
        Validates that 'value' is an integer greater than 0.

        Args:
            name (str): The name of the value (assumed to be a string).
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
