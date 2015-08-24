"""
Initialise App
"""

from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config")
app.config.from_pyfile("config.py")

# DB connection
#FIXME

from app import models
from app import views
