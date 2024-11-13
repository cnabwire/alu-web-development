#!/usr/bin/python3
""" shebang line"""


from 7-base_geometry import BaseGeometry
"""inherits from previous class"""

class Rectangle(BaseGeometry):
    """
    Represents a rectangle that inherits from BaseGeometry.

    This class validates the dimensions of the rectangle (width and height)
    to ensure they are positive integers.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle instance with width and height.

        Validates the width and height to ensure they are positive integers.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not greater than 0.
        """
        self.integer_validator("width", width)  # Validate width
        self.integer_validator("height", height)  # Validate height
        self.__width = width  # Set the private width attribute
        self.__height = height  # Set the private height attribute

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.

        The string representation is in the format: [Rectangle] <width>/<height>

        Returns:
            str: The string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Computes the area of the rectangle.

        The area is calculated as width * height.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

