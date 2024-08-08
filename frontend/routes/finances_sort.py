from os import getenv


from .. import app
from requests import get
from flask_login import current_user
from flask import render_template

BACKEND_URL = getenv("BACKEND_URL")


@app.get("/profit")
def profit():
    nickname = current_user.email.split("@")[0]
    data = {
        "current_user": nickname
    }

    profit_response = get(f"{BACKEND_URL}/profit", json=data)
    if profit_response.status_code == 200:
        profit = profit_response.json()
        return render_template("profit.html", profit=profit)
    error_code = profit_response.status_code
    return render_template("error.html", error_code=error_code)

@app.get("/loss")
def loss():
    nickname = current_user.email.split("@")[0]
    data = {
        "current_user": nickname
    }
    loss_response = get(f"{BACKEND_URL}/loss", json=data)
    if loss_response.status_code == 200:
        loss = loss_response.json()
        return render_template("loss.html", loss=loss)