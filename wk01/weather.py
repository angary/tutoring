"""
A simple program to print out a recommendation for what to wear out given the 
weather.

WHy don't we need to specify the type of a variable when we declare it?
- Python is dynamically typed, and it is also an interpreted language

How do we denote code blocks in Python compared to C?
- We use indentation to denote code blocks instead of curly brackets in C

How is the `print` function in Python different to `printf` in C?
- No semicolons (goes for everyline in python)
- Python's print function automatically adds a '\n'
- In C, you can use %s to print out a string (in python, you can use f-strings)

"""

# Scan in the input as a string in weather
weather = input()

if weather == "raining":
    print("You should wear a raincoat when you go out")
elif weather == "sunny":
    print("You should wear a hat when you go out")
else:
    print("Have a nice day")
