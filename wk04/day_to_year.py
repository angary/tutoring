"""
A file to convert from days since 1970 to year
"""
from calendar import isleap

ORIGIN_YEAR = 1970

def day_to_year(days):
    """
    A function to convert from days since 1970 to year
    """
    year = ORIGIN_YEAR

    while days > 365:
        if isleap(year):
            if days > 366:
                days -= 366
                year += 1
            else: # days is 366
                days = 0 # Set days to 0, break does not get covered in coverage
        else:
            days -= 365
            year += 1

    return year
