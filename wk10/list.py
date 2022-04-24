"""
Example of how a for loop works behind the scenes
"""

class CustomList():
    def __init__(self, l=[]):
        self.l = l
        self.i = -1

    def __iter__(self):
        self.i = -1
        return self

    def __next__(self):
        self.i += 1
        if self.i >= len(self.l):
            raise StopIteration
        return self.l[self.i]


if __name__ == "__main__":
    custom_list = CustomList([1, 2, 3])

    # Pythonic syntax
    for x in custom_list:
        print(x)
    
    # Behind the scenes
    custom_list_iterator = iter(custom_list)
    while True:
        try:
            result = next(custom_list_iterator)
            print(result)
        except StopIteration:
            break
