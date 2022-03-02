def wondrous(start):
    '''
    Returns the wondrous sequence for a given number.
    '''
    current = start
    sequence = []

    while current != 1:
        sequence.append(current)
        if (current % 2 == 0):
            current /= 2
        else:
            current = (current * 3) + 1

    return sequence
