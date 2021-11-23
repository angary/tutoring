"""
Difference between a "class" and an "object":

Class is like a blueprint for making an object
Object is an instance of a class
"""
from typing import Tuple


class Point:
    def __init__(self, x: float, y: float):
        '''
        Initialises the point with the given co-ordinates
        '''
        self.x = x
        self.y = y

    def get_coords(self) -> Tuple[float, float]:
        '''
        Returns the co-ordinates as a tuple
        '''
        return (self.x, self.y)

    def set_x(self, x: float):
        '''
        Sets the x co-ordinate
        '''
        self.x = x

    def set_y(self, y: float):
        '''
        Sets the y co-ordinate
        '''
        self.y = y

    def __add__(self, point: "Point") -> "Point":
        '''
        Returns a new point which is the vector addition of this point,
        and the point given.

        Both this point and the point given remain unchanged.
        '''
        return Point(self.x + point.x, self.y + point.y)
        

    def __mul__(self, scalar: float) -> "Point":
        '''
        Returns a new point which is the scalar multiplication of this point and
        the given value.

        This point remains unchanged.
        '''
        return Point(self.x * scalar, self.y * scalar)

if __name__ == '__main__':
    # Make a point
    x = Point(10, 10)
    y = Point(5, 5)
    # print(x.get_coords())
    z = x + y # same as z = x.__add__(y)
    # print(z.get_coords())
    # z = x * 3 # this works
    # z = 3 * x # this does not work
    print(z.get_coords())
