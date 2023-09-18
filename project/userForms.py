from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from mongoengine import BinaryField, ImageField
from wtforms import StringField, SelectField, FileField, EmailField, DateTimeField, IntegerField, PasswordField, \
    SubmitField, RadioField
from wtforms.validators import InputRequired, ValidationError, EqualTo

from project.models.user import User


def validate_email(input_email):
    """it checks if a user with a particular email exist"""
    try:
        obj = User.objects.get(email=input_email)
        return obj
    except Exception:
        return None


class UserForm(FlaskForm):
    first_name = StringField(label='First Name', validators=[InputRequired()])
    last_name = StringField(label='Last Name', validators=[InputRequired()])
    email = EmailField(label='Email', validators=[InputRequired()])
    password = PasswordField(label='Password', validators=[InputRequired()])
    password1 = PasswordField(label='Confirm Password', validators=[EqualTo('password'), InputRequired()])
    vehicle_model = StringField(label='Vehicle Model', validators=[InputRequired()])
    plate_number = StringField(label='Plate Number', validators=[InputRequired()])
    vehicle_image = FileField(label='Vehicle Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only')])
    profile_pic = FileField(label='Profile picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only')])
    submit = SubmitField(label='Sign up')

    # def validate_plate_number(self, input_username):
    #     """it checks if a user with a particular username exist"""
    #     from models import storage
    #     customer = storage.get(attr=input_username, cls=Customers)
    #     if customer:
    #         raise ValidationError('Username already exist')
