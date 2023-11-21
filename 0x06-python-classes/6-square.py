#!/usr/bin/python3
"""Write an empty class Square that defines a square:"""
"""Defines a class Square"""

class Square:
    """Class that defines properties of square."""
    """Private instance attribute: size"""
    """__position (tuple): position of the square."""
    
    
    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with size"""
        """Instantiation with position"""
        self.__size = size
        self.position = position
        
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
    
    
    """Define a Getter"""
    @property
    def position(self):
        """Returns the position of a square"""
        return self.position
    
    """Define a Setter"""
    @size.setter
    def position(self, value):
        """Returns the position of a square"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
            
    """Public instance method: def my_print(self): that prints in stdout the square with the character """
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for j in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ",  end="")
                print("#" * (self.__size))
        
    pass
