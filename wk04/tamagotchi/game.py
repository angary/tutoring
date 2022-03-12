"""
Create a new Tamagotchi object and invoke some of its methods.

As you do this, discuss:
What is the difference between a module, a class, and a function?
- Module: Is a file that contains implementations of classes or functions or variables
  that you can import
- Class: A class is a new data type that can contain it's own variables and functions
  
- Function: A piece of code that can take in parameters and return something, or do something

What is the difference between a class and an object?
- A class is a blueprint for an object, and an object is an instance of a class

What is the difference between normal function and a method of an object?
- A method is just a function that exists inside a class / object

"""

from tamagotchi import Tamagotchi

tamagotchi = Tamagotchi("Alfredo")

print("Just born!")
print(tamagotchi)

print("After one day")
tamagotchi.increment_time()
print(tamagotchi)

print("Fed and after two days")
tamagotchi.feed()
tamagotchi.increment_time()
print(tamagotchi)
