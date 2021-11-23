# Import the library
import my_math_library as mml

# Create the following triangle
triangle = mml.Triangle("blue", 3, 4, 5)

# How many sides does the triangle have?
print(f"There are {len(triangle.sides)} sides to this triangle.")
print(f"The sides are of length {triangle.sides}")

# What is the area of the triangle
print(f"The area of the triangle is {triangle.area()}")

# What is the perimeter of the triangle
print(f"The perimeter of the triangle is {triangle.perimeter()}")

# What the angle between the side of length 5 and 3
print(f"The angle between 5 and 3 is (found using sin) {mml.my_angle_finder(hypotenuse=5, opposite=3)} radians")
print(f"The angle between 5 and 3 is (found using cos) {mml.my_angle_finder(hypotenuse=5, adjacent=3)} radians")

"""
What is the difference between a module, a class and a function?

- module   : A python file that contains classes, and or functions, and or variables
- class    : A struct that also contains functions
- function : Something that takes in input, and can give an output

What is the difference between "normal" function and a method of an object?

- function : It exists, and can take in input, and return output
- method   : A method exists inside a class and is accessed like object.method()

What is the difference between a "normal" variable and an attribute of an object?

- variable  : It exists in a python program
- attribute : This lives inside the object, and is accessed like object.attribute
"""
