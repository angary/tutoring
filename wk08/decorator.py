from isbn import isValid
from socket import socket, AF_INET, SOCK_STREAM
import requests

def ISBNValidator(function):
    """
    TODO: Complete this wrapper
    """
    pass


@ISBNValidator
def sendToPublisher(isbn):
    """
    Pretend to send ISBN to the publisher via the Internet (through a network request) by sending it to localhost:8000 which is where http server is run on.
    Don't worry about any of the socket code, this is just to show you something cool you can do with Python.
    Please put your focus on the use of decorator here.
    """
    # Send a GET request to the localhost
    requests.get(f'http://127.0.0.1:8000?isbn={isbn}')
    print('Sent ISBN to the publisher!')


@ISBNValidator
def printBook(isbn):
    """
    Print out the book along with ISBN.
    """
    BOOK_NAME = 'Legend of Hayden'
    print(f'Printing book <{BOOK_NAME}>\nISBN: {isbn}')


if __name__ == "__main__":
    # Get the ISBN
    isbn = input('What is the ISBN? ')

    # Call the functions that uses ISBN
    try:
        sendToPublisher(isbn)
        printBook(isbn)
    except ValueError:
        print(f'{isbn} is invalid.')
