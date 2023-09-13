#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class that represents a rectangle.

    Attributes:
        __width: An integer representing the width of the rectangle.
        __height: An integer representing the height of the rectangle.

    Methods:
        area(): Returns the area of the rectangle.
        __str__(): Returns a string representation of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width: An integer representing the width of the rectangle.
            height: An integer representing the height of the rectangle.

        Returns:
            None.
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area of the rectangle.

        Args:
            None.

        Returns:
            The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Args:
            None.

        Returns:
            A string representation of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
