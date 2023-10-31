#!/usr/bin/env python3
"""
flask app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    """
     This is the view that is called when the user clicks the hello button.
     @return The response to the request as a string ( html
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
