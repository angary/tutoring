from typing import ValuesView
from divisors import divisors
from hypothesis import given, strategies
import pytest

def test_12():
    assert divisors(12) == {1,2,3,4,6,12}

# Property based testing
@given(strategies.integers(min_value=1, max_value=200))
def test_divisible(n):
    print(n)
    for d in divisors(n):
        assert n % d == 0


@given(strategies.integers(max_value=0))
def test_non_positive(n):
    with pytest.raises(ValueError):
        divisors(n)
