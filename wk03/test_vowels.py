from vowels import find_vowels
import pytest

def test_find_vowels_simple():
    assert find_vowels("aeiou bcd") == {
        "a": 1,
        "e": 1,
        "i": 1,
        "o": 1,
        "u": 1,
    }

def test_find_vowels_upper():
    with pytest.raises(ValueError):
        find_vowels("AEIOU")
