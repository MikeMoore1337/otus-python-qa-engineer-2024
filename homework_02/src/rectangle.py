from polygon import Polygon


class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__([width, height, width, height])

    def _is_valid_polygon(self):
        return True

    def get_area(self):
        width, height = self.sides[:2]
        return width * height
