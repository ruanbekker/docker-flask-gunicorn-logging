import os
import sys
import logging
import json_logging
from flask import render_template
from app import app

json_logs = os.environ.get('JSON_LOGS', True)

@app.before_first_request
def setup_logging():
    if not app.debug:
        print('debug disabled')
        app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.INFO)
    if json_logs:
        print('json enabled')
        json_logging.init_non_web(enable_json=True)
        logger = logging.getLogger("json-logger")
        app.logger.setLevel(logging.INFO)
        app.logger.addHandler(logging.StreamHandler(sys.stdout))
    else:
        print('debug enabled')
        app.logger.addHandler(logging.StreamHandler())
        app.logger.setLevel(logging.DEBUG)

@app.route('/')
def home():
    return render_template("index.html")
