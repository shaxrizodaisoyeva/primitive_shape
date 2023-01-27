class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def distance_from_Xcoordinate(self):
        """
        This method finds the distance between a point and its X coordinates.

        Args:
            No
        Returns:
            float or int: distance.
        """
        from math import sqrt
        return sqrt((0-self.y)**2)

    def distance_from_Ycoordinate(self):
        """
        This method finds the distance between a point and its Y coordinates.

        Args:
            No
        Returns:
            float or int: distance.
        """
        from math import sqrt
        return sqrt((0-self.x)**2)

    def getQuadrant(self):
        """
        This method finds which quadrant the point is in.

        Args:
            No
        Returns:
            int: quadrant.
        """
        if self.x>0 and self.y>0:
            ans=1
        if self.x<0 and self.y>0:
            ans=2
        if self.x<0 and self.y<0:
            ans=3
        if self.x>0 and self.y<0:
            ans=4
        return ans

    def on_Xcoordinate(self):
        """
        This method checks for a point on the X coordinate.

        Args:
            No
        Returns:
            bool: result.
        """
        if self.y==0:
            ans=True
        else:
            ans=False
        return ans

    def on_Ycoordinate(self):
        """
        This method checks for a point on the Y coordinate.

        Args:
            No
        Returns:
            bool: result.
        """
        if self.x==0:
            ans=True
        else:
            ans=False
        return ans
 