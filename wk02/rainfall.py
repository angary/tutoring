import pytest

'''
Compute the average of only the positive elements in the list.
'''
def rainfall(integers):
    '''
    Single-loop solution
    '''
    total = 0
    count = 0
    for i in integers:
        if  i > 0:
            total += i
            count += 1
    if (count > 0):
        return total/count
    else:
        return 0

def rainfall_alternative(integers):
    # To calculate average, we want to take the sum of positive numbers and 
    # divide by the number of positive numbers
    result = [i for i in integers if i > 0]
    if len(result) == 0:
        return 0
    else:
        return sum(result) / len(result)


@pytest.fixture
def test_data_set():
    return [1, 2, 3]

# Write tests here
def test_simple_all_positive(test_data_set):
    print(test_data_set)
    assert rainfall(test_data_set) == 1

def test_simple_all_positive_alternative(test_data_set):
    assert rainfall_alternative(test_data_set) == 2

def test_empty_list():
    assert rainfall([]) == 0

def test_all_negative():
    assert rainfall([-1, -2, -3]) == 0

def test_positive_and_negative():
    assert rainfall([-1, -2, -3, 1, 2, 3]) == 2

def test_zero():
    assert rainfall([1, 2, 3, 0]) == 1
