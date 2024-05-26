"""
Python Flask Calculator Web Application unit tests
"""

# Imports
import math
import random
from application import application


def test_default_route():
    """
    Make a GET request to "/" and return a status code of 200
    """
    # Make HTTP response
    response = application.test_client().get("/")

    # Run assertions
    assert response.status_code == 200

def test_custom_log_base_1():
    """
    Make a POST request to the /calculate endpoint to perform
    the custom_log_base operation

    This unit test will run with manually provided test
    values
    """
    # Test variables
    number_1 = 256
    number_2 = 4

    # Make HTTP response
    response = application.test_client().post("/calculate", data = {
        "operation": "custom_log_base",
        "number_1": number_1,
        "number_2": number_2
    })

    # Run assertions
    matching_string = "Result: 4.0"
    assert response.status_code == 200
    assert matching_string.encode() in response.data

def test_custom_log_base_2():
    """
    Make a POST request to the /calculate endpoint to perform
    the custom_log_base operation

    This unit test will run with randomly generated test
    values
    """
    # Test variables
    number_1 = random.randint(1, 1000)
    number_2 = random.randint(1, 1000)

    # Make HTTP response
    response = application.test_client().post("/calculate", data = {
        "operation": "custom_log_base",
        "number_1": number_1,
        "number_2": number_2
    })

    # Run assertions
    custom_log_base_answer = float(math.log(number_1, number_2))
    matching_string = f"Result: {custom_log_base_answer}"
    assert response.status_code == 200
    assert matching_string.encode() in response.data

def test_celsius_to_fahrenheit():
    """
    Make a POST request to the /calculate endpoint to perform
    the celsius_to_fahrenheit operation

    This unit test will run with manually provided test
    values
    """
    # Test variables
    number_1 = 36

    # Make HTTP response
    response = application.test_client().post("/calculate", data = {
        "operation": "celsius_to_fahrenheit",
        "number_1": number_1
    })

    # Run assertions
    matching_string = "Result: 96.8"
    assert response.status_code == 200
    assert matching_string.encode() in response.data

def test_factorial():
    """
    Make a POST request to the /calculate endpoint to perform
    the factorial operation

    This unit test will run with randomly generated test
    values
    """
    # Test variables
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)

    # Make HTTP response
    response = application.test_client().post("/calculate", data = {
        "operation": "factorial",
        "number_1": number_1,
        "number_2": number_2
    })

    # Run assertions
    factorial_answer = math.factorial(int(number_1))
    matching_string = f"Result: {factorial_answer}"
    assert response.status_code == 200
    assert matching_string.encode() in response.data

def test_subtraction_1():
    """
    Make a POST request to the /calculate endpoint to perform
    the subtraction operation

    This unit test will run with manually provided test
    values
    """
    # Test variables
    number_1 = 57
    number_2 = 8

    # Make HTTP response
    response = application.test_client().post("/calculate", data = {
        "operation": "subtraction",
        "number_1": number_1,
        "number_2": number_2
    })

    # Run assertions
    matching_string = "Result: 49.0"
    assert response.status_code == 200
    assert matching_string.encode() in response.data

def test_subtraction_2():
    """
    Make a POST request to the /calculate endpoint to perform
    the subtraction operation

    This unit test will run with randomly generated test
    values
    """
    # Test variables
    number_1 = random.randint(1, 1000)
    number_2 = random.randint(1, 1000)

    # Make HTTP response
    response = application.test_client().post("/calculate", data = {
        "operation": "subtraction",
        "number_1": number_1,
        "number_2": number_2
    })

    # Run assertions
    subtraction_answer = number_1 - number_2
    matching_string = f"Result: {subtraction_answer}"
    assert response.status_code == 200
    assert matching_string.encode() in response.data
