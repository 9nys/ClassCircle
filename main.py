import math


class Circle:

    class_pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.class_pi * self.radius ** 2


radius = 5
circle = Circle(radius)
print("Площа круга:", circle.area())
