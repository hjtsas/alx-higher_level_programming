#!/usr/bin/python3
"""Defines a function that adds attributes to object"""


def add_attribute(obj, name, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: An object.
        name: A string representing the name of the attribute.
        value: The value of the attribute.

    Returns:
        None.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
