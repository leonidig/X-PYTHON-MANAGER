from .. import app
from ..db import Session, User
from ..forms import LoginForm, RegisterForm


from flask import flash, render_template, redirect, url_for
from flask_login import LoginManager, login_user

from sqlalchemy import select



login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)



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