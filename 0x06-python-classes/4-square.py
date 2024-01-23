#!/usr/bin/python3
"""A module that defines a square by its size """


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Method to initialize the square class
        Arguments:
            size: the size of the square
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
         """ A method that calculates the area of a square
        """
        return (self.__size ** 2)
     @property
    def size(self):
        """ a method that retrieves the size of a square"""

        return self.__size

     @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
