from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, SubmitField
from wtforms.validators import InputRequired

from project import db, bcrypt
from project.models.user import User


def user_confirmation(email, password):
    """This checks if a user exists or not and returns an object if it does or None"""
    requested_user = db.get_one(email=email, cls=User)
    if requested_user:
        print(str(requested_user.password_hash))
        # if requested_user.check_password(attempted_password=password):
        if bcrypt.check_password_hash(requested_user.password_hash, password):
            return requested_user
    else:
        return None


class LoginForm(FlaskForm):
    email = EmailField(label='Email', validators=[InputRequired('Enter a valid email address.')])
    password = PasswordField(label='Password', validators=[InputRequired('Enter your password')])
    submit = SubmitField(label='Login')
