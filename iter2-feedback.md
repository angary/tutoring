# General Iteration 2 Feedback

Some general feedback for iteration 2.
Overall there was lots of improvement from iteration 1, from implementing the feedback.
However, if you have yet to implement feedback (i.e. not using helper functions / fixtures) from iteration 1 please do so.

A lot of the issues with the code was from not implementing feedback from iteration 1 (so do take a look at [iter1-feedback.md](iter1-feedback.md)!). 
However, here are some thoughts on system design / technical skills that separates software engineering from copy and pasting code off the internet.

## Design

### Server

Make sure that all that is in `server.py` is purely for interfacing, i.e. the only code in `server.py` routes is there for extracting out params / args from the request, and then passing those values into the backend functions.

```py
@app.route(...)
def some_route():
    # DO: Extract out params / args
    # DO NOT: Have business logic here
    # DO: Return jsonified output of the backend function with params / args passed in
```

Examples of what **NOT** to include in server.py

- Checking for the validity of the token
- Saving of data for persistence

The reason for this is to have a clear separation of logic, rather than having implementation logic split across the codebase.
As a result, it would be better to modify backend functions to take in `token`, instead of `auth_user_id`.
There is a very clean way to handle the validation of tokens using Python decorators.

### Persistence

When it comes to implementing persistance, it was common to see a pattern like this:

```py
"""
In a some file, functions were defined to save and load the data
"""
def save_data():
    # Write data to a file

def load_data():
    # Read data from file

...

"""
Then in server.py, save_data() was called after calling the backend function.
"""
@app.route(...)
def some_route():
    # Extract args and call backend function
    save_data()
```

This is **NOT** good design for the following reasons:

- `server.py` should only handle interfacing between the routes and the backend functions.
  Handling storage of data should be handled in the backend.
  This results in highly coupled code, i.e. a modification in a backend function may or may not require modifying the code in `server.py` again.
- This splits the backend logic across `server.py` and the backend file, making it harder to determine where a behaviour is coming from.
- This also results in many repeated lines of code to `server.py`.

Ideally you would've already called a function like `data_store.set(store)` in the backend every time the data store was modified.

As a result, a good design would have looked something like 
```py
"""
Inside data_store.py
"""
class Datastore:
    def __init__(self):
        # Read the file and set self.__store to be what's read from the file if it exists
        self.__store = initial_object

    def get(self):
        # Can also read the file in this function
        return self.__store

    def set(self, store):
        # Write to the file as well
        if not isinstance(store, dict):
            raise TypeError('store must be of type dictionary')
        self.__store = store

print('Loading Datastore...')

global data_store
data_store = Datastore()
```

This is a better design for the following reasons:

- Since every time the datastore is modified, `data_store.set(store)` is already called, by modifying this function, it is guaranteed that every time the backend wants to save, the changes are saved (reduces coupling compared to previous design, where two separate functions had to be called in different places).
- By modifying this only, no lines of code need to be modified in other files (follows the DRY rule).
- It keeps the storage related code inside `data_store.py` which is good abstraction and allows each module to focus on their own purpose (i.e. if we were to implement a database, it would require more rewriting of code).


As for whether to read the file in the `__init__` method vs `get` method, I recommend `__init__` for the following reason:
- At the bottom of the file there is the line `data_store = Datastore()`, which triggers the `__init__` method. 
  Since this line of code is read once, `__init__` is only called once at the beginning, whereas if we read the file in `get` we need to read it every time `get` is called which is more inefficient.
  It would be better to just store a copy of the data in a local variable and update that along with the storage file in the `set` method.

### Testing

It is common practice to have something like a testing utils file (i.e. `test_utils.py`) if you need helper functions.

For pytest fixtures specifically, it is normal to make a new file called `conftest.py` where you can store your fixtures.
These fixtures can then be used in other files without the need to import it.
For more information check the [docs](https://docs.pytest.org/en/6.2.x/fixture.html#conftest-py-sharing-fixtures-across-multiple-files).

If you find yourself doing something at the top of each file like
```py
import pytest

SUCCESS = 200
ACCESS_ERROR = 403
INPUT_ERROR = 400

def some_test():
    ...
    assert response.status_code == SUCCESS # etc

def another_test():
    ...
    assert response.status_code == ACCESS_ERROR # etc
```

It would be better to do
```py
from http import HTTPStatus # (Optional, only if you want to use HTTPStatus.OK)
from src.error import AccessError, InputError

def some_test():
    ...
    # Since 200 is a standard code for success there is no need to abstract it
    assert response.status_code == 200 
    # If you want, you can also do something like
    assert response.status_code == HTTPStatus.OK

def another_test():
    ...
    # This is the best way to handle things, as when an AccessError is raised,
    # flask looks for AccessError.code and returns that
    assert response.status_code == AccessError.code
```

Note that using `AccessError.code` would be the best way of checking for the correct status code as if you were to modify the status code for an access error, it wouldn't require rewriting all the tests.
This is because when an `AccessError` is raised, flask checks for `AccessError.code` to determine what HTTP status code to return according to the [docs](https://flask.palletsprojects.com/en/2.1.x/errorhandling/#registering) (note this also applies for `InputError`).