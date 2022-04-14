from typing import Tuple

class Point:
    def __init__(self, x: int, y: int) -> None:
        '''
        Initialises the point with the given co-ordinates
        '''
        self.x = x
        self.y = y

    def get_coords(self) -> Tuple[int, int]:
        '''
        Returns the co-ordinates as a tuple
        '''
        return (self.x, self.y)

    def set_x(self, x: int) -> None:
        '''
        Sets the x co-ordinate
        '''
        self.x = x

    def set_y(self, y: int) -> None:
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

    def __sub__(self, point: "Point") -> "Point":
        '''
        Returns a new point which is the vector addition of this point,
        and the point given.

        Both this point and the point given remain unchanged.
        '''
        return Point(self.x - point.x, self.y - point.y)

    def __mul__(self, scalar: int) -> "Point":
        '''
        Returns a new point which is the scalar multiplication of this point and
        the given value.

        This point remains unchanged.
        '''
        return Point(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: int) -> "Point":
        '''
        Returns a new point which is the scalar multiplication of this point and
        the given value.

        This point remains unchanged.
        '''
        return Point(self.x * scalar, self.y * scalar)

if __name__ == '__main__':
    p1 = Point(10, 10)
    p2 = Point(5, 5)
    # p3 = p1.__add__(p2)
    p3 = p1 + p2
    print(p3.get_coords())
    p4 = p1 * 4
    print(p4.get_coords())
