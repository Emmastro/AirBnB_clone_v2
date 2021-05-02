#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_is_fun(text):
    return "C " + text.replace("_", " ")


@app.route("/python", strict_slashes=False)
def python():
    return "Python is cool"


@app.route("/python/<text>", strict_slashes=False)
def Python_is_magic(text):
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def n_is_a_number(n):
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', num=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', num=n)


@app.route('/states_list', strict_slashes=False)
def states_list():
    return render_template('7-states_list.html',
                           states=storage.all("State"))


@app.teardown_appcontext
def teardown(err):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
