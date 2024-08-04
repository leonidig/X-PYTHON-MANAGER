from flask import Flask, render_template
from requests import get


app = Flask("frontend")
BACKEND_URL = "http://127.0.0.1:8000"


@app.get("/")
def index():
    balances = {
        "balances": get(f"{BACKEND_URL}/get_balances").json()
    }
    print(balances)
    return render_template("index.html", **balances)



@app.get("/balance/<int:balance_id>")
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


if __name__ == "__main__":
    app.run(debug=True, port=5000)