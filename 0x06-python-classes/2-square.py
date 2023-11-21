#!/usr/bin/python3
""""Write an empty class Square that defines a square:"""
"""Defines a class Square"""

class Square:
    """Class that defines properties of square."""
    """"Private instance attribute: size"""
    
    
    def __init__(self, size=0):
        """"Instantiation with size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    pass
