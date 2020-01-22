#!/usr/bin/python3
""" simple flask app """
from flask import Flask as fapp


app = fapp(__name__)


@app.route("/")
def sayHi():
    """ say hi when called """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ hbnb dir """
    return "HBNB"


@app.route("/c/<text>")
def c_place(content):
    """ return C and string """
    return ("C {}".format(content.replace('_', ' ')))


if __name__ == "__main__":
    app.run()
