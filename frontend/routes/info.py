from os import getenv


from .. import app


from flask import render_template
from flask_login import login_required

from requests import get




BACKEND_URL = getenv("BACKEND_URL")


@app.get("/balance/<int:balance_id>")
@login_required
def get_balance_info(balance_id):
    balances = get(f"{BACKEND_URL}/get_balances").json()
    selected_balance = None
    for item in balances:
        if item.get('id')== balance_id:
            selected_balance = item
            break
    if selected_balance:
        return render_template("info.html", balance=selected_balance)
    else:
        return f"Could not found balance with id : {item}"