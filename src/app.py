from flask import Flask, render_template

from helpers import foo

app = Flask(__name__)

@app.route("/")
def hello_world():
    message = foo()

    return  render_template('home.html',
            message=message)