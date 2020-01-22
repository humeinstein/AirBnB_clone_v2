#!/usr/bin/python3                                                              
""" simple flask app """
from flask import Flask as fapp
from flask import abort, render_template

app = fapp(__name__)
app.url_map.strict_slashes = False

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


@app.route('/python/')
@app.route('/python/<text>')
def displayPython(text="is cool"):
    """ show python followed by string """
    if (text == "is cool"):
        return("Python {}".format(text))
    else:
        return("Python {}".format(text.replace("_", " ")))

@app.route('/number/<int:n>')
def displayNumber(n):
    """ displays number if unsigned int """
    if n.isnumeric():
        return("{} is a number".format(n))
    else:
        abort(404)

@app.route('/number_template/<n>')
def template(n):
    """ return if unsigned int """
    if n.isnumeric():
        return render_template('5-number.html', n=n)
    else:
        abort(404)


@app.route("/number_odd_or_even/<n>")
def number_odd_or_even_template(n):
    """ return n if int """
    try:
        n = int(n)
        if n % 2 == 0:
            st = "even"
        else:
            st = "odd"
        return render_template('6-number_odd_or_even.html', n=n, s=s)
    except:
        abort(404)

if __name__ == "__main__":
    app.run()
