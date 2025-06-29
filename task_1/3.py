import math


class Shape:
    def area(self):
        return 0

    def perimeter(self):
        return 0
    

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width
    
    def perimeter(self):
        return 2 * (self.height + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * pow(self.radius, 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


shapes = [Circle(10), Circle(14), Rectangle(4, 10), Rectangle(7, 3)]
for shape in shapes:
    print(f"Area = {shape.area()}, Perimeter = {shape.perimeter()}")