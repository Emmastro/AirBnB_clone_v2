#!/usr/bin/python3
"""starts a flask web application"""
from flask import Flask 
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def inex():
    """displays 'Hello HBNB!""""
    return "Hello HBNB!"

if __name__ = "__main__":
    app.run(debug=True)