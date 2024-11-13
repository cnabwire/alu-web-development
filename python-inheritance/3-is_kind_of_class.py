#!/usr/bin/python3
"""
This module contains a function that checks if an object is an instance
of a specific class or if it is an instance of a class that inherited
from the specified class.
"""

def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of the specified class or
    a class that inherits from it.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a_class or if the obj...
        is an inst.. of a class that inherited from a_class, else False.
    """
    return type(obj) is a_class or issubclass(type(obj), a_class)
