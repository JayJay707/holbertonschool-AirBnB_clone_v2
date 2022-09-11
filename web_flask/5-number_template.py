#!/usr/bin/python3
"""
flask model for route
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    """
        hbnb route page
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def index():
    """
        /hbnb page
    """
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def C():
    """
        /C route
    """
    return 'C {:s}'.format(text.replace('_', ' '))

@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python():
    """
        /Python route
    """
    return 'C {:s}'.format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def number():
    """
        /number route
    """
    return '{} is a number'.format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template():
    """
        /template route
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)