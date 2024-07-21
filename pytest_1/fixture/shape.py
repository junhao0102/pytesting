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


class rectangle(shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    #----檢查 other 物件是否是 rectangle 類別的實例----
    def __eq__(self, other):
        if not isinstance(other, rectangle):
            return False
        return self.length == other.length and self.width == other.width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length + self.width) * 2
