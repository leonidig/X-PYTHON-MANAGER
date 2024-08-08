from os import getenv

from .. import app
from flask_login import current_user
from flask import render_template, request
from requests import get



BACKEND_URL = getenv("BACKEND_URL")



@app.get("/search")
def search():
    query = request.args.get('query','')
    if query:
        nickname = current_user.email.split('@')[0]
        data = {
            "current_user": nickname
        }
        balances = get(f"{BACKEND_URL}/get_balances", json=data).json()
        filtered = [balance for balance in balances if query.lower() in balance['comment'].lower()]
        return render_template("index.html", balances = filtered, query = query)