"""
Write a simple Flask server that contains corresponding routes for adding 
names/ages and getting names/ages in `server.py`.

The routes should simply be stubs for now.
"""

# Add imports
from names_ages import add_name_age, get_names_ages, clear_names_ages
from flask import Flask, request, jsonify

# Add server intialiser
APP = Flask(__name__)

# route: "/addnameage"
@APP.route("/addnameage", methods=["POST"])
def addnameage():
    data = request.get_json()
    name = data["name"]
    dob = data["dob"]
    add_name_age(name, dob)
    return {}


# route: "/getnamesages"
@APP.route("/getnamesages", methods=["GET"])
def getnamesages():
    min_age = request.args.get('min_age')
    return jsonify(get_names_ages(min_age))


# route: "/clear"
@APP.route("/clear", methods=["DELETE"])
def clear():
    clear_names_ages()
    return {}


# Run server
if __name__ == "__main__":
    APP.run(debug=True, port=8080)
