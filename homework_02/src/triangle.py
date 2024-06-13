import math

from polygon import Polygon


class Triangle(Polygon):
    def __init__(self, a, b, c):
        super().__init__([a, b, c])

    def _is_valid_polygon(self):
        a, b, c = self.sides
        return a + b > c and a + c > b and b + c > a

    def get_area(self):
        a, b, c = self.sides
        s = self.get_perimeter() / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
