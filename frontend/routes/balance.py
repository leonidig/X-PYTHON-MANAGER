from os import getenv

from .. import app
from sqlalchemy import select
from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required
from requests import post, get
from datetime import datetime
from .. db import User, Session


BACKEND_URL = getenv("BACKEND_URL")


@app.get("/append_balance")
def get_append_balance():
    return render_template("append_balance.html")



@app.post("/append_balance")
@login_required
def append_balance():
    now = str(datetime.now())
    nickname = current_user.email.split('@')[0]
    with Session.begin() as session:
        untouchable = session.scalar(select(User).where(User.email == current_user.email))
        data = {
            "current_user": nickname
        }
        response = get(f"{BACKEND_URL}/get_total_sum", json=data)
        if response.status_code == 200:
            total_sum = response.json()
        data = {
            "owner": current_user.email.split('@')[0],
            "total": request.form['append_number'],
            "date": now[:16],
            "theme": request.form['choice'],
            "untouchable": untouchable.untouchable,
        }
        balance = post(f"{BACKEND_URL}/append_balance", json=data)

        if balance.status_code == 200:
            return redirect(url_for("index"))
        return f"Error {balance.status_code}"