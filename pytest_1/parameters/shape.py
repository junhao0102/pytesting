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
    
class recangle(shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
class square(recangle):
    #----通過調用 super() 函式，調用了父類 rectangle 的 __init__ 方法----
    def __init__(self, sidelength):
        super().__init__(sidelength,sidelength)
        

