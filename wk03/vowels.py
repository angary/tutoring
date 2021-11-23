
def find_vowels(message):

    result = {}
    for c in message:
        if c.isupper():
            raise ValueError(f"An upper case character {c} was found")
        if c in "aeiou":
            result[c] = result.get(c, 0) + 1
    return result


"""
1. What is __name__?
Name is a variable that will be either the name of the file or __main__ if it
is the file being run

2. What happens if we don't have `if __name__ == "__main__"`?
When we import this file into another file, the code at the bottom will not run
"""

if __name__ == '__main__':
    message = input()
    try:
        result = find_vowels(message)
    except ValueError as e:
        print(f"There was an error: {e}")

