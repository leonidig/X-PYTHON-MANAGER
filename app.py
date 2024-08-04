from os import getenv



from forms import LoginForm, RegisterForm
from db import User, Session

from flask import Flask, render_template, flash, redirect, url_for
from flask_login import login_user, current_user, login_required, LoginManager
from sqlalchemy import select
from requests import get
from dotenv import load_dotenv


load_dotenv()
SECRET_KEY = getenv("SECRET_KEY")
app = Flask("frontend")
app.config['SECRET_KEY'] = SECRET_KEY
BACKEND_URL = getenv("BACKEND_URL")
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@app.get("/")
def index():
    balances = {
        "balances": get(f"{BACKEND_URL}/get_balances").json()
    }
    # print(balances)
    nickname = " "
    if current_user.is_authenticated:
        nickname = current_user.email.split('@')[0]
        return render_template("index.html", nickname=nickname)
    return render_template("index.html", **balances)



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




@login_manager.user_loader
def load_user(user_id):
    with Session.begin() as session:
        user = session.scalar(select(User).where(User.id == user_id))
        if user:
            user = User(email=user.email)
            return user
    

@app.get('/register')
def register():
    form = RegisterForm()
    return render_template('form_template.html', form=form)

@app.post('/register')
def register_post():
    form = RegisterForm()
    if form.validate_on_submit():
       with Session.begin() as session:
           user = session.scalar(select(User).where(User.email == form.email.data))
           if user:
               flash("User exists!")
               return redirect(url_for('register'))
           pwd = form.password.data
           user = User(
               nickname = form.email.data.split('@')[0],
               email = form.email.data,
               password = pwd,
           )
           session.add(user)
       return redirect(url_for('login'))
    return render_template('form_template.html', form=form)

@app.get('/login')
def login():
    form = LoginForm()
    return render_template('form_template.html', form=form)

@app.post('/login')
def login_post():
    form = LoginForm()
    if form.validate_on_submit():
        with Session.begin() as session:
            user = session.query(User).where(User.nickname == form.nickname.data).first()
            if user:
                if user.password == form.password.data:
                    login_user(user)
                    return redirect(url_for("index"))
                flash("Wrong password")
            else:
                flash("Wrong nickname")
    return render_template('form_template.html', form=form)





if __name__ == "__main__":
    app.run(debug=True, port=5000)