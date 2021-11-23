# Code Quality

One of the great things about this course is that we begin focusing on tangible code quality.
There are many measures of "code quality", but I am to cover the main ones in this course.

## Pythonic

When starting out 1531, with C fresh in their memory, it is easy to write "Python" code, in the sense that yes it is valid Python syntax, but they write it as though they are still using C.
Either that, or you may avoid Python's new syntax because you are more comfortable with what you know.
To that I say please try out what Python has to offer!
And it's *totally not because we assess you on it*, but because Python has fantastic features allow you to not only code faster, but also write beautiful elegant code.

Below are some code snippets that showcase improvements that you can make to your code.
That being said, it doesn't cover everything, and hopefully you feel inspired enough to discover yourself other ways to write better Python code.

### Checking if something is in a list

Typically, you might have a flag (a variable, typically a boolean) that tracks if something is found or not.
After looping through the list, you then have handle what happens if the value is not found.

```py
found = False
for value in values:
    if value == thing_to_find:
        found = True

if not found:
    do_something()
```

A `for ... else` loop can be used in place of this.
This is done by having a `for` loop that contains a `break` somewhere inside it, and then having an `else` statement immediately after the `for` loop.
If the `break` is never triggered during the `for` loop, then the `else` statement will be triggered.

```py
for value in values:
    if value == thing_to_find:
        break
else:
    do_something()
```

Even cleaner is something like 

```py
if thing_to_find not in values:
    do_something()
```

where the `in` keyword checks if the value `x` is inside the list `xs`.
Adding the `not` keyword means that we take the opposite, i.e. `not False == True`.

### Checking for something in a list of dictionaries

Ok, but what if we can't use the `in` keyword because we are want to check that a value inside a dictionary inside a list of dictionaries exists?

Here, `xs` is a list of dictionaries and we want to check if `thing_to_find` is a value in one of the dictionaries, where the key name is `"key"`.

You may to for a `for ... else` loop:

```py
for x in xs:
    if x["key"] == thing_to_find:
        break
else:
    do_something()
```

However, we can use a **list comprehension**, where we extract out all the values with the key `"key"` from the dictionaries into a new list, and then check if our value is in that list.

```py
if thing_to_find not in [x["key"] for x in xs]:
    do_something()
```

Now the algorithmically inclined (or those that have done COMP2521) may argue that the first solution was faster as it stops looping once it finds the value.
To that I say it is irrelevant for the following reasons:

1. This is a software engineering course (not a course that focuses on optimisation)
2. This still runs in linear time
3. The data in this course is not big enough for it to be relevant

### Extracting certain values from a list

What if we want to extract everything from a list based of a certain condition?

```py
new_values = []
for value in values:
    if some_condition(value):
        new_values.append(value)
```

We can also do this in one line with a **list comprehension** (yes list comprehensions are very useful)!

```py
new_values = [value for value in values if some_condition(value)]
```

### Safely getting values

In fact, we can also use **list comprehensions** for the previous problem of finding a value in an array.
The following two functions are identical in functionality.

```py
def find_val(values, thing_to_find):
    for value in values:
        if value["key"] == thing_to_find:
            return value
    # This next line is not necessary as by default Python returns None anyways
    return None

def find_val(values, thing_to_find):
    return [x for x in values if x["key"] == thing_to_find].get(0, None)
```

That being said, the last line is getting a bit long, though everything before the `.get(0, None)` is fine to have on one line.
But what does `.get()` do for a list?


It can take in 2 parameters, where the first is a index or a key (it depends if we are calling it from a `list` or a `dict`), and the second value is what gets returned if the index or key does not exist.
This is nice if you are not sure the index / key exists, as indexing using square brackets, i.e. 
- `values[0]` will throw a `IndexError` if the index `0` does not exist in the list `values`
- `values["a"]` will throw a `KeyError` if the key `"a"` does not exist in the dictionary `values`

### Counting values

Let's say we are doing something like counting the frequency of how often a value appears in a list.
Here, `elements` is a list, and we have a dictionary called `frequency` where the keys are values inside `elements` and their respective value in the dictionary is how often they appear in the list.

A common pattern I see is something like

```py
frequency = {}

for value in values:
    if value not in frequency:
        frequency[value] = 1
    else:
        frequency[value] += 1
```

That being said, it can also be done using `.get()` to automatically initialise the value to 0 if it does not exist.

```py
frequency = {}

for value in values:
    frequency[value] = frequency.get(value, 0) + 1
```

That being said there also is a `.count()` method which returns how often a value may appear in a list.
And using this, we can actually use 

```py
frequency = {value: values.count(value) for value in values}
```

**Not relevant to 1531 but I think it's cool:**

However, the code above runs in *O(n^2)*.
This is because `.count()` runs in *O(n)*, and we are looping over *n* values in our `for` loop.
To this I will admit, yes, that is not very nice - particularly because the fact that we are counting the frequencies of values implies that there must be repeats of values.
If there are $k$ unique values, we can improve the runtime from *O(n^2)* to *O(kn)* by doing

```py
frequency = {value: values.count(value) for value in set(values)}
```

Here, the `set()` converts the list into a `set` which is, just like in mathematics, a collection of unique values.
As a result, it no longer needs to count values it has already counted.

### Using sets over lists

Often times, you may use a list just because you use it all the time and you are comfortable with it.

However, a set is a bit similar to a list except for the following
1. Sets cannot contain duplicates (often can be a very useful property)
2. Sets are unordered - as a result they also cannot be indexed like an array to retrieve an item

Often a set may be useful for tracking a group of values, and is often be used like

```py
if value in some_set:
    do_something()
```

This aspect isn't particularly special to Python, and can be used in other languages.

Another benefit of sets is that it's easier to delete items.
For lists, we have to check if a value exists in it first, before we attempt to delete it otherwise a `ValueError` is thrown.

```py
if thing_to_remove is in a_list:
    a_list.remove(thing_to_remove)
```

Whilst in a set, we can just do

```
a_set.discard(thing_to_remove)
```

which will not throw a `ValueError` even if `thing_to_remove` is not in the list.

**Not relevant to 1531 but I think it's cool:**

Checking if something is in a set or deleting something from a set in Python runs in *O(1)* as compared to *O(n)* for a list.
This is because sets are implemented as a hash table, so finding it happens instantly, whilst we have to search linearly through a list.
Furthermore, removing an item from a list runs in *O(n)* as we have to shift all the items to ensure that everything is in the correct index after deletion.


