"""
Python Flask Calculator Web Application
"""

# Imports

from flask import Flask, render_template, request
import math

# Initialise the Flask application
# You must use the word "application" for this to work in AWS
application = Flask(__name__)

# Add routes


@application.route("/")
def index():
    """
    Return the main calculator webpage
    """
    return render_template("index.html")


@application.route("/calculate", methods=["GET"])
def calculate_redirect():
    """
    If the user makes a GET request to the /calculate path,
    return the main calculator webpage
    """
    return render_template("index.html")


@application.route("/calculate", methods=["POST"])
def calculate():
    """
    Perform mathematical operations and return the result to
    the main calculator webpage
    """
    # Required values
    result = None
    operation = request.form["operation"]
    number_1 = float(request.form["number_1"])

    # Perform mathematical operations
    if operation == "addition":
        number_2 = float(request.form["number_2"])
        result = number_1 + number_2

    if operation == "celsius_to_fahrenheit":
        result = (number_1 * 9/5) + 32.0
    
    if operation == "natural_log":
        result = math.log(number_1)
    return render_template("index.html", result=result)


# Run the Flask application
if __name__ == "__main__":
    application.debug = True
    application.run()
