#!/usr/bin/python3
'''Start web application with two routings'''


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''Return string when route queried'''

    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Return string when route queried'''

    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    '''Return reformatted text'''

    return 'C ' + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is_cool'):
    '''Reformat text based on optional variable'''

    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_is_int(n):
    '''Allow request if path variable is a valid integer'''

    return str(n) + ' is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''Retrieve template for request'''

    path = '5-number.html'
    return render_template(path, n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes+False)
def number_odd_or_even(n):
    '''Render template based on conditional'''

    path = '6-number_odd_or_even.html'
    return render_template(path, n=n)

if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
