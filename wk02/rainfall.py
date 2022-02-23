
'''
Compute the average of only the positive elements in the list.
'''


def rainfall(integers):
    positives = [x for x in integers if x > 0]
    if positives == []:
        return 0
    return sum(positives) / len(positives)


# Write tests here
def test_empty_list():
    assert(rainfall([]) == 0)


def test_with_zeroes():
    assert(rainfall([0, 0, 3]) == 3)


def test_with_all_negative():
    assert(rainfall([-1, -2, -3]) == 0)


def test_all_positive():
    assert(rainfall([1, 2, 3]) == 2)
