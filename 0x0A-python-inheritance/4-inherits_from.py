#!/usr/bin/python3
"""Module containing is_same_class method"""
def inherits_from(obj, a_class):
    """Returns:
    True: if the object is exactly an instance of the specified class
    False: otherwise"""
    return isinstance(obj, a_class) and type(obj) != a_class
