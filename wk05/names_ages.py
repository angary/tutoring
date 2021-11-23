from datetime import datetime
from dateutil.relativedelta import relativedelta

# Store a list of dictionary of name and ages
names_ages = []


def date_to_age(dob):
    """
    Convert the date of birth to an age
    """
    dob_date = datetime.fromtimestamp(dob)
    curr_date = datetime.now()
    difference = relativedelta(curr_date, dob_date)
    return difference.years


def add_name_age(name, dob):
    """
    Add the dictionary {name, age} to the data store
    """
    names_ages.append({
        "name": name,
        "age": date_to_age(dob)
    })


def get_names_ages(min_age):
    """
    Returns the list of name ages
    """
    if min_age is None:
        return names_ages
    # return [person for person in names_ages if person["age"] > min_age]
    return list(filter(lambda record: record["age"] >= int(min_age), names_ages))


def clear_names_ages():
    """
    Clears the list of name-ages
    """
    names_ages.clear()


def edit_name_age(name, dob):
    """
    Given a name and a new dob, updates the corresponding record
    """
    new_age = date_to_age(dob)
    for name_age in names_ages:
        if name_age["name"] == name:
            name_age["age"] = new_age


"""
Datetime objects cannot be passed over the internet via json. To send details 
such as time, we can use something known as the unix timestamp

The unix timestamp is an integer that tracks the total number of seconds past
1st Jan 1970

More details:
https://www.unixtimestamp.com/
"""
