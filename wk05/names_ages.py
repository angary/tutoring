import datetime

data = []

def date_to_age(dob):
    dob_datetime = datetime.datetime.fromtimestamp(dob)
    now_datetime = datetime.datetime.now()
    diff = now_datetime - dob_datetime
    return diff.days // 365


def add_name_age(name, dob):
    data.append({
        "name": name,
        "age": date_to_age(dob)
    })


def edit_name_age(name, dob):
    for name_age in data:
        if name_age["name"] == name:
            name_age["age"] = date_to_age(dob)
            return


def get_names_ages(min_age):
    """
    Note that all three ways of filtering the list work / accomplish the same
    thing of returning a new filtered list
    """
    # return [name_age for name_age in data if name_age["age"] > min_age]
    # return list(filter(lambda x: x > min_age, data))
    def filter_age(name_age):
        return name_age["age"] > min_age
    return list(filter(filter_age, data))


def clear_names_ages():
    data.clear()

