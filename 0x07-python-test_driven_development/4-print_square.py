#!/usr/bin/python3
"""This module contains a function to print a square"""



def print_square(size):
    """
        Prints a square with the character '#'

        Args:
            size: size length of the square

        Raises:
        TypeError: If size is not an integer
        TypeError: If size is a float and less than zero
        ValueError: If size is less than zero

    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
