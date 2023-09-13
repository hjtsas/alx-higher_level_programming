#!/usr/bin/python3
"""Defines a Rectangle subclass Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class that represents a square.

    Attributes:
        __size: An integer representing the size of the square.

    Methods:
        area(): Returns the area of the square.
        __str__(): Returns a string representation of the square.
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
            size: An integer representing the size of the square.

        Returns:
            None.
        """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returns the area of the square.

        Args:
            None.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.

        Args:
            None.

        Returns:
            A string representation of the square.
        """
        return f"[Square] {self.__size}/{self.__size}"
