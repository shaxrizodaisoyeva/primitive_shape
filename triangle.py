from polygon import Polygon

class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def getArea(self):
        from math import sqrt
        d=(self.a+self.b+self.c)/2
        return sqrt(d*(d-self.a)*(d-self.b)*(d-self.c))

    def getPerimeter(self):
        return self.a+self.b+self.c