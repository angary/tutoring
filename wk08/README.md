# Tutorial 8

## A. Creating your own routes

This exercise links to **[Lab08 - Routes](routes.md)**.

Break into random groups of 5 to complete the brainstorming part of the exercise.

## B. Decorators

### Part 1 - Currying in Python

* How can a function return a function in Python?
* What will the following program print? Try to figure it out before running the program.

```python
def f():
    def g():
        return 1
    return g

def i(x):
    def j(y):
        return x + y
    return j

print(f())
print(f()())
print(i(1))
print(i(1)(2))
```

### Part 2 - ISBN Validator

An ISBN (International Standard Book Number) is a 10 character string assigned to every commercial book before 2007. Each character is a digit between 0 and 9, but the last character might also be 'X'.

We have written a program in [isbn.py](isbn.py) that asks the user for an ISBN (in `main`) and determines whether it is valid or not (in `is_valid()`).

The check for validity goes as follows:
* Multiply each of the first 9 digits by its position. The positions go from 1 to 9.
* Add up the 9 resulting products.
* Divide this sum by 11, and get the remainder, which is a number between 0 and 10.
* If the remainder is 10, the last character should be the letter 'X'. Otherwise, the last character should be the remainder (a single digit).

#### Examples

```txt
What is the ISBN? 1503290565
1503290565 is valid
```

```txt
What is the ISBN? 938007834X
938007834X is valid
```

```txt
What is the ISBN? 2222222224
2222222224 is invalid
```

In [decorator.py](decorator.py) complete the decorator function `ISBNValidator` which calls the `isValid` function from the previous part, and checks whether the input is a valid ISBN. If not, raise a `ValueError`.

For example:

```bash
$ python3 decorator.py
What is the ISBN? 938007834X
Printing book <Legend of Hayden>
ISBN: 938007834X
```

```bash
$ python3 decorator.py
What is the ISBN? 2222222224
2222222224 is invalid.
```

## D. Functional and Non-Functional

* What is the difference between functional and non functional requirements? (See lecture slides)
* Are the following requirements functional or non functional?
  1. Every unsuccessful attempt by a user to access an item of data shall be recorded on an audit trail.
  2. Privacy of information, the export of restricted technologies, intellectual property rights, etc. should be audited.
  3. The software system should be integrated with banking API

## E. Property-Based Testing

*This is not core course content*.

In `divisors.py`, we have written a function which for any positive integer `n`, returns a set of all the numbers that divide it.

A simple test is located in `divisors_test.py`. Consider what property, or properties, this function has and write them as property-based tests.
