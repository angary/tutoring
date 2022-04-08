"""
Examples of when we would use a decorator / wrap a function
"""

from time import time
from datetime import datetime
from functools import lru_cache

# Logging
# * = "unpacking operator"
# def log(f, *args, **kwargs):
#     print(f"Called {f.__name__} at {datetime.now()} with args: {args} and kwargs: {kwargs}")
#     return f(*args, **kwargs)

def log(f):
    def new_function(*args, **kwargs):
       print(f"Called {f.__name__} at {datetime.now()} with args: {args} and kwargs: {kwargs}")
       return f(*args, **kwargs)
    return new_function


# Timing
# def timeit(f, *args):
#     start = time()
#     result = f(args)
#     duration = time() - start
#     print(f"It took {duration} to run {f.__name__}")
#     return result

def timeit(f):
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        duration = time() - start
        print(f"It took {duration} to run {f.__name__}")
        return result
    return wrapper

@timeit
def f(x, y, z=10, a="a"):
    print(f"f was called with {x}, {y}, z={z}, a={a}")
    return x, y

# print(timeit(f)(10, 20, z=10, a="a"))
print(f(10, 20, z=10, a="a"))

# @lru_cache
# @log
# def fib(n):
#     if n in (0, 1):
#         return n
#     return fib(n - 1) + fib(n - 2)

# print(fib(int(input("Enter n: "))))
