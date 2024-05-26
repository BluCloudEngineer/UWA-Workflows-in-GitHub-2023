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


def test_celsius_to_fahrenheit_1():
    """
    Make a POST request to the /calculate endpoint to perform
    the celsius_to_fahrenheit operation

    This unit test will run with manually provided test
    values
    """
    # Test variables
    number_1 = 36
    number_2 = 88

    # Make HTTP response
    response = application.test_client().post("/calculate", data={
        "operation": "celsius_to_fahrenheit",
        "number_1": number_1,
        "number_2": number_2
    })

    # Run assertions
    matching_string = "Result: 96.8 °F"
    assert response.status_code == 200
    assert matching_string.encode() in response.data


def test_celsius_to_fahrenheit_2():
    """
    Make a POST request to the /calculate endpoint to perform
    the celsius_to_fahrenheit operation

    This unit test will run with randomly generated test
    values
    """
    # Test variables
    number_1 = random.randint(1, 1000)
    number_2 = random.randint(1, 1000)

    # Make HTTP response
    response = application.test_client().post("/calculate", data={
        "operation": "celsius_to_fahrenheit",
        "number_1": number_1,
        "number_2": number_2
    })

    # Run assertions
    fahrenheit_answer = float(number_1 * 9 / 5 + 32)
    matching_string = f"Result: {fahrenheit_answer} °F"
    assert response.status_code == 200
    assert matching_string.encode() in response.data


def test_celsius_to_kelvin_1():
    """
    Make a POST request to the /calculate endpoint to perform
    the celsius_to_kelvin operation

    This unit test will run with manually provided test
    values
    """
    # Test variables
    number_1 = 100
    number_2 = 5

    # Make HTTP response
    response = application.test_client().post("/calculate", data={
        "operation": "celsius_to_kelvin",
        "number_1": number_1,
        "number_2": number_2
    })

    # Run assertions
    matching_string = "Result: 373.15"
    assert response.status_code == 200
    assert matching_string.encode() in response.data


def test_celsius_to_kelvin_2():
    """
    Make a POST request to the /calculate endpoint to perform
    the celsius_to_kelvin operation

    This unit test will run with randomly generated test
    values
    """
    # Test variables
    number_1 = random.randint(1, 1000)
    number_2 = random.randint(1, 1000)

    # Make HTTP response
    response = application.test_client().post("/calculate", data={
        "operation": "celsius_to_kelvin",
        "number_1": number_1,
        "number_2": number_2
    })

    # Run assertions
    kelvin_answer = number_1 + 273.15
    matching_string = f"Result: {kelvin_answer}"
    assert response.status_code == 200
    assert matching_string.encode() in response.data


def test_number_to_hexadecimal_1():
    """
    Make a POST request to the /calculate endpoint to perform
    the to_hexadecimal conversion operation

    This unit test will run with manually provided test
    values
    """
    # Test variables
    number_1 = 255
    number_2 = 128

    # Make HTTP response
    response = application.test_client().post("/calculate", data={
        "operation": "to_hexadecimal",
        "number_1": number_1,
        "number_2": number_2
    })

    # Run assertions
    matching_string = "Result: FF"
    assert response.status_code == 200
    assert matching_string.encode() in response.data


