"""
What is the name? World Health Organisation
It's acronym is WHO.
"""

def acro(string: str) -> str:
    return "".join(word[0].upper() for word in string.split(" "))


if __name__ == '__main__':
    name = input("What is the name? ")
    print(f"It's acronym is {acro(name)}.")
