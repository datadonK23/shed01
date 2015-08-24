"""
Views
"""

from flask import render_template
from app import app#, connection
#from models import Features

# main page
@app.route("/")
def index(): 
    return render_template("index.html")

