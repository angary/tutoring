"""
Write a function that yields all of the fibonacci numbers up to n
using a generator

What is a generator?
>>> Function that acts as an iterator

What does the `yield` keyword do?
>>> It "pauses" the code, and then returns the "next" value 

How can we use the values returned by generators?
>>> 

"""
from typing import Iterator


def generate(n: int) -> Iterator:
    # Yield all of the fib nums up to n
    a, b = 0, 1
    counter = 0
    while True:
        if counter >= n:
            break
        yield a
        a, b = b, a + b
        counter += 1
    return


if __name__ == "__main__":
    n = int(input("Enter in value: "))
    for i in generate(n):
        print(i)
