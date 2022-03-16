# Tutorial 5

## A. A Simple Server

### Part 1 - The Backend

In `names_ages.py`, write a simple program which:

- Stores a list of dictionaries containing names and ages.
- Has a function `add_name_age` that takes in a name and a date of birth, and adds the dictionary {name, age} to the data store
- Has a function `get_names_ages` that returns the list of name-ages.
- Has a function `clear_names_ages` that clears the list of name-ages.
- Uses a helper function `date_to_age` which converts the date to an age

### Part 2 - Server Stubs

Write a simple Flask server that contains corresponding routes for adding names/ages and getting names/ages in `server.py`. The routes should simply be stubs for now.

### Part 3 - Failing HTTP Tests

Write a HTTP test for each of your routes inside `names_ages_test.py`. You will need to check:

- The response status code;
- The contents of the return value;

in each of your tests. The tests should fail when you run them.

Once you have done this, complete the implementations of the Flask route wrapper functions. The tests should pass.

- Discuss briefly why clearing the data store using the `.clear()` method works, when simply setting it to `= []` doesn't.

## B. Code Review

1. Your tutor will break up into groups for this activity. Take a look at [this webpage](https://www.youtube.com/watch?v=GfL5zOhpB14). What routes do you think are necessary to allow this webpage to function? For each route:

- Discuss the data it might take in
- Discuss the data it might return

[h11b doc](https://docs.google.com/document/d/1aBZe_8lMALVVZdTISQTswMuR-ozE6pQGIoMn5R0yptM/edit?usp=sharing)

2. Are there any considerations that need to be made when choosing how to breakup routes?

## C. Networks

Breakdown the key components of an HTTP URL, such as http://unsw.com/calendar/view?term=t3&week=5#top

| Value           | Name |
| --------------- | ---- |
| http            |      |
| unsw.com        |      |
| calendar/view   |      |
| ?term=t3&week=5 |      |
| #top            |      |

## D. More Flask

This exercise continues on from Exercise A.

1. Add a new route, `edit_name_age` that, given a name and a new date of birth, updates corresponding record. Develop this HTTP test-first by stubbing out the backend function and Flask route, writing the failing test and then implementing to pass the test.

2. Change the `get_names_ages` route and backend method to optionally accept a minimum age, and only returns people who are older than that age. Use the `filter` function in your backend solution.

## E. JSON & YAML

- Convert the JSON file [data_1.json](data_1.json) to YAML in [data_1.yml](data_1.yml)
- Convert the YAML file [data_2.yml](data_2.yml) to JSON in [data_2.json](data_2.json)
