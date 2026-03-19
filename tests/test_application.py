"""
Python Flask Calculator Web Application unit tests
"""

# Imports
import math
import random
from application import application


def test_addition_1():
    """
    Make a POST request to the /calculate endpoint to perform
    the addition operation

    This unit test will run with manually provided test
    values
    """
    # Test variables
    number_1 = -26
    number_2 = 103

    # Make HTTP response
    response = application.test_client().post("/calculate", data={
        "operation": "addition",
        "number_1": number_1,
        "number_2": number_2
    })

    # Run assertions
    matching_string = "Result: 77"
    assert response.status_code == 200
    assert matching_string.encode() in response.data


def test_addition_2():
    """
    Make a POST request to the /calculate endpoint to perform
    the addition operation

    This unit test will run with randomly generated test
    values
    """
    # Test variables
    number_1 = random.randint(1, 1000)
    number_2 = random.randint(1, 1000)

    # Make HTTP response
    response = application.test_client().post("/calculate", data={
        "operation": "addition",
        "number_1": number_1,
        "number_2": number_2
    })

    # Run assertions
    addition_answer = number_1 + number_2
    matching_string = f"Result: {addition_answer}"
    assert response.status_code == 200
    assert matching_string.encode() in response.data


def test_default_route():
    """
    Make a GET request to "/" and return a status code of 200
    """
    # Make HTTP response
    response = application.test_client().get("/")

    # Run assertions
    assert response.status_code == 200


def test_get_calculate_redirect():
    """
    Make a GET request to "/calculate" and return a
    status code of 200
    """
    # Make HTTP response
    response = application.test_client().get("/calculate")

    # Run assertions
    assert response.status_code == 200
    assert response.status_code != 405

def test_celsius_to_kelvin_1():
    """
    Make a POST request to the /calculate endpoint to perform
    the celsius to kelvin conversion

    This unit test will run with randomly generated test
    values
    """
    # Test variables
    number_1 = random.randint(1, 1000)

    # Make HTTP response
    response = application.test_client().post("/calculate", data={
        "operation": "celsius_to_kelvin",
        "number_1": number_1
    })

    # Run assertions
    kelvin_answer = number_1 + 273.15
    matching_string = f"Result: {kelvin_answer}"
    assert response.status_code == 200
    assert matching_string.encode() in response.data

def test_celsius_to_kelvin_2():
    """
    Make a POST request to the /calculate endpoint to perform
    the celsius to kelvin conversion

    This unit test will run with manually provided test
    values
    """
    # Test variables
    number_1 = -100

    # Make HTTP response
    response = application.test_client().post("/calculate", data={
        "operation": "celsius_to_kelvin",
        "number_1": number_1
    })

    # Run assertions
    matching_string = f"Result: {float(number_1) + 273.15}"
    assert response.status_code == 200
    assert matching_string.encode() in response.data

