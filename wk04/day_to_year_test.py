from day_to_year import day_to_year

def test_day_to_year():
    assert day_to_year(1) == 1970 # "January 1st 1970"
    assert day_to_year(366) == 1971 # "January 1st 1971"
    assert day_to_year(365 + 365 + 1) == 1972 # "January 1st 1972"
    assert day_to_year(365 + 365 + 366 + 1) == 1973 # "January 1st 1973"

    # Edge case is when the days left is exactly 366
    assert day_to_year(365 + 365 + 366) == 1972 # December 31st 1972
