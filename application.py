# Imports
from flask import Flask

# Initialise the Flask application
application = Flask(__name__) # You must use the word "application" for this to work in AWS

# Add routes
@application.route("/")
def default_route():
    """
    Return a string of "Hello world!"
    """
    return "Hello world!"



# Run the Flask application
if __name__ == "__main__":
    application.debug = True
    application.run()
