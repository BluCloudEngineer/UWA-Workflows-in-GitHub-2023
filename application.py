# Imports
from flask import Flask, render_template, request

# Initialise the Flask application
application = Flask(__name__) # You must use the word "application" for this to work in AWS

# Add routes
@application.route("/")
def index():
    return render_template("index.html")

@application.route("/calculate", methods=["POST"])
def calculate():
    # Required values
    result = None
    operation = request.form["operation"]
    #number_1 = float(request.form["number_1"])
    #number_2 = float(request.form["number_2"])

    # Perform logic
    # TODO

    return render_template("index.html", result = result)



# Run the Flask application
if __name__ == "__main__":
    application.debug = True
    application.run()
