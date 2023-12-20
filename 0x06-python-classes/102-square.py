#!/usr/bin/python3

class Square:
    """
    This class defines a square.

    Attributes:
    - size (float or int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
        - size (float or int, optional): The size of the square.

        Raises:
        - TypeError: If size is not a number (float or integer).
        - ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the current size of the square.

        Returns:
        - float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
        - value (float or int): The size to set.

        Raises:
        - TypeError: If value is not a number (float or integer).
        - ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number (float or integer)")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        - float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if two squares are equal based on their area.

        Args:
        - other (Square): The other square to compare.

        Returns:
        - bool: True if equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """
        Checks if two squares are not equal based on their area.

        Args:
        - other (Square): The other square to compare.

        Returns:
        - bool: True if not equal, False otherwise.
        """
        return not self.__eq__(other)

    def __gt__(self, other):
        """
        Checks if one square is greater than the other based on their area.

        Args:
        - other (Square): The other square to compare.

        Returns:
        - bool: True if greater, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """
        Checks if one square is greater than or equal to the other.

        Args:
        - other (Square): The other square to compare.

        Returns:
        - bool: True if greater than or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        """
        Checks if one square is less than the other based on their area.

        Args:
        - other (Square): The other square to compare.

        Returns:
        - bool: True if less, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """
        Checks if one square is less than or equal to the other.

        Args:
        - other (Square): The other square to compare.

        Returns:
        - bool: True if less than or equal, False otherwise.
        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return False
