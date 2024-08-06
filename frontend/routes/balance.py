from os import getenv

from .. import app

from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required
import requests
from datetime import datetime



BACKEND_URL = getenv("BACKEND_URL")


@app.get("/append_balance")
def get_append_balance():
    return render_template("append_balance.html")



@app.post("/append_balance")
@login_required
def append_balance():
    now = str(datetime.now())
    data = {
        "owner": current_user.email.split('@')[0],
        "total": request.form['append_number'],
        "date": now[:16]
    }
    balance = requests.post(f"{BACKEND_URL}/append_balance", json=data)
    if balance.status_code == 200:
        return redirect(url_for("index"))
    return f"Error {balance.status_code}"