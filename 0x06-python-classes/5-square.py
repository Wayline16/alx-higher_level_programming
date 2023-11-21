#!/usr/bin/python3
"""Write an empty class Square that defines a square:"""
"""Defines a class Square"""

class Square:
    """Class that defines properties of square."""
    """Private instance attribute: size"""
    
    
    def __init__(self, size=0):
        """Instantiation with size"""
        self.__size = size
        
    """Public instance method: def area(self): that returns the current square area"""
    def area(self):
        """Return: Area of a Square"""
        return self.__size ** 2
    
    """Define a Getter"""
    @property
    def size(self):
        """Returns the size of a square"""
        return self.__size
    
    """Define a Setter"""
    @size.setter
    def size(self, value):
        """Returns the size of a square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
            
    """Public instance method: def my_print(self): that prints in stdout the square with the character """
    def my_print(self):
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * (self.__size))
        
    pass
