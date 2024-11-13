#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of the specified class or
    a class that inherits from it.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if the object is an instance of a_class or if the object 
        is an instance of a class that inherited from a_class, else False.
    """
    return isinstance(obj, a_class)
