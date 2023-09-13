#!/usr/bin/python3
"""Defines an inherited class-checking function"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class;
    otherwise False.

    Args:
        obj: An object.
        a_class: A class.

    Returns:
        A boolean value indicating whether the object is an instance of a class that inherited (directly or indirectly)
        from the specified class.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
