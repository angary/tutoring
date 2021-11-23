import datetime
from typing import List, Dict

names_ages: List[Dict] = []

def date_to_age(timestamp: int) -> int:
    dt = datetime.datetime.fromtimestamp(timestamp)
    now = datetime.datetime.now()
    diff = now - dt
    return diff.days // 365

def get_names_ages(min_age: int) -> List[Dict]:
    if min_age is None:
        return names_ages
    return list(filter(lambda record: record['age'] >= int(min_age), names_ages))

def add_name_age(name: str, dob: int) -> None:
    names_ages.append({
        'name': name,
        'age': date_to_age(dob)
    })

def edit_name_age(name: str, dob: int) -> None:
    for name_age in names_ages:
        if name_age['name'] == name:
            name_age['age'] = date_to_age(dob)
            return

def clear_names_ages() -> None:
    names_ages.clear()

if __name__ == "__main__":
    add_name_age("bob", 0)
    print(names_ages)
