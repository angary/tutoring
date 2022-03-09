from calendar import isleap

ORIGIN_YEAR = 1970

def day_to_year(days):
    year = ORIGIN_YEAR

    while days > 365:
        if isleap(year):
            if days > 366:
                days -= 366
                year += 1
        else:
            days -= 365
            year += 1

    return year
