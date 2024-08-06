# from os import getenv
# from flask import render_template
# from flask_login import current_user
# from requests import get

# from .. import app

# BACKEND_URL = getenv("BACKEND_URL")

# @app.get("/")
# def index():
#     balances = {
#         "balances": get(f"{BACKEND_URL}/get_balances").json()
#     }
    
#     nickname = ""
#     total_sum = 0
    
#     if current_user.is_authenticated:
#         nickname = current_user.email.split('@')[0]
#         response = get(f"{BACKEND_URL}/get_total_sum")
#         if response.status_code == 200:
#             total_sum = response.json().get("total_sum", 0)
    
#     return render_template("index.html", nickname=nickname, total_sum=total_sum, **balances)


from os import getenv
from flask import render_template
from flask_login import current_user, login_required
from requests import get
from .. import app
from ..db import User

BACKEND_URL = getenv("BACKEND_URL")

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
            return response.status_code
        

