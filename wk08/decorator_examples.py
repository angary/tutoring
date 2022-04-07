"""
Examples of when we would use a decorator
"""

from time import time
from datetime import datetime


# Logging
def log(f, arg):
    print(f"Called {f.__name__} at {datetime.now()}")
    return f(arg)

# Timing
def timeit(f, arg):
    start = time()
    result = f(arg)
    duration = time() - start
    print(f"It took {duration} to run {f.__name__}")
    return result

def f(n):
    print(f"f was called with {n}")
    return n

