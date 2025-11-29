#!/usr/bin/python3
"""
This module defines the MyList class which inherits from list
and adds a method to print the list sorted in ascending order.
"""

class MyList(list):
    """
    MyList class that inherits from list and provides
    a method to print the list sorted in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list elements sorted in ascending order without modifying the original list.
        """
        print(sorted(self))
