#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """This class defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square class.

        Args:
        size (int, optional): The size of the square.
        position (tuple, optional): The position of a square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Gets the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
            self.__size = value

    @property
    def position(self):
        """Get the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2 or \
        not all(isinstance(i, int) for i in value) or \
        not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value

    def area(self):
       """Return the current area of the square."""
        return self.__size ** 2

    def my_print(self):
      """Print the square with the # character.""" 
        if self.__size == 0:
            print("")
            return
            
             [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
            
    def __str__(self):
        """Define the print() representation of a Square."""
        result = ""
        if self.__size == 0:
            result += "\n"
        else:
            for _ in range(self.__position[1]):
                result += "\n"
            for _ in range(self.__size):
                result += " " * self.__position[0] + "#" * self.__size + "\n"
        return result.rstrip()
