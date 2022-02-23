# Tutorial 2

## Core Exercises

## A. Code Review

[This exercise links to **Lab 02 - Code Review**](code_review.py).

In groups, discuss answers to the questions. If you have time, you can start modifying the code.

## B. Thinking About Testing

* What is a test list? Why is it important?
* What is a good approach to writing a test list?

[This exercise links to **Lab 02 - Testing**](testing.py).

## C. Test-Driven Development

* What is test-driven development? How does it help us write better code?
* Complete the stubs inside `test_list_exercises.py` as a class.
* In pairs, work on steps 2 and 3 of the exercise.

[This exercise links to **Lab 02 - List**](test_list_exercises.py).

## D. Fixtures

* What is a pytest fixture?
* How can we use fixtures to improve our tests?
* As a class, change `test_list_exercises.py` to use a fixture.

## Extra Exercises

## E. Testing in Python

Consider this problem:

 > Given a list of integers, compute the average of only the *positive* elements.

There is a stub for a function that solves this problem in [rainfall.py](rainfall.py). Before implementing it, write some pytest compatible tests for the function.

* What needs to be tested for?
* What are the edge cases and how should they be handled?

Once the tests are written, commit them to git.

## F. Python Programming

On a separate branch called `rainfall_solution`, implement the function such that it passes all the tests.

Use a **list comprehension** in your program.

* How confident are you that your solution is correct?
* Is your solution very different from how you might do it in C?

Once you have done this, `git checkout master` and replace the `rainfall` stub with the following solution:

<details>
<summary>Don't look at this until after you've solved the problem with a list comprehension!</summary>

```python
def rainfall(integers):
    '''
    Single-loop solution
    '''
    total = 0
    count = 0
    for i in integers:
        if  i > 0:
            total += i
            count += 1
    if (count > 0):
        return total/count
    else:
        return None
```

</details>

It should pass all the tests you have written.

## G. Git Merges

Try to merge `rainfall_solution` back into `master`. This will create a merge conflict.

With the class, discuss which solution is better and how you might resolve the merge conflict to ensure it is the one used.
