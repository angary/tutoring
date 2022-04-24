# Tutorial 10

## A. MyExperience

It's time to fill out MyExperience!!

## B. Kahoot Activity

You will spend the first part of the tutorial doing a kahoot activity with your tutor. They will share a code with you!

## C. Generators

Write a function `generate(n)` that yields all of the fibonacci numbers up to n using a generator.

As you complete the exercise, discuss:
* What is a generator?

> Iterator that returns values according to a defined function

```py
# Uses a list
for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]:
    print(i)

# Using a generator
for i in range(15):
    print(i)
```

* What does the `yield` keyword do?

> Pauses the flow of the program and returns the given value, continuing on when the generator is next called

* How can we use the values returned by generators?

> Use in a a for loop, convert it into a list / iterable, use `next()` function

## D. General Revision

You can spend time with your tutor to review any topics in the course that you feel you want to build more confidence in.
