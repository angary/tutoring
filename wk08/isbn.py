"""
* Multiply each of the first 9 digits by its position. The positions go from 1 to 9.
* Add up the 9 resulting products.
* Divide this sum by 11, and get the remainder, which is a number between 0 and 10.
* If the remainder is 10, the last character should be the letter 'X'. Otherwise, the last character should be the remainder (a single digit).

"""

def is_valid(isbn):
    """
    Determines whether the ISBN is valid or not
    """
    result = 0
    for i, val in enumerate(isbn[:9]):
        result += (i + 1) * int(val)
    remainder = result % 11

    if remainder == 10:
        return isbn[-1] == "X"
    return int(isbn[-1]) == remainder


"""
```txt
What is the ISBN? 1503290565
1503290565 is valid
```

```txt
What is the ISBN? 938007834X
938007834X is valid
```

```txt
What is the ISBN? 2222222224
2222222224 is invalid
```
"""

if __name__ == "__main__":
    # Get the ISBN
    isbn = input('What is the ISBN? ')
    # Show the result
    valid = 'valid' if is_valid(isbn) else 'invalid'
    print(f'{isbn} is {valid}.')
