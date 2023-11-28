#!/usr/bin/python3
"""
Write an empty class Rectangle that defines a rectangle:
"""
class Rectangle:
    """class thats take in two parameters, creates private instance attributes by
    taking in two arguments.
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        
    @property
    def width(self):
        """__width getter.

        Returns:
            __width (int): horizontal dimension of rectangle

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): horizontal dimension of rectangle

        Attributes:
            __width (int): horizontal dimension of rectangle

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less than 0.

        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """__height getter.

        Returns:
            __height (int): vertical dimension of rectangle

        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """Args:
                value (int): vertical dimension of rectangle

            Attributes:
                __height (int): vertical dimension of rectangle

            Raises:
                TypeError: If `value` is not an int.
                ValueError: If `value` is less than 0.
        """
        if type(value) is not int:
            raise TypeError('height  must be an integer')
        elif value < 0:
            raise ValueError('height  must be >= 0')
        self.__height = value
    
    def area(self):
        """
        Returns:
            area of a rectangle

        """
        return int(self.height) * int(self.width)
    
    def perimeter(self):
        """
        Returns:
            parameter of a rectangle
        """
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height * 2) + (self.width * 2)
            
        
    pass
