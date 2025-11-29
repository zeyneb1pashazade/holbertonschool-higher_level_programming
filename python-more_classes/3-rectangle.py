#!/usr/bin/python3
"""
3-rectangle.py
Defines a Rectangle class with private instance attributes (width and height),
properties with validation, methods for area and perimeter, and
custom string representation (__str__) using the '#' character.
"""


class Rectangle:
    """
    Represents a rectangle with specified width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        # Call the setters to ensure validation is performed upon instantiation
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the private instance attribute __width."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the private instance attribute __width, validating the value.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the private instance attribute __height."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the private instance attribute __height, validating the value.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        Area = width * height.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        Perimeter = 2 * (width + height).
        If width or height is 0, the perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using the character '#'.
        If width or height is 0, returns an empty string.
        This is used by print() and str().
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        # Create a single row of '#' characters with the correct width
        row = "#" * self.__width

        # Join multiple rows (equal to the height) with newline characters
        return "\n".join([row for _ in range(self.__height)])
# __repr__ is omitted to use Python's default object representation.
