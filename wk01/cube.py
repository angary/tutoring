"""
A program that prints out hte cube of a given number

Why don't Python programs need a `main` function?
- Python has an interpreter (instead of a compiler), and it just reads the code
  from top down

Why do we need to write a function declaration for
`cube` at the top of the file?
- Because the python interpreter is not aware that the function exists until it has read it


What operator can we use instead of needing to write `x * x * x`?
- The operator is `**`

"""

# Define a function before it is used
def cube(x):
    return x ** 3

# Scan in input and convert it to an int from a string
number = int(input("Please enter a number: "))

# Print out the value cubed
result = cube(number)
print(f"The cube of the number you have entered is {result}")
