#!/usr/bin/python3
"""Defines a class and inherited class-checking function"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an instance of a class that inherited from,
    the specified class; otherwise False.

    Args:
        obj: An object.
        a_class: A class.

    Returns:
        A boolean value indicating whether the object is an instance of, or if the object is an instance of a class
        that inherited from, the specified class.
    """
    return isinstance(obj, a_class)
