"""acronym

A sample exam question

Write a program in `acronym.py` that asks the user for a multi-word name and
then passes it to a function `acro()` that returns the corresponding acronym,
which is then printed to the user.

Example usage:

```
What is the name? World Health Organisation
Its acronym is WHO.
```
"""

def acro(words: str) -> str:
    return "".join([x[0] for x in words.split()]).upper()


if __name__ == "__main__":
    words = input("What is the name? ")
    print(f"Its acronym is {acro(words)}")

