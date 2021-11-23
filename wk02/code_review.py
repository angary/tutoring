"""
What does this program do?

- Makes a new list, where all the even values have their value multiplied by 2

What style could be improved?

- The spacing is inconsistent
- Indentation is not 4 spaces (refer to style guide on webcms3)

Is this code pythonic?

- Could use for-in loop

List comprehension:

- A way of working with lists very concisely
"""

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# result = []

# for item in x:
#     if item % 2 == 0:
#         result.append(item * 2)
#     else:
#         result.append(item)

result = [i if i % 2 == 1 else i * 2 for i in range(1, 11)]

print(result)
