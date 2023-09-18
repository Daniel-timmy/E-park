from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from mongoengine import IntField
from wtforms import EmailField, PasswordField, SubmitField, StringField, FileField
from wtforms.validators import InputRequired, EqualTo

from project import db, bcrypt
from project.models.admin import Admin


def admin_confirmation(email, password, admin_code):
    """This checks if a user exists or not and returns an object if it does or None"""
    # employee_code = ['1001', '1002', '1003', '1004', '1006']
    try:
        requested_user = db.get_one(email=email, cls=Admin)
        if requested_user:
            print(str(requested_user.password_hash))
            # if requested_user.check_password(attempted_password=password):
            if admin_code == requested_user.admin_code:
                if bcrypt.check_password_hash(requested_user.password_hash, password):
                    return requested_user
    except Exception:
        return None


def validate_admin_email(input_email):
    """it checks if a user with a particular email exist"""
    try:
        obj = Admin.objects.get(email=input_email)
        return obj
    except Exception:
        return None


class AdminForm(FlaskForm):
    email = EmailField(label='Email', validators=[InputRequired('Enter a valid email address.')])
    password = PasswordField(label='Password', validators=[InputRequired('Enter your password')])
    admin_code = StringField(label='Admin code')
    submit = SubmitField(label='Login')


class AForm(FlaskForm):
    first_name = StringField(label='First Name', validators=[InputRequired()])
    last_name = StringField(label='Last Name', validators=[InputRequired()])
    email = EmailField(label='Email', validators=[InputRequired()])
    password = PasswordField(label='Password', validators=[InputRequired()])
    password1 = PasswordField(label='Confirm Password', validators=[EqualTo('password'), InputRequired()])
    admin_code = IntField(required=True)
    submit = SubmitField(label='register')
