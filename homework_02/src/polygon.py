from figure import Figure


class Polygon(Figure):
    def __init__(self, sides):
        self.sides = sides
        if not self._is_valid_polygon():
            raise ValueError("The sides do not form a valid polygon")

    def get_perimeter(self):
        return sum(self.sides)

    def _is_valid_polygon(self):
        raise NotImplementedError("This method should be overridden in subclasses")
