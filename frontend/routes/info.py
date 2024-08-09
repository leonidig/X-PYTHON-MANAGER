from os import getenv


from .. import app


from flask import render_template
from flask_login import login_required, current_user

from requests import get




BACKEND_URL = getenv("BACKEND_URL")


@app.get("/balance/<int:balance_id>")
@login_required
def balance(balance_id):
    nickname = current_user.email.split("@")[0]
    data = {
        "current_user": nickname
    }
    balances_response = get(f"{BACKEND_URL}/balance/{balance_id}", json=data)
    if balances_response.status_code == 200:
        selected_balance = balances_response.json()
        return render_template("info.html", balance=selected_balance, balance_id=balance_id)
    else:
        error_code = balances_response.status_code
        return render_template("error.html", error_code=error_code)
    