#!/usr/bin/python3
"""
This module defines a class BaseGeometry with a method area() that
raises an exception.
"""


class BaseGeometry:
    """
    A class that represents a base geometry object.
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")
