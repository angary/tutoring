"""
What does it do?
- It prints out all the values of the array, except that if it is even, the
  value is multiplied by two

What style could be improved here?
- Spacing not consistent
- Indentation not 4 spaces (refer to style guide on webcms3)
- Could use for-range loop in this case
- range(len(x)) is redundant, could just use range normally
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
result = []

# For loop method
# for number in numbers:
#   if number % 2 == 0:
#     result.append(number * 2)
#   else:
#     result.append(number)

# List Comprehension method
result = [i * 2 if i % 2 == 0 else i for i in numbers]

# print(result)


print(result)
