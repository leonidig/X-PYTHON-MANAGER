from .. import app
from flask import render_template
from flask_login import login_required



@app.get("/about")
@login_required
def about():
    return render_template('about.html')