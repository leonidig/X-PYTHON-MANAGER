from os import getenv
from flask import render_template
from flask_login import current_user, login_required
from requests import get
from .. import app
from ..db import User

BACKEND_URL = getenv("BACKEND_URL")# "http://127.0.0.1:8000"

@app.get("/")
@login_required
def index():

    nickname = ""

    # total_sum = 0
    
    if current_user.is_authenticated:
        nickname = current_user.email.split('@')[0]
        data = {
            "current_user": nickname
        }
        response = get(f"{BACKEND_URL}/get_total_sum", json=data)
        if response.status_code == 200:
            total_sum = response.json()
            balances = {
                "balances": get(f"{BACKEND_URL}/get_balances", json=data).json()
            }
            # print("*" * 80)
            # print(balances)
            return render_template('index.html', **balances, nickname=nickname, total_sum=total_sum)
           
        else:
            error_code = response.status_code
            return render_template("error.html", error_code=error_code)