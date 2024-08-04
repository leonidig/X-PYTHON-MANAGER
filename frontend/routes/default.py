from os import getenv


from .. import app

from flask import render_template
from flask_login import current_user

from requests import get

BACKEND_URL = getenv("BACKEND_URL")



@app.get("/")
def index():
    balances = {
        "balances": get(f"{BACKEND_URL}/get_balances").json()
    }
    # print(balances)
    nickname = ""
    if current_user.is_authenticated:
        nickname = current_user.email.split('@')[0]
        return render_template("index.html", nickname=nickname)
    return render_template("index.html", **balances)
