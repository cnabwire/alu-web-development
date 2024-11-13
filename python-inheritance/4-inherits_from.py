#!/usr/bin/python3
"""
This module contains a function that checks if an obj.. is an inst...
of a class that inherited from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited from
    the specified class, either directly or indirectly.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a class that inherited 
        from a_class, else False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
