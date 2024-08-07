from os import getenv

from .. import app
from sqlalchemy import select
from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required
from requests import post, get
from datetime import datetime
from .. db import User, Session


BACKEND_URL = getenv("BACKEND_URL")




@app.post("/append_balance")
@login_required
def append_balance():
    global untouchable
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
            "comment": request.form["comment"]
        }

        balance = post(f"{BACKEND_URL}/append_balance", json=data)
        
        if balance.status_code == 200:
            return redirect(url_for("index"))
        error_code = balance.status_code
        return render_template("error.html", error_code=error_code)
    

@app.get("/append_balance")
def get_append_balance():
    nickname = current_user.email.split('@')[0]
    with Session.begin() as session:
        untouchable = session.scalar(select(User).where(User.email == current_user.email))
        untouchable_var = untouchable.untouchable
    return render_template("append_balance.html", untouchable_var=untouchable_var)