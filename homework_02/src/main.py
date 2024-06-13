import math

from circle import Circle
from rectangle import Rectangle
from square import Square
from triangle import Triangle


def main():
    triangle = Triangle(3, 4, 5)
    rectangle = Rectangle(2, 4)
    square = Square(3)
    circle = Circle(5)

    assert triangle.get_area() == 6.0
    assert rectangle.get_area() == 8
    assert square.get_area() == 9
    assert circle.get_area() == math.pi * 25

    assert triangle.add_area(circle) == 6.0 + math.pi * 25


if __name__ == "__main__":
    main()
