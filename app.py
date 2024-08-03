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


if __name__ == "__main__":
    app.run(debug=True, port=5000)