import math

MESSAGE = 'MATHS IS AWESOME!!!'

'''
This code works like magic until Week 8 :D (when we teach you how to make your own classes!)
Or if you're really keen you can run the code, poke around and figure it out :))
'''
class Triangle:
    NUM_SIDES = 3

    def __init__(self, colour, *sides):
        # What is *sides?
        # * is an unpacking operator allows to additonal optional arguments
        # You may often see (*args, **kwargs), which means it takes in 
        # extra optional positional arguments, and keyword arguments
        print(sides)
        self.sides = sides
        self.__colour = colour

    @property
    def sides(self):
        return sorted([self.__a, self.__b, self.__c])

    @sides.setter
    def sides(self, sides):
        if len(sides) != 3:
            raise ValueError('Please enter 3 sides to create a triangle', sides)
        self.__a = sides[0]
        self.__b = sides[1]
        self.__c = sides[2]

    @property
    def colour(self):
        return self.__colour

    @colour.setter
    def colour(self, colour):
        self.__colour = colour

    def perimeter(self):
        return sum(self.sides)

    def area(self):
        p = self.perimeter() / 2
        return (p * (p - self.__a) * (p - self.__b) * (p - self.__c)) ** 0.5

def my_angle_finder(opposite=None, hypotenuse=None, adjacent=None):
    if opposite is not None and hypotenuse is not None:
        return math.asin(opposite / hypotenuse)
    elif adjacent is not None and hypotenuse is not None:
        return math.acos(adjacent / hypotenuse)
    elif adjacent is not None and opposite is not None:
        return math.atan2(opposite / adjacent)
