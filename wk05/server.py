from flask import Flask, jsonify, request
from names_ages import add_name_age, get_names_ages, clear_names_ages, edit_name_age

# Initialise the flask server
APP = Flask(__name__)

# Define the routes
@APP.route("/addnameage", methods=["POST"])
def addnameage():
    data = request.get_json()
    name = data["name"]
    dob = data["dob"]
    add_name_age(name, dob)
    return {}


@APP.route("/editname", methods=["PUT"])
def addnameageput():
    data = request.get_json()
    name = data["name"]
    dob = data["dob"]
    edit_name_age(name, dob)
    return {}


@APP.route("/getnamesages", methods=["GET"])
def getnamesages():
    """
    Make sure to convert the args to an int as by default all params are strings
    Also use .get() and give it a default value so that the parameter can be
    optional
    """
    min_age = int(request.args.get("min_age", 0))
    return jsonify(get_names_ages(min_age))


@APP.route("/clear", methods=["DELETE"])
def clear():
    clear_names_ages()
    return {}


# Run the server
if __name__ == "__main__":
    APP.run(debug=True, port=8080)
