#!/usr/bin/python3
"""
Class MyList that inherits from the built-in list class and adds a method
to print the list sorted in ascending order.
"""


class MyList(list):
    """
    A class that inherits from the built-in list class and adds a method to
    print the list sorted in ascending order.
    """
    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.
        """
        print(sorted(self))
