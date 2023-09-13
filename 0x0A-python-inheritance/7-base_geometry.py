#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """
    A base class for other geometry classes.

    Attributes:
        None.

    Methods:
        area(): Raises an Exception with the message "area() is not implemented".
        integer_validator(name, value): Validates value.
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

    def integer_validator(self, name, value):
        """
        Validates value.

        Args:
            name: A string representing the name of the value.
            value: An integer representing the value to be validated.

        Returns:
            None.
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
