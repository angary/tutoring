import sys

i = 0
while i < 10:
    j = 0
    while j < 10:
        if i == 0 or i == 9 or j == 0 or j == 9:
            sys.stdout.write('*')
        else:
            sys.stdout.write(' ')
        j = j + 1
    sys.stdout.write("\n")
    i = i + 1
