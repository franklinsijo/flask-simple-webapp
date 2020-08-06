#!/usr/bin/env python3

from flask import Blueprint, render_template

app = Blueprint('app', __name__)

@app.route('/')
def display_app():
    return render_template('app.html')
