from isbn import is_valid

def ISBNValidator(function):
    def wrapper(isbn, *args, **kwargs):
        if is_valid(isbn):
            return function(isbn, *args, **kwargs)
        raise ValueError
    return wrapper

@ISBNValidator
def printBook(isbn, book):
    """
    Print out the book along with ISBN.
    """
    print(f'Printing book <{book}>\nISBN: {isbn}')

if __name__ == "__main__":
    # Get the ISBN
    isbn = input('What is the ISBN? ')

    # Call the functions that use ISBN
    try:
        printBook(isbn, 'Legend of Hayden')
    except ValueError:
        print(f'{isbn} is invalid.')
