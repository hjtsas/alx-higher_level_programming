#!/usr/bin/python3
"""Defines an inherited list class mylist"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.

    Attributes:
        None.

    Methods:
        print_sorted(): Prints the list in ascending order.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.

        Args:
            None.

        Returns:
            None.
        """
        print(sorted(self))
