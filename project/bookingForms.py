from datetime import datetime

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, SelectField, DateTimeField, IntegerField, SubmitField, RadioField
from wtforms.validators import InputRequired


class BookingForm(FlaskForm):
    lot = SelectField(label='Lot', choices=['EDU', 'FET', 'LSC', 'PHY', 'LAW'],
                      validators=[InputRequired('Choose a parking lot.')])
    space = SelectField(label="Spaces", choices=['01', '02', '03', '04', '05', '06', '07', '08',
                                                 '09', '10', '11', '12', '13', '15', '16', '17',
                                                 '18', '19', '20', '21', '22', '23', '24', '25'],
                        validators=[InputRequired('Choose a parking space')])
    duration = IntegerField(label="Duration", validators=[InputRequired()])
    start_time = DateTimeField(label="Start time", default=datetime.utcnow())
    model = StringField(label="model", validators=[InputRequired()])
    time_unit = SelectField(choices=['weeks', 'days', 'hours'],
                            validators=[InputRequired()])

    plate_number = StringField(label="Plate number", validators=[InputRequired()])
    reservation_type = SelectField(
        choices=['Reservations', 'On spot'],
        validators=[InputRequired()])  # to reduce the complexity of nav pills
    vehicle_image = FileField(label='Vehicle Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only')])
    submit = SubmitField(label='Make payment')
