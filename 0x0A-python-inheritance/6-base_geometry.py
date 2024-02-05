#!/usr/bin/python3
"""This is a module container of the function base_geometry"""


class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")
