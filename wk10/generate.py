from typing import Iterator

def generate(n: int) -> Iterator[int]:
    """
    Generates the first n fibonacci numbers
    """
    a, b, counter = 0, 1, 0
    while counter < n:
        yield a
        a, b = b, a + b
        counter += 1


def my_range(n: int) -> Iterator[int]:
    """
    Implementation of the range function
    """
    i = 0
    while i < n:
        yield i
        i += 1
    return

if __name__ == "__main__":
    for x in generate(10):
        print(x)
