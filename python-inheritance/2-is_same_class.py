#!/usr/bin/python3
""" This module fedines the function 'is_same_class'"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an instance of the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if the object is an instance of the class, False otherwise.
    """
    return type(obj) is a_class
