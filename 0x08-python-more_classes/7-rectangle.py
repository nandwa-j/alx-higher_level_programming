#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """This is a representation of a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute"""
        if not isinstance(value, int):
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """Returns a printable string representation of a rectangle"""
        rectangle = ""
        if self.__width != 0 and self.__height != 0:
            rectangle += "\n".join(str(self.print_symbol) * self.__width
                                   for j in range(self.__height))
        return rectangle

    def __repr__(self):
        """Returns a string representation of the rectangle for reproduction"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message for every object that is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
