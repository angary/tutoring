from isbn import is_valid

def ISBNValidator(function):
    pass

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
