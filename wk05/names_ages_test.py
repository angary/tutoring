import pytest
import requests

@pytest.fixture(autouse=True)
def setup():
    requests.delete("http://127.0.0.1:8080/clear")


def test_add_name_age():
    response = requests.post("http://127.0.0.1:8080/addnameage", json={
        "name": "gary sun",
        "dob": 0
    })
    assert response.status_code == 200
    assert response.json() == {}


def test_get_names_ages():
    requests.post("http://127.0.0.1:8080/addnameage", json={
        "name": "gary sun",
        "dob": 0
    })
    response = requests.get("http://127.0.0.1:8080/getnamesages")
    assert response.status_code == 200
    assert response.json() == [
        {
            "name": "gary sun",
            "age": 52
        }
    ]


def test_get_names_ages_with_filter():
    requests.post("http://127.0.0.1:8080/addnameage", json={
        "name": "gary sun",
        "dob": 0
    })
    response = requests.get("http://127.0.0.1:8080/getnamesages", params={
        "min_age": 100
    })
    assert response.status_code == 200
    assert response.json() == []

