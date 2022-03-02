# Tutorial 3

## A. Code Review

**[This exercise links to Lab03 - Wondrous](wondrous.py)**.

**Without running the code**, in your project groups try to figure out what the bugs are and how to resolve them.

## B. Agile

**[This exercise links to Lab03 - Agile](https://gitlab.cse.unsw.edu.au/COMP1531/22T1/STAFF/repos/lab03/lab03_agile)**.

Your tutor will break you up into groups, with people who you are not in the same project team as you. You will have around 10 minutes to complete the group activity for the lab.

After that time, share thoughts among the class.

## C. Finding Vowels

### Part 1 - Dictionaries

Write a python program in a new file [vowel.py](vowel.py) that takes in a series of words on a single line in from standard input, passes that input string into a function called `find_vowels`, which then return the frequency of how often each vowel appears.
This object is then outputted (however you think works best). 
Assume all input is lowercase or uppercase letters, or spaces.

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
