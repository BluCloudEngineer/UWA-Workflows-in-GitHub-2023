"""
Python Flask Calculator Web Application unit tests
"""

# Imports
from application import application


def test_default_route():
    """
    Make a GET request to "/" and return a status code of 200
    """
    # Make HTTP response
    response = application.test_client().get("/")

    # Run assertions
    assert response.status_code == 200
    assert response.status_code != 404

def test_pr():
    """
    Manual test 1
    """
    a = 1
    b = 1
    assert a == b

def test_pr_2():
    """
    Manual test 2
    """
    a = 100
    b = a
    assert a == b
