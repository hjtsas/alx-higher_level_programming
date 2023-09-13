#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """
    A base class for other geometry classes.

    Attributes:
        None.

    Methods:
        area(): Raises an Exception with the message "area() is not implemented".
    """

    def area(self):
        """
        Raises an Exception with the message "area() is not implemented".

        Args:
            None.

        Returns:
            None.
        """
        raise Exception("area() is not implemented")