def test_number_to_hexadecimal_2():
    """
    Make a POST request to the /calculate endpoint to perform
    the to_hexadecimal conversion operation

    This unit test will run with randomly generated test
    values
    """
    # Test variables
    number_1 = random.randint(1, 255)
    number_2 = random.randint(1, 255)

    # Make HTTP response
    response = application.test_client().post("/calculate", data={
        "operation": "to_hexadecimal",
        "number_1": number_1,
        "number_2": number_2
    })

    # Run assertions
    hexadecimal_answer = hex(number_1).replace("0x", "").upper()
    matching_string = f"Result: {hexadecimal_answer}"
    assert response.status_code == 200
    assert matching_string.encode() in response.data


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
    response = application.test_client().post("/calculate", data={
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
    response = application.test_client().post("/calculate", data={
        "operation": "custom_log_base",
        "number_1": number_1,
        "number_2": number_2
    })

    # Run assertions
    custom_log_base_answer = float(math.log(number_1, number_2))
    matching_string = f"Result: {custom_log_base_answer}"
    assert response.status_code == 200
    assert matching_string.encode() in response.data


def test_factorial_1():
    """
    Make a POST request to the /calculate endpoint to perform
    the factorial operation

    This unit test will run with manually provided test
    values
    """
    # Test variables
    number_1 = 5
    number_2 = 2

    # Make HTTP response
    response = application.test_client().post("/calculate", data={
        "operation": "factorial",
        "number_1": number_1,
        "number_2": number_2
    })

    # Run assertions
    matching_string = "Result: 120"
    assert response.status_code == 200
    assert matching_string.encode() in response.data


def test_factorial_2():
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
    response = application.test_client().post("/calculate", data={
        "operation": "factorial",
        "number_1": number_1,
        "number_2": number_2
    })

    # Run assertions
    factorial_answer = math.factorial(int(number_1))
    matching_string = f"Result: {factorial_answer}"
    assert response.status_code == 200
    assert matching_string.encode() in response.data


def test_log10_1():
    """
    Make a POST request to the /calculate endpoint to perform
    the log10 operation

    This unit test will run with manually provided test
    values
    """
    # Test variables
    number_1 = 1000000
    number_2 = 1000

    # Make HTTP response
    response = application.test_client().post("/calculate", data={
        "operation": "log10",
        "number_1": number_1,
        "number_2": number_2
    })

    # Run assertions
    matching_string = "Result: 6"
    assert response.status_code == 200
    assert matching_string.encode() in response.data


def test_log10_2():
    """
    Make a POST request to the /calculate endpoint to perform
    the log10 operation

    This unit test will run with randomly generated test
    values
    """
    # Test variables
    number_1 = random.randint(1, 1000)
    number_2 = random.randint(1, 1000)

    # Make HTTP response
    response = application.test_client().post("/calculate", data={
        "operation": "log10",
        "number_1": number_1,
        "number_2": number_2
    })

    # Run assertions
    log10_answer = math.log10(number_1)
    matching_string = f"Result: {log10_answer}"
    assert response.status_code == 200
    assert matching_string.encode() in response.data


def test_modulus_1():
    """
    Make a POST request to the /calculate endpoint to perform
    the modulus operation

    This unit test will run with manually provided test
    values
    """
    # Test variables
    number_1 = 5
    number_2 = 2

    # Make HTTP response
    response = application.test_client().post("/calculate", data={
        "operation": "modulus",
        "number_1": number_1,
        "number_2": number_2
    })

    # Run assertions
    matching_string = "Result: 1"
    assert response.status_code == 200
    assert matching_string.encode() in response.data


def test_modulus_2():
    """
    Make a POST request to the /calculate endpoint to perform
    the modulus operation

    This unit test will run with randomly generated test
    values
    """
    # Test variables
    number_1 = random.randint(1, 1000)
    number_2 = random.randint(1, 1000)

    # Make HTTP response
    response = application.test_client().post("/calculate", data={
        "operation": "modulus",
        "number_1": number_1,
        "number_2": number_2
    })

    # Run assertions
    modulus_answer = number_1 % number_2
    matching_string = f"Result: {modulus_answer}"
    assert response.status_code == 200
    assert matching_string.encode() in response.data


def test_multiplication_1():
    """
    Make a POST request to the /calculate endpoint to perform
    the multiplication operation

    This unit test will run with manually provided test
    values
    """
    # Test variables
    number_1 = 5
    number_2 = 3

    # Make HTTP response
    response = application.test_client().post("/calculate", data={
        "operation": "multiplication",
        "number_1": number_1,
        "number_2": number_2
    })

    # Run assertions
    matching_string = "Result: 15.0"
    assert response.status_code == 200
    assert matching_string.encode() in response.data


def test_multiplication_2():
    """
    Make a POST request to the /calculate endpoint to perform
    the multiplication operation

    This unit test will run with randomly generated test
    values
    """
    # Test variables
    number_1 = random.randint(1, 1000)
    number_2 = random.randint(1, 1000)

    # Make HTTP response
    response = application.test_client().post("/calculate", data={
        "operation": "multiplication",
        "number_1": number_1,
        "number_2": number_2
    })

    # Run assertions
    multiplication_answer = number_1 * number_2
    matching_string = f"Result: {multiplication_answer}"
    assert response.status_code == 200
    assert matching_string.encode() in response.data


def test_square_root_1():
    """
    Make a POST request to the /calculate endpoint to perform
    the sqrt operation

    This unit test will run with manually provided test
    values
    """
    # Test variables
    number_1 = 16
    number_2 = 64

    # Make HTTP response
    response = application.test_client().post("/calculate", data={
        "operation": "sqrt",
        "number_1": number_1,
        "number_2": number_2
    })

    # Run assertions
    matching_string = "Result: ± 4.0"
    assert response.status_code == 200
    assert matching_string.encode() in response.data


def test_square_root_2():
    """
    Make a POST request to the /calculate endpoint to perform
    the sqrt operation

    This unit test will run with randomly generated test
    values
    """
    # Test variables
    number_1 = random.randint(1, 1000)
    number_2 = random.randint(1, 1000)

    # Make HTTP response
    response = application.test_client().post("/calculate", data={
        "operation": "sqrt",
        "number_1": number_1,
        "number_2": number_2
    })

    # Run assertions
    square_root_answer = math.pow(number_1, 0.5)
    matching_string = f"Result: ± {square_root_answer}"
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
    response = application.test_client().post("/calculate", data={
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
    response = application.test_client().post("/calculate", data={
        "operation": "subtraction",
        "number_1": number_1,
        "number_2": number_2
    })

    # Run assertions
    subtraction_answer = number_1 - number_2
    matching_string = f"Result: {subtraction_answer}"
    assert response.status_code == 200
    assert matching_string.encode() in response.data
