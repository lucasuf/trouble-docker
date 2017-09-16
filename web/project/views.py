from flask import request, render_template
from project.app import app

from project.models import *


@app.route('/')
def index():
    return render_template('index.html')
