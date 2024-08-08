from .. import app
from flask import render_template



@app.get("/about")
def about():
    return render_template('about.html')