#!/usr/bin/python3
"""Defines a class-checking function"""


def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class; otherwise False.

    Args:
        obj: An object.
        a_class: A class.

    Returns:
        A boolean value indicating whether the object is exactly an instance of the specified class.
    """

    return type(obj) == a_class
