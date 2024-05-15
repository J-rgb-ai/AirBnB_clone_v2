#!/usr/bin/python3
"""
Script to start a Flask web application.
"""

from flask import Flask, abort

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route for the root path that displays "Hello HBNB!"
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route for "/hbnb" that displays "HBNB"
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route "/c/<text>" displays "C ", followed by value of text variable
    (replace underscore _ symbols with a space)
    """
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Route "/python/<text>" displays "Python ", follow by value of text variable
    (replace underscore _ symbols with a space)
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    Route "/number/<n>" that displays "n is number" only if n is an integer
    """
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
