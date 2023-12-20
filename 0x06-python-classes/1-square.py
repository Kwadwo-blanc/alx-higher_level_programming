#!/usr/bin/python3

class Square:
    """
    This class represents a square.

    The purpose of this class is to define a square by having a private
    instance attribute 'size' and allowing instantiation with a given size
    (without type or value verification).
    """

    def __init__(self, size):
        """
        Initializes a new instance of the Square class.

        Args:
        - size (int): The size of the square.

        Note:
        The size is a private attribute and is not type or value verified.
        """
        self.__size = size
