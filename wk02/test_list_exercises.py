from list_exercises import reverse_list, minimum, sum_list
import pytest

"""
* What is a pytest fixture?
- A pytest fixture is a way of setting up data / inputs that can be passed into 
- our tests

* How can we use fixtures to improve our tests?
- We can use fixtures to remove the need for rewriting out input / data multiple
  times

* As a class, change `test_list_exercises.py` to use a fixture.
"""

@pytest.fixture
def l():
    return [1, 2, 3, 4, 5]

def test_reverse(l):
    reverse_list(l)
    assert(l == [5, 4, 3, 2, 1])


def test_min_positive_numbers(l):
    assert(minimum(l) == 1)


def test_sum_positive_numbers(l):
    assert(minimum(l) == 15)
