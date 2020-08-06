#!/usr/bin/env python3

from flask import Flask

app =  Flask(__name__)

from web import routes
app.register_blueprint(routes.app)