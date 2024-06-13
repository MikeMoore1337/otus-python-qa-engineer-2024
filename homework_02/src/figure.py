class Figure:
    def get_area(self):
        raise NotImplementedError("This method should be overridden in subclasses")

    def get_perimeter(self):
        raise NotImplementedError("This method should be overridden in subclasses")

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("The argument must be an instance of Figure")
        return self.get_area() + figure.get_area()
