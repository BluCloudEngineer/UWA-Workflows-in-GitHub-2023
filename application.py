"""
Python Flask Calculator Web Application
"""

# Imports
import math
from flask import Flask, render_template, request

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
    if operation == "celsius_to_fahrenheit":
        fahrenheit = float(number_1 * 9 / 5 + 32)
        result = f"{fahrenheit} °F"

    if operation == "celsius_to_kelvin":
        result = float(number_1) + 273.15

    if operation == "to_hexadecimal":
        result = hex(int(number_1)).replace("0x", "").upper()

    if operation == "custom_log_base":
        base = float(request.form["number_2"])
        result = math.log(number_1, base)

    if operation == "factorial":
        result = math.factorial(int(number_1))

    if operation == "log10":
        result = math.log10(number_1)

    if operation == "modulus":
        divider = float(request.form["number_2"])
        result = number_1 % divider

    if operation == "multiplication":
        number_2 = float(request.form["number_2"])
        result = number_1 * number_2

    if operation == "sqrt":
        result = f"± {math.sqrt(number_1)}"

    if operation == "subtraction":
        number_2 = float(request.form["number_2"])
        result = number_1 - number_2

    if operation == "to_binary":
        result = format(number_1, '08b')

    return render_template("index.html", result=result)


# Run the Flask application
if __name__ == "__main__":
    application.debug = True
    application.run()
