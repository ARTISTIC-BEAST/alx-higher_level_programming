#!/usr/bin/python3
"""Square module"""
Rect = __import__('9-rectangle').Rectangle


class Square(Rect):
    """Square class"""

    def __init__(self, size):
        """[summary]
        Args:
            size (int): size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """overloading str method
        Returns:
            str: square data
        """

        sr = "[Square] {}/{}".format(self.__size, self.__size)
        return sr
