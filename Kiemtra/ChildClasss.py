# 3.	Xây dựng 3 lớp con Circle, Rect, Triangle kế thừa lớp Shape
import math
from Shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
# chu vi = pi x 2 x ban kinh
# radius la ban kinh

    def perimeter(self):
        return 2 * math.pi * self.radius
# dien tich

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
