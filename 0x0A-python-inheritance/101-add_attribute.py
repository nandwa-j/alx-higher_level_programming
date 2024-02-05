#!/usr/bin/python3
"""This module contains the add_attribute function"""


def add_attribute(obj, objname, value):
    """add attribute to object
    args:
        obj: class object
        objname: object name
        value: value of attribute
    """
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, objname, value)
