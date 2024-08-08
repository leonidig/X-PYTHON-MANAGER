from os import getenv

from .. import app

from flask_login import current_user, login_required
from flask import redirect, url_for
from requests import get, delete


BACKEND_URL = getenv("BACKEND_URL")


@app.get("/delete_balance/<int:balance_id>")
@login_required
def delete_balance(balance_id):
    user = current_user.email.split("@")[0]
    balance = get(f'{BACKEND_URL}/balance/{balance_id}').json()
    owner = balance.get("owner")
    print(owner)
    data = {
        "balance_id": balance_id,
        "current_user": user
    }
    deleted_balance = delete(f"{BACKEND_URL}/delet_balance/{balance_id}", json=data)
    if deleted_balance.status_code == 200:
        return redirect(url_for('index'))
    return(f'Error {deleted_balance.status_code}')