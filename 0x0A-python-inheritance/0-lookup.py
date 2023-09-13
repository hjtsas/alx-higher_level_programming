#!/usr/bin/python3
"""Defines an object attribute function"""


def lookup(obj):
    """
    Returns a list of all available attributes and methods of an object.

    Args:
        obj: An object.

    Returns:
        A list of strings representing the attributes and methods of the input object.
    """
    return dir(obj)
