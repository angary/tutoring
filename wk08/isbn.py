def is_valid(isbn):
    # Get the sum of the first 9 digits multiplied by their position
    sum_of_first_nine = sum([int(x) * (i + 1) for i, x in enumerate(isbn[:9])])

    # Get the remainder when this is divided by 11
    remainder = sum_of_first_nine % 11

    # Calculate the validity
    if (remainder == 10):
        return isbn[-1] == 'X'
    else:
        return int(isbn[-1]) == remainder

if __name__ == "__main__":
    # Get the ISBN
    isbn = input('What is the ISBN? ')
    # Show the result
    valid = 'valid' if is_valid(isbn) else 'invalid'
    print(f'{isbn} is {valid}.')
