class Line:
    def __init__(self, x1, y1, x2, y2) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_length(self):
        """
        This method finds the length of line.

        Args:
            No
        Returns:
            float or int: distance.
        """
        from math import sqrt
        return sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
a=Line(2,3,4,9)
print(a.get_length())