from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import InputRequired


class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[InputRequired('Enter a valid email address.')])
    password = PasswordField(label='Password', validators=[InputRequired('Enter your password')])
    submit = SubmitField(label='Login')
