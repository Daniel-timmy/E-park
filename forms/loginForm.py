from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    email = EmailField(validators=[InputRequired('Enter a valid email address.')])
    password = PasswordField(validators=[InputRequired('Enter your password')])
    submit = SubmitField(label='Login')
