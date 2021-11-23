# Tutorial 2

## A. Code Review

Review this piece of code.

* What does it do?
* What style could be improved here?
* Is this code [pythonic](https://www.computerhope.com/jargon/p/pythonic.htm)? Fix it.

```python
x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []

for idx in range(len(x)):
  if x[idx] % 2 == 0:
    result.append(x[idx] * 2)
  else:
    result.append(x[idx])

print(result)
```

> Issues
>
> * Spacing not consistent
> * Indentation not 4 spaces (refer to style guide in webcms3)
> * Could use for-in loop in this case
> * `range(len(x))` is redundant, could just use range normally

## B. Thinking About Testing

The following `set_name` function is used to set a name according to the follow requirements on input:

* First Name must be at least 3 characters, and no more than 30.
* Last Name must be at least 3 characters, and no more than 50.
* First Name can only contain letters (uppercase or lowercase), and dashes.
* Last Name can only contain letters (uppercase or lowercase), spaces, and dashes.
* Middle Name can be None, but if it's not none, it can be between 1 and 50 characters.
* Middle Name cannot be longer than the first name, and it cannot be longer than the last name.

Your tutor will break you up into your project groups for this activity. Once completed you can come back together to discuss what you have.

The function returns `True` if the inputs are valid, and `False` if the inputs are invalid.

```python
def set_name(firstName, middleName, lastName):
    pass
```

Write a list of inputs and associated return values. This is good practice for trying to conceptualise edge case.

## C. Testing in Python

Consider this problem:

 > Given a list of integers, compute the average of only the *positive* elements.

There is a stub for a function that solves this problem in [rainfall.py](rainfall.py). Before implementing it, write some pytest compatible tests for the function.

* What needs to be tested for?
* What are the edge cases and how should they be handled?

Once the tests are written, commit them to git.

## D. Python Programming

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

## E. Git Merges

Try to merge `rainfall_solution` back into `master`. This will create a merge conflict.

With the class, discuss which solution is better and how you might resolve the merge conflict to ensure it is the one used.

## F. Fixtures

Keep both functions and name the new one `rainfall_alternative`.

Copy the first test and replace the function call to `rainfall` with `rainfall_alternative` (don't forget to change the name of the test function too).

Make sure the test still passes, now instead of passing the same test data to `rainfall` and `rainfall_alternative`, put it in a `fixture` and pass that to both of the test functions.

* How can we use fixtures to improve our tests?
