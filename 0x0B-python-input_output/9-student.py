#!/usr/bin/python3
""" My student class module
"""

class Student:
    """ My student class module
    """
    
    def __init__(self, first_name, last_name, age):
        """ Initialize attributes
            Constructor method
        """
        self.first_name = first_name
        self.last_name  = last_name
        self.age        = age
        
    def to_json(self):
        """Method that returns directory description"""
        return self.__dict__.copy()
    