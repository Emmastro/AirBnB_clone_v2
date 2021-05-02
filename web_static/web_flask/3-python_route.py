#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def index():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def C_is_fun(text):
    return "C " + text.replace("_", " ")


@app.route("/python")
def python():
    return "Python is cool"


@app.route("/python/<text>")
def Python_is_magic(text):
    return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
