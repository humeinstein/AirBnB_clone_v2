#!/usr/bin/python3
""" simple flask app """
from flask import Flask as fapp


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

@app.route('/number_template/<int:n>')
def displayHtml(n):
    """ display html if n is # """
    return render_template('5-nummber.html', number=n)


if __name__ == "__main__":
    app.run()
