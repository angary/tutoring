# General Iteration 1 Feedback

Some general feedback for iteration 1.
Missing things in the important section may result in loss of marks.
Alternatively, missing many things that are in the medium priority may result in loss of marks in iteration 2 as we check for pythonic code style.

## High Priority

### Code Style

- Use helper functions for commonly repeated code, i.e.

  ```py
  def find_user(auth_user_id):
      # Return user if id exists else return nothing or raise error
  ```

### Tests

- Use fixtures to clear data, and or also return data that needs to be reused
  ```py
  @pytest.fixture
  def data():
      return {
          "a": get_a(),
          "b": get_b()
      }
  
  def test_data(data):
      a = some_function(data["a"])
      assert another_function(a, data["b"]) == expected_value_for_b
  ```
- Make sure tests are named well and have a comment explaining what the test does and or checks
  - Try to be at least as clear as the tests used in course tests
- Aim to test one case in each test, however it is fine to have multiple asserts in a test if it's for the same case or to check that a dictionary has the correct values for the correct keys
  ```py
  # INSTEAD OF
  def test_fail_cases():
      with pytest.raises(ErrorA):
          func(invalid_input_a)
      with pytest.raises(ErrorB):
          func(invalid_input_b)
      assert func(valid_input) == expected_value
  
  # DO THIS
  def test_input_a_raises_error_a():
      with pytest.raises(ErrorA):
          func(invalid_input_a)

  def test_input_b_raises_error_b():
      with pytest.raises(ErrorB):
          func(invalid_input_b)
  
  def test_valid_input_returns_correct_value():
      assert func(valid_input) == expected_value
  ```
  - This is because:
    - If the first assert fails in a test, then the rest of the asserts do not get tested so you don't know if they work or not
    - By separating out the tests, you can have more meaningful test names for each test


## Medium Priority

### Code Quality

- For finding checking if something exists, rather than a single use boolean flag, you can use Python's `for ... else` loops or the `in` keyword

  ```py
  # INSTEAD OF THIS
  found = False
  for val in vals:
      if val == "thing_to_find":
          found = True
          print("found")
          break
  if not found:
      print("not found")
  
  # DO THIS
  for val in vals:
      if val == "thing_to_find":
          print("found")
          break
  else:
      print("not found")

  # OR THIS
  if "thing_to_find" in vals:
      print("found")
  else:
      print("not found")
  ```
- Avoid boolean literals (i.e. `True` and `False`) in conditional statements
  ```py
  # INSTEAD OF
  if a == True and b is True and c != False:
      pass
  
  # DO THIS
  if a and b and not c:
      pass
  ```
- Use list comprehensions
  ```py
  # INSTEAD OF
  results = []
  for val in vals:
      if some_condition(val):
          results.append(val)
  
  # DO THIS
  results = [val for val in vals if some_condition(val)]
  ```

### Tests

- Use Python string multiplication for generating long strings as it is easier to tell how long the string is
  ```py
  # INSTEAD OF
  def test_x_return_50_xs():
      assert x == "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
  
  # DO THIS
  def test_x_return_50_xs():
      assert x == "x" * 50
  ```


## Low Priority

### Code style

- Make sure the doc string is inside the function, as this is how python and text editors (i.e. vscode) recognise that it is a docstring
  ```py
  # INSTEAD OF
  """
  Some docstring
  """
  def func():
      return
  
  # DO THIS
  def func():
      """
      Some docstring
      """
      return
  ```
- Bit of a personal preference here, but sticking to a consistent indentation level instead of indenting till the end of something like a variable name can make things easier / more readable
  ```py
  # INSTEAD OF THIS
  assert some_long_test_case_name_or_condition() == {
                                                        "a": 1
                                                        "b": 2
                                                    }
  # DO THIS
  assert some_long_test_case_name_or_condition() == {
      "a": 1,
      "b": 2
  }
  ```
- There is no need to put code after a `return` or a `raise` after another conditional statement
  ```py
  # INSTEAD OF
  if some_condition():
      raise Error("some message")
  else:
      return value
  
  # DO THIS
  if some_condition():
      raise Error("some message")
  return value
  ```

### Tests

- Adding `autouse=True` as a kwag to `@pytest.fixture` means that the fixture will run every test.
  This can be useful, as sometimes you may forget to add that fixture, even though it should be called for every test

  ```py
  @pytest.fixture(autouse=True)
  def some_fixture():
      # Do something
  ```
