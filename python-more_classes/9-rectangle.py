#!/usr/bin/python3
"""
9-rectangle.py: Defines Rectangle class, tracks count, custom print symbol,
static/class methods.
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area.
        Returns rect_1 if both have the same area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a new Rectangle instance with width == height == size.
        """
        return cls(size, size)

    def __str__(self):
        """Returns the printable string representation using print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""

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
