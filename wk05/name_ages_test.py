import requests
import pytest

URL = "http://localhost:8080"
OK = 200

# Clear fixture
@pytest.fixture
def clear_data():
    requests.delete(f"{URL}/clear")


def test_add_name(clear_data):
    """
    Test that adding a name returns correct status code and json
    """
    # Test that clear data works
    response = requests.get(f"{URL}/getnamesages")
    assert response.status_code == OK
    assert response.json() == []


    # Test that adding a name returns correct status code and json
    response = requests.post(f"{URL}/addnameage", json={
        "name": "Bob",
        "dob": 1602609815
    })
    assert response.status_code == OK
    assert response.json() == {}


def test_get_names(clear_data):
    """
    Test that after adding a new name, the route /getnamesages will return
    a list including the new name
    """
    # Assert that nothing is returned initially
    # Test that clear data works
    response = requests.get(f"{URL}/getnamesages")
    assert response.status_code == OK
    assert response.json() == []

    # Add names
    response = requests.post(f"{URL}/addnameage", json={
        "name": "Bob",
        "dob": 1602609815
    })
    assert response.status_code == OK
    assert response.json() == {}

    # Assert that what we added is now returned
    response = requests.get(f"{URL}/getnamesages")
    assert response.status_code == OK
    assert response.json() == [{
        "name": "Bob",
        "age": 1
    }]


def test_get_names_restrict(clear_data):
    """
    Test that having a min_age parameter of 40 will only return members that are
    older than 40
    """
    requests.post(f'{URL}/addnameage', json={
        'name': 'Rob', 'dob': 160260981,
    })
    requests.post(f'{URL}/addnameage', json={
        'name': 'Hayden', 'dob': 1602609815,
    })

    response = requests.get(f'{URL}/getnamesages', params={'min_age': 40})
    assert response.status_code == OK
    assert response.json() == [{
        'name': 'Rob',
        'age': 46
    }]


def test_edit_names_ages(clear_data):
    """
    Test that editing the dob of a member works
    """
    requests.post(f'{URL}/addnameage', json={
        'name': 'Rob',
        'dob': 1000
    })

    response = requests.put(f'{URL}/editnameage', json={
        'name': 'Rob',
        'dob': 10 ** 8
    })

    response = requests.get(f'{URL}/getnamesages')
    assert response.status_code == OK
    assert response.json() == [{
        'name': 'Rob',
        'age': 51
    }]
