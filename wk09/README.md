# Tutorial 9

## A. System Modelling

Generate a state diagram to describe the states and subsequent transitions that would occur for a grocery store checkout system, from the perspective of the user-machine interaction.

![](https://www.canstarblue.com.au/wp-content/uploads/2018/09/shutterstock_793003627-300x189.jpg)

> I recommend checking out "Lucid Chart" (this can be useful for iteration 3 or COMP2511)
> https://lucid.app/lucidchart/e00bd92b-b562-4bb2-b26f-d1e3d5501acb/edit?viewport_loc=335%2C55%2C1516%2C844%2C0_0&invitationId=inv_8a2c94ac-c3c0-40ee-bfef-25b871a6958e


## B. Type Hints

Consider the `names_ages` code from Tute 05 where we made a simple flask server.

Add type hints to each function in `names_ages.py`. In an `if __name__ == '__main__'` block, call the function with a few values and use `mypy` to type-check the validity of the function calls.

> Video on the importance of types
> https://youtu.be/pMgmKJyWKn8?t=317

## C. A Simple Class

In `point.py`, complete the class definition according to the provided documentation.

As you complete the exercise, discuss as a class:

* Revision: what is a class versus an object?
* What is the `__init__` method?
* What is `self`?
* How are the `__add__` and `__mul__`  methods different from normal methods, and how can we use them?

## D. Exam-Style Problem

Write a program in [acronym.py](acronym.py) that asks the user for a multi-word name and then passes it to a function `acro` that returns the corresponding acronym, which is then printed to the user.

Example usage:
```txt
What is the name? World Health Organisation
It's acronym is WHO.
```
