import os
from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

json_logs = os.environ.get('JSON_LOGS', True)

from app import views
