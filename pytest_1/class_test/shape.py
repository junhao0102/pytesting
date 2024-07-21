class shape:

    def area(self):
        pass

    def perimeter(self):
        pass


class circle(shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2 * 3.14 * self.radius
