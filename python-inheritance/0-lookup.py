#!/usr/bin/python3
"""
Module to return a list of available attributes and methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object whose attributes and methods are to be listed.

    Returns:
        list: List of attributes and methods of the object.
    """
    return dir(obj)
