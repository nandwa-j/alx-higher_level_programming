#!/usr/bin/python3
"""This module contains the lookup function"""


def lookup(obj):
    """
    Args:
        obj: initial object
        Returns: a list of available attributes and
                 methods of an object
    """
    return dir(obj)
