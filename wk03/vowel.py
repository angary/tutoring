import pytest

VOWELS = "aeiou"


def find_vowels(message):
    # result = {c: 0 for c in VOWELS}
    # for char in message:
    #     if char.isupper():
    #         raise ValueError
    #     if char in VOWELS:
    #         result[char] += 1
    # return result
    if any([c.isupper() for c in message]):
        raise ValueError
    return {c: message.count(c) for c in VOWELS}


def test_find_vowels_throws_value_error_on_uppercase():
    with pytest.raises(ValueError):
        find_vowels("Aa")


if __name__ == '__main__':
    message = input("Please enter in a message: ")
    try:
        vowels = find_vowels(message)
        for key, val in vowels.items():
            print(f"{key}: {val}")
    except ValueError:
        print("Error: has an uppercase character")

