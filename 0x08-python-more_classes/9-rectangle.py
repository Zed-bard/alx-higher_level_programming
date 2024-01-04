#!/usr/bin/python3
"""
Contains a definition for class rectangle.
"""


class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.set_dimensions(width, height)
        type(self).number_of_instances += 1

    def set_dimensions(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_dimension(value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_dimension(value)
        self.__height = value

    def validate_dimension(self, value):
        if not isinstance(value, int):
            raise TypeError("Dimension must be an integer")
        elif value < 0:
            raise ValueError("Dimension must be >= 0")

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height) if self.width > 0 and self.height > 0 else 0

    def __str__(self):
        return '\n'.join([str(self.print_symbol) * self.width for _ in range(self.height)])

    def __repr__(self):
        return f'{self.__class__.__name__}({self.width}, {self.height})'

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @classmethod
    def bigger_or_equal(cls, rect_1, rect_2):
        if not all(isinstance(rect, cls) for rect in (rect_1, rect_2)):
            raise TypeError("Both rectangles must be instances of Rectangle")
        return max(rect_1, rect_2, key=lambda rect: rect.area())

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
