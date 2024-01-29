#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """This is a represantation of a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing the rectangle class

        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than zero
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrives the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__height * self.__width

    def __str__(self):
        """Returns a printable string representation of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        string = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle += "#"
            if column < self.__height - 1:
                rectangle += "\n"
        return string
