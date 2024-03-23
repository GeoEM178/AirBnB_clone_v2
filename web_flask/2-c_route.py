#!/usr/bin/python3
"""
first route and flask init
"""

from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def start_page():
    """start_page route with simple string"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """returns string HBNB"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def sec_with_param(text):
  """_summary_

  Args:
      text (string): from user params
  """

  return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')