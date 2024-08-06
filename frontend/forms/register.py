from flask_wtf import FlaskForm
from wtforms import (
    EmailField,
    StringField,
    PasswordField,
    SubmitField,
    FloatField
)
from wtforms.validators import (
    DataRequired,
    EqualTo,
    Email,
)


class RegisterForm(FlaskForm):
    email = EmailField(validators=[DataRequired(), Email(),])
    password = PasswordField(validators=[DataRequired(),])
    password_confirm = PasswordField(validators=[DataRequired(), EqualTo("password")])
    untouchable = FloatField(validators=[DataRequired(),])
    submit = SubmitField("Register")