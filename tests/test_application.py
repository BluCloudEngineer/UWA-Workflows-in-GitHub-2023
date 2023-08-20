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

def test_pr():
    """
    Manual test
    """
    a = 1
    b = 1
    assert a != b
