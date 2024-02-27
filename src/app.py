
import os
import time

from flask import Flask, render_template
from celery import Celery

from dotenv import load_dotenv

from helpers import foo

load_dotenv()

app = Flask(__name__)

celery = Celery(
    __name__,
    broker=os.getenv('BROKER'),
    backend=os.getenv('BACKEND')
)

@app.route("/")
def hello_world():
    message = foo()

    return  render_template('home.html',
            message=message)

@celery.task
def divide(x, y):
    time.sleep(5)
    return x / y