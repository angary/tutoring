import sys
"""
sys.stdout.write() is like print() but without a newline at the end
"""

# DRY: Don't repeat yourself
def is_border(row, col):
    return row in (0, SIZE - 1) or col in (0, SIZE - 1)

SIZE = 20
for i in range(SIZE):
    for j in range(SIZE):
        if is_border(i, j):
            print("*", end="")
        else:
            print(" ", end="")
    print()
