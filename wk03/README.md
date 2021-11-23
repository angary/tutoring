# Tutorial 3

## A. Code Review

Your tutor will select one of your classmate's code from Lab02 to present and discuss as a class.

Is the code:
* Compliant with the COMP1531 Style Guide?
* Pythonic in nature?

## B. Agile

Each group in the tutorial should share a summary of their teams plans and progress in relation to:
 * When (or if) they are running standups and whether they are synchronous or asynchronous
 * How often they meet, how they meet, and what the goals/outcomes of any meetings so far have been
 * Have they or will they try pair programming
 * Any challenges they've faced already after being in a group for a week

Other group members (in other teams) are encouraged to ask questions and learn from what other groups are doing/saying.

## C. Finding Vowels

### Part 1 - Dictionaries

Write a python program in a new file `vowel.py` that takes in a series of words on a single line in from standard input, passes that input string into a function called `find_vowels`, which then return the frequency of how often each vowel appears. This object is then outputted (however you think works best). Assume all input is lowercase or uppercase letters, or spaces.

```python
def find_vowels(message):
    pass

if __name__ == '__main__':
    pass
```

### Part 2 - Exception Throwing & Handling

If there are any uppercase letters passed in as part of the input, a `ValueError` should be thrown and caught in the main part of the code. The user should then be given a clear error message.

* First, write a failing unit test that asserts the error is thrown
* Then modify your code so that the test passes
* Then, update the `if __name__` block to catch the exceptional case.

## D. Importing

Here is a file *foo.py*
```python
def bar(txt):
    return txt

name = 'Ralph'
def editName(string):
    name = string
def getName():
    return name
```

In the same directory we have a file *imp.py*. There are multiple ways we can import and use a function in another file. Discuss each.
```python
import foo
print(foo.bar('hi')) # 1

import foo as fooFile
print(fooFile.bar('hi')) # 2

from foo import bar
print(bar('hi')) # 3

from foo import *
print(bar('hi')) # 4
```

Why does the following function not behave as intended?
```python
import foo

print(foo.getName())
foo.editName('Hayden')
print(foo.getName())
```

## E. Files

Write a python program that:
* Opens a file `tolstoy.txt`;
* Writes the contents of that file with all punctuation removed from the start and end of each word to `no_punctuation.txt`.

Use a `with`/`as` statement and `string.punctuation` in your code.
