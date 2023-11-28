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
        return int(self.__height) * int(self.__width)
    
    def perimeter(self):
        """
        Returns:
            parameter of a rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)
            
    def draw_rectangle(self):
        """
        @str: is a string that contains the "#" that will build the rectangle
        Returns:
            str (str): string suitable for printing rectangle (final newline
            omitted)
        """
        str = ""
        if self.__height == 0 or self.__width == 0:
            return str
        else:
            for row in range(self.__height):
                for colunm in range(self.__width):
                    str += "#"
                if self.__width != 0 and row < (self.__height - 1):
                    str += '\n'
            return str
    
    def __str__(self):
        """Allows direct printing of instances.

        Returns:
            The output of _draw_rectangle, which creates a string
        representation of the rectangle suitable for printing.

        """
        return self.draw_rectangle()
    
    def __repr__(self):
        """Allows use of eval().

        Returns:
            A string of the code needed to create the instance.

        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
    
    @staticmethod
    def __del__():
        """Prints message upon deletion of instance.

        """
        print('Bye rectangle...')
        
    
    pass
