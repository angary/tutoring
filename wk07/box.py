SIZE = 20

def is_at_border(x):
    return x in (0, SIZE - 1)

for i in range(SIZE):
    for j in range(SIZE):
        if is_at_border(i) or is_at_border(j):
            print('*', end="")
        else:
            print(' ', end="")
    print()
