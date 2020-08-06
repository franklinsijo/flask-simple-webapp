#!/usr/bin/env python3

import logging
import sys
import os

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/flask-simple-webapp/')

from web import app as application