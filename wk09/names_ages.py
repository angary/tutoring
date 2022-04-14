import datetime
import time
from typing import List, Dict

data: List[Dict] = []


def date_to_age(dob: float) -> int:
    dob_datetime = datetime.datetime.fromtimestamp(dob)
    now_datetime = datetime.datetime.now()
    diff = now_datetime - dob_datetime
    return diff.days // 365


def add_name_age(name: str, dob: float) -> None:
    data.append({
        "name": name,
        "age": date_to_age(dob)
    })


def edit_name_age(name: str, dob: int) -> None:
    for name_age in data:
        if name_age["name"] == name:
            name_age["age"] = date_to_age(dob)
            return


def get_names_ages() -> List[Dict]:
    return data


def clear_names_ages() -> None:
    data.clear()


if __name__ == "__main__":
    # Take in string input
    name = input("Please enter your name: ")
    dob_str = input("Please enter your date of birth in dd/mm/yyyy: ")

    # Convert date of birth string to date time object
    dob_dt = datetime.datetime.strptime(dob_str, "%d/%m/%Y")

    # Convert from date time object into a unix timestamp
    dob = time.mktime(dob_dt.timetuple())

    # Add the name
    add_name_age(name, dob)

    # Get the list of names and ages
    print(get_names_ages())
