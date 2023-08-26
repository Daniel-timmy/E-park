from datetime import datetime

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, SelectField, DateTimeField, IntegerField, SubmitField, RadioField
from wtforms.validators import InputRequired


class BookingForm(FlaskForm):
    lot = SelectField(choices=['EDU', 'FET', 'LSC', 'PHY', 'LAW'],
                      validators=[InputRequired()])
    space = SelectField(choices=['01', '02', '03', '04', '05', '06', '07', '08',
                                 '09', '10', '11', '12', '13', '15', '16', '17',
                                 '18', '19', '20', '21', '22', '23', '24', '25'],
                        validators=[InputRequired('Choose a parking space')])
    duration = IntegerField(validators=[InputRequired()])
    start_time = DateTimeField(default=datetime.utcnow())
    model = StringField(validators=[InputRequired()])
    plate_number = StringField(validators=[InputRequired()])
    reservation_type = RadioField(choices=[('unchecked', 'Unchecked'), ('Reservation', 'Reservation')],
                                  default='unchecked',
                                  id='reservation')  # to reduce the complexity of nav pills
    vehicle_image = FileField(label='Vehicle Image', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Images only')])
    submit = SubmitField(label='Make payment')
