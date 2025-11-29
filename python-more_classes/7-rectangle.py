#!/usr/bin/python3
"""
7-rectangle.py: Defines Rectangle class, tracks instance count, and
uses a customizable print_symbol for string representation.
"""


class Rectangle:
    """Represents a rectangle."""

    # Tracks the number of active Rectangle instances
    number_of_instances = 0

    # Symbol used for string representation (can be any type)
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle and increments instance count."""
        self.width = width
        self.height = height

        # Increment instance counter
        Rectangle.number_of_instances += 1

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
        """Returns the printable string representation using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""

        # Use the class or instance attribute print_symbol
        # The str() cast is important if print_symbol is not a string
        symbol = str(self.print_symbol)

        row = symbol * self.__width
        return "\n".join([row for _ in range(self.__height)])

    def __repr__(self):
        """Returns the string representation for recreation (eval())."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message and decrements the instance counter on deletion.
        """
        print("Bye rectangle...")

        # Decrement the counter
        Rectangle.number_of_instances -= 1
