from polygon import Polygon

class Square(Polygon):
    def __init__(self, height):
        super().__init__(height,height)
    pass

a=Square(4)
print(a.getArea())