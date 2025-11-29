#!/usr/bin/python3
"""
5-rectangle.py: Defines a Rectangle class with properties, area/perimeter,
__str__, __repr__, and a deletion message using __del__.
"""


class Rectangle:
    """Represents a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns the printable string representation ('#')."""
        if self.__width == 0 or self.__height == 0:
            return ""

        row = "#" * self.__width
        return "\n".join([row for _ in range(self.__height)])

    def __repr__(self):
        """Returns the string representation for recreation (eval())."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when an instance is deleted or garbage-collected.
        """
        print("Bye rectangle...")
