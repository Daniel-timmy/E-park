from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, SelectField, FileField, EmailField, DateTimeField, IntegerField, PasswordField, \
    SubmitField, RadioField
from wtforms.validators import InputRequired


class UserForm(FlaskForm):
    first_name = StringField(label='First Name', validators=[InputRequired()])
    last_name = StringField(label='Last Name', validators=[InputRequired()])
    email = EmailField(label='Email', validators=[InputRequired()])
    password = PasswordField(label='Password', validators=[InputRequired()])
    password1 = PasswordField(label='Confirm Password', validators=[InputRequired()])
    vehicle_model = StringField(label='Vehicle Model', validators=[InputRequired()])
    plate_number = StringField(label='Plate Number', validators=[InputRequired()])
    vehicle_image = FileField(label='Vehicle Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only')])
    profile_pic = FileField(label='Vehicle Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only')])
    submit = SubmitField(label='Sign up')
