#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""

class MyInt(int):
    """
    A class that represents an integer with inverted == and != operators.

    Attributes:
        None.

    Methods:
        __eq__(self, other): Inverts the == operator.
        __ne__(self, other): Inverts the != operator.
    """

    def __eq__(self, other):
        """
        Inverts the == operator.

        Args:
            other: An object to compare with.

        Returns:
            A boolean value indicating whether the two objects are not equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator.

        Args:
            other: An object to compare with.

        Returns:
            A boolean value indicating whether the two objects are equal.
        """
        return super().__eq__(other)
